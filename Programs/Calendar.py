def print_calendar(year):
    for month in range(1, 13):
        # Display the month and year
        print(calendar.month_name[month], year)
        print("-----------------------------")
        
        # Display the calendar for the month
        cal = calendar.monthcalendar(year, month)
        print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")
        for week in cal:
            for day in week:
                if day == 0:
                    print("\t", end="")
                else:
                    print(f"{day:2}", end="\t")
            print()

        print()
def calendardate():
    if __name__ == "__main__":
        try:
            year = int(input("Enter the year for the calendar: "))
            print_calendar(year)
        except ValueError:
            print("Invalid input. Please enter a valid year.")
