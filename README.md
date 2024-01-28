# Prank Application

This is a simple prank application that rotates the screen and plays a sound while displaying an image using tkinter and Pygame libraries.

## Features

- Rotates the screen orientation multiple times.
- Plays a sound.
- Displays an image using tkinter.
- Supports custom images and sounds.

## Requirements

- Python 3.7 and above
- tkinter
- PIL (Python Imaging Library)
- Pygame
- rotatescreen

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/MuhammadRaffey/Screen-Rotation-Prank.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main.py` script:

    ```
    python main.py
    ```

2. Sit back and enjoy the prank!

## Customization

- You can replace the image and sound files in the `assets` directory with your own files.
- Modify the `rotate_screen` method to change the number of screen rotations or the delay between rotations.
- Customize the GUI layout and design by editing the `prank` method in the `Prank` class.


## Creating an Executable (Optional)

1. Install PyInstaller:

    ```
    pip install pyinstaller
    ```

2. Generate an executable:

    ```
    pyinstaller --onefile --noconsole --add-data "assets;assets" main.py
    ```

    This command will create a standalone executable file in the `dist` directory. The `--onefile` option packages everything into a single executable, `--noconsole` hides the command prompt window, and `--add-data` includes the assets directory.

3. Locate and run the executable:

    The executable file will be located in the `dist` directory. You can run it directly to execute the prank application without needing to run Python or install any dependencies.

## Contributing

Contributions are welcome! If you have any ideas for improvement or encounter any issues, feel free to open an issue or submit a pull request.

