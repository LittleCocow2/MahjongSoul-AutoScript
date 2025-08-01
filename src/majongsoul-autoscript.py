import uiautomator2 as u2
import random
import time
import cv2
import numpy as np
import os

# 资源文件路径（使用 assets 目录）
NEXT_ROUND_BUTTON_TEMPLATE = os.path.join("assets", "next_round_button.png")
tongban_path = os.path.join("assets", "tongban.png")
yuanshi_path = os.path.join("assets", "yuanshi.png")
chouka_path = os.path.join("assets", "chouka.png")
zhongju_path = os.path.join("assets", "zhongju.png")

# 获取手牌的坐标区域
hand_area = [(250, 980), (350, 975), (450, 985), (550, 980), (650, 1000), (750, 1000), (850, 1000), (950, 1000), (1050, 1000), (1150, 1000)]
zhan_xing = [(810, 710), (970, 710), (1100, 710)]

# 连接到雷电模拟器
def connect_device():
    device = u2.connect('127.0.0.1:5555')
    print("连接成功")
    return device

def play_random_tile(device, choice):
    # 修罗之战
    if choice == 2:
        # 随机选取 3 个不重复的坐标
        selected_positions = random.sample(hand_area, 3)
        for x, y in selected_positions:
            device.click(x, y)
        device.click(1385, 850)
    # 占星之战
    if choice == 1:
        x, y = random.choice(zhan_xing)
        device.click(x, y)
        time.sleep(0.2)
    # 随机出牌
    x, y = random.choice(hand_area)
    device.click(x, y)
    time.sleep(0.1)
    device.click(x, y)
    # 自动胡、碰、杠
    device.click(55, 615)
    time.sleep(0.2)
    device.click(55, 675)
    time.sleep(0.25)
    # 开始下一局
    if is_next_round_button_present(device, zhongju_path, option=1):
        time.sleep(1)
        if is_next_round_button_present(device, NEXT_ROUND_BUTTON_TEMPLATE):
            device.click(1550, 1000)
            device.click(1550, 1000)
            time.sleep(2)
            device.click(780, 800)
        else:
            if is_next_round_button_present(device, tongban_path) or is_next_round_button_present(device, yuanshi_path) or is_next_round_button_present(device, chouka_path):
                print("在主界面或抽卡界面")
                return
            else:
                device.click(1800, 1000)
    time.sleep(0.25)
    print('正在运行')

def take_screenshot(device):
    """ 直接获取屏幕截图并转换为 OpenCV 格式 """
    screenshot_data = device.screenshot()  # 获取截图数据（PIL Image）
    screenshot = np.array(screenshot_data)  # 转换为 NumPy 数组
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换为 OpenCV 格式
    return screenshot

def match_template(image, template, threshold=0.9):
    """
    在整张截图中寻找“下一局”按钮
    :param image: 整张屏幕截图
    :param template: “下一局”按钮的模板
    :param threshold: 匹配阈值（0~1，越接近1要求匹配越严格）
    :return: 按钮是否存在
    """
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转灰度
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  # 模板转灰度
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val >= threshold

def is_next_round_button_present(device, path, option=0):
    """
    判断 '下一局' 按钮是否存在
    :param device: uiautomator2 设备对象
    :param path: 模板图片路径
    :param option: 匹配选项（0: 默认阈值, 1: 低阈值）
    :return: True（按钮存在）或 False（按钮不存在）
    """
    screenshot = take_screenshot(device)
    next_round_template = cv2.imread(path)
    if screenshot is None or next_round_template is None:
        print("无法加载截图或模板，请检查文件路径！")
        return False
    return match_template(screenshot, next_round_template, threshold=0.3 if option == 1 else 0.9)

def main():
    print("1. 占星之战")
    print("2. 修罗之战")
    print("3. 其他")
    choice = int(input("请选择模式（填数字）："))
    device = connect_device()
    while True:
        if is_next_round_button_present(device, tongban_path) or is_next_round_button_present(device, yuanshi_path) or is_next_round_button_present(device, chouka_path):
            print("在主界面或抽卡界面")
            return
        play_random_tile(device, choice)
        time.sleep(0.75)  # 模拟人类操作

if __name__ == "__main__":
    main()