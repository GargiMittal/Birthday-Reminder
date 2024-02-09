# Python program For
# Birthday Reminder Application

# time module is must as reminder
# is set with the help of dates
import time

# Birthday file is the one in which the actual birthdays
# and dates are present. This file can be
# manually edited or can be automated.
# For simplicity, we will edit it manually.
# Birthdays should be written in this file in
# the format: "MonthDay Name Surname" (Without Quotes)

birthdayFile = "path to /file.txt"

def checkTodaysBirthdays():
    today = time.strftime('%m%d')
    flag = 0
    with open(birthdayFile, 'r') as f:
        for line in f:
            if today in line:
                line = line.split(' ')
                flag = 1
                # line[1] contains Name and line[2] contains Surname
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Birthdays Today:", line[1], duration=10)
    if flag == 0:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("No Birthdays Today!")

if __name__ == '__main__':
    checkTodaysBirthdays()
