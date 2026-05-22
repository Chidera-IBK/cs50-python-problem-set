months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    try:
        date = input("Date: ").strip()
        if date[0].isdigit():
            month, day, year = date.split("/")

            if  1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                month = month.zfill(2)
                day = day.zfill(2)

                print(f"{year}-{month}-{day}")
                break


        elif date[0].isalpha():
            begin, year = date.split(",")
            month, day = begin.strip().split(" ")

            if month in months and 1 <= int(day) <= 31:
                month_num = months[month].zfill(2)
                day_num = day.zfill(2)
                print(f"{year.strip()}-{month_num}-{day_num}")
                break
    except ValueError:
        continue
