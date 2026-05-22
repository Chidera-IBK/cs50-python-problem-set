def main():
    time = input("What time is it? ").strip()
    time_in_hours = convert(time)

    if 7 <= time_in_hours <= 8:
        print("Breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("Lunch time")
    elif 18 <= time_in_hours <= 19:
        print("Dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60

if __name__ == "__main__":
    main()
