# Mahjong Soul Auto Script

This is an automation script for *Mahjong Soul*, supporting modes like "Four-Player Mahjong" (and others) through image recognition for automatic tile playing and next-round operations.

## Features
- Automatic tile playing (supports random tile selection and Four-Player Mahjong mode)
- Automatic detection of the "Next Round" button
- Compatible with Leidian Emulator (1920x1080 resolution)
- Low memory usage, suitable for background running

## Directory Structure
- `src/`: Source code directory containing the main script `majongsoul-autoscript.py`
- `assets/`: Resource directory containing 5 image templates (`next_round_button.png`, `tongban.png`, `yuanshi.png`, `chouka.png`, `zhongju.png`)
- `requirements.txt`: List of Python dependencies
- `LICENSE`: MIT License

## Installation

### 1. Install Leidian Emulator (or Other Android Emulators)
- Download and install Leidian Emulator 9: [Leidian Emulator Official Site](https://www.ldmnq.com/?n=401674)
  - If using another Android emulator, refer to its documentation and modify the IP/port in the script accordingly.
- Open the emulator, set the resolution to **1920x1080** in settings, then restart the emulator.
- Download the *Mahjong Soul* APK ([Mahjong Soul Official Site](https://www.mahjongsoul.com/) or other trusted sources), drag it into the emulator to install, or download via the emulator’s built-in browser.
- Log in to your *Mahjong Soul* account and complete any updates.

**Note**: Do not use a multi-instance manager to start the emulator; directly click the Leidian Emulator 9 icon.

### 2. Configure ADB
- Right-click the Leidian Emulator 9 shortcut and select "Open file location."
- In the folder’s address bar, type `cmd` and press Enter to open a command prompt.
- Run the following command:
  ```bash
  adb shell
  ```
- Close the command prompt after execution.

### 3. Install Python Dependencies
- Ensure Python 3.8 or higher is installed.
- Clone or download this repository to your local machine.
- Navigate to the project root directory and install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Ensure the 5 image templates in the `assets/` directory are correctly referenced by `majongsoul-autoscript.py`.

## Usage
1. Launch Leidian Emulator and start *Mahjong Soul*, entering the main interface or an in-game session.
2. Navigate to the `src/` directory and run the script:
   ```bash
   cd src
   python majongsoul-autoscript.py
   ```
3. Select a mode as prompted:
   - **1**: Zhan Xing (Astrology Battle)
   - **2**: Xiu Luo (Shura Battle)
   - **3**: Other
4. The script will run automatically until it detects the main interface or card-draw interface (e.g., when coins are depleted or the game ends).

**Stopping the Script**: Close the command prompt window.

## Notes
- **Compliance**: Strictly adhere to *Mahjong Soul*’s Terms of Service. Using this script may risk account bans; use with caution.
- **Running Duration**: Avoid extended usage. Recommended limits:
  - Ranked Matches: Up to 8 hours daily
  - Event Matches: Up to 12 hours daily
- **Image Templates**: Ensure the image templates in `assets/` match the game’s resolution (1920x1080), or recognition may fail.
- **Script Behavior**: The script stops automatically upon detecting the main or card-draw interface. If it crashes, it may have been started on the main interface; start it during a match or mode selection instead.
- **Recommended Modes**: Four-Player Mahjong is most efficient. Suggested priority: Ranked Matches > Limited-Time Events > Shura Battle.
- **Memory Usage**: The script has low memory usage and can run safely in the background.

## Contributing
We welcome contributions! Please submit Issues or Pull Requests to report bugs or suggest improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy gaming!