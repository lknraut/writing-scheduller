import datetime

def get_starting_page(start_date, input_date, daily_pages):
    starting_page = 1
    days_diff = (input_date - start_date).days

    if days_diff < 0:
        return None  # Return None if the input date is before the start date

    starting_page += (days_diff * daily_pages)
    return starting_page

while True:
    start_date_str = input("Enter the start date (dd mm yyyy), or enter 'q' to quit: ")
    if start_date_str == 'q':
        break
    input_date_str = input("Enter the input date (dd mm yyyy): ")
    daily_pages = int(input("Enter the number of pages you can write each day: "))
    start_date = datetime.datetime.strptime(start_date_str, "%d %m %Y").date()
    input_date = datetime.datetime.strptime(input_date_str, "%d %m %Y").date()
    starting_page = get_starting_page(start_date, input_date, daily_pages)
    if starting_page is None:
        print("Error: Input date is before the start date.")
    else:
        print(f"You will start on page {starting_page} on {input_date}.")
