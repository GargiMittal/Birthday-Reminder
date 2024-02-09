# Birthday Reminder for Windows

This is a simple birthday reminder application built using Python for Windows. It utilizes the `win10toast` library to display toast notifications on Windows 10 whenever there are birthdays today.

## Features

- Allows users to save birthdays along with names in a text file (`file.txt`).
- Displays toast notifications on Windows 10 for birthdays occurring on the current day.

## Installation

1. Ensure you have Python installed on your Windows system. You can download Python from the official website: https://www.python.org/downloads/

2. Install the `win10toast` library using pip:
   ```pip install win10toast```

## Usage

1. Create a text file named `file.txt` where you'll store the birthdays. Each entry in the file should be in the format: "MonthDay Name Surname" (without quotes), e.g., "0101 John Doe".

2. Run the `reminder.py` script using Python. Ensure that the path to the `file.txt` is correctly set in the script.

3. The script will check for birthdays occurring today. If there are any birthdays, it will display toast notifications on Windows 10.

## Running the Application at Startup

To ensure that the birthday reminder application runs automatically at startup:

1. Press `Win + R` to open the Run dialog.
2. Type `shell:startup` and press Enter. This will open the Startup folder.
3. Copy the `reminder.py` script or create a shortcut to it in this folder.
4. make sure to add the path of `file.txt` to `reminder.py`.

Now, the script will run automatically every time you start your Windows system, and you'll receive birthday reminders via toast notifications.

## Requirements

- Python 3.x
- `win10toast` library

## future Work
Improve Tkinter design

## References
birthday reminder appilcation made for Ubuntu: https://www.geeksforgeeks.org/birthday-reminder-application-python/


