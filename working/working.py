import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(time):
    try:
        start_time, end_time = time.split(" to ")
    except ValueError:
        raise ValueError("Invalid Input")

    if "AM" in start_time:
        try:
            Time, Meridian = start_time.split(" ")
        except ValueError:
            raise ValueError()
        if ":" in Time:
            hour, minutes = Time.split(":")
            if int(minutes) > 59:
                raise ValueError("Invalid Input")
            elif hour == "12":
                hour = "00"
        elif Time == "12":
            hour = "00"
            minutes = "00"
        else:
            hour = Time
            minutes = "00"

    elif "PM" in start_time:
        try:
            Time, Meridian = start_time.split(" ")
        except ValueError:
            raise ValueError("Invalid Input")
        if ":" in Time:
            hour, minutes = Time.split(":")
            hour = int(hour)
            if hour > 12:
                raise ValueError("Invalid Input")
            else:
                hour += 12
            if int(minutes) > 59:
                raise ValueError("Invalid Input")
        else:
            hour = int(Time)
            if hour > 12:
                raise ValueError("Invalid Input")
            else:
                hour += 12
            minutes = "00"
    else:
        raise ValueError("Invalid Input")

    if "AM" in end_time:
        try:
            eTime, eMeridian = end_time.split(" ")
        except ValueError:
            raise ValueError()
        if ":" in eTime:
            ehour, eminutes = eTime.split(":")
            if int(minutes) > 59:
                raise ValueError("Invalid Input")
        elif eTime == "12":
            ehour = "00"
        else:
            ehour = eTime
            eminutes = "00"

    elif "PM" in end_time:
        try:
            eTime, eMeridian = end_time.split(" ")
        except ValueError:
            raise ValueError("Invalid Input")
        if ":" in eTime:
            ehour, eminutes = eTime.split(":")
            if len(eminutes) > 2:
                raise ValueError("Invalid Input")
            ehour = int(ehour)
            if ehour > 12:
                raise ValueError("Invalid Input")
            elif ehour == 12:
                ehour == "12"
            else:
                ehour += 12
        else:
            ehour = int(eTime)
            if ehour > 12:
                raise ValueError("Invalid Input")
            elif ehour == 12:
                ehour = 12
                eminutes = "00"
            else:
                ehour += 12
            eminutes = "00"
    else:
        raise ValueError("Invalid Input")


    return f"{int(hour):02}:{minutes} to {int(ehour):02}:{eminutes}"





if __name__ == "__main__":
    main()
