import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def calculate_pages():
    # Get the user input from the GUI
    start_date = start_cal.get_date()
    end_date = end_cal.get_date()
    schedule = int(schedule_entry.get())

    # Calculate the number of days between start and end dates
    num_days = (end_date - start_date).days + 1

    # Loop through each day and calculate expected page number
    for i in range(num_days):
        # Calculate page number for front and back pages
        front_page = i * 2 + 1
        back_page = i * 2 + 2

        # Calculate page number for third page (back)
        if i % 3 == 2:
            third_page = back_page
        else:
            third_page = back_page - 1

        # Calculate the date for the current day
        current_date = start_date + datetime.timedelta(days=i)

        # Calculate the expected page number for the current day
        if current_date.weekday() < 5:
            expected_page = front_page
        else:
            expected_page = third_page

        # Display the expected page number for the current day in the GUI
        output_text.insert(tk.END, f"Date: {current_date.strftime('%d/%m/%Y')}, Expected Page: {expected_page}\n")

# Create the GUI
root = tk.Tk()
root.title("Writing Scheduler")

# Create a frame for the date selection widgets
date_frame = ttk.Frame(root, padding=10)
date_frame.pack()

# Create a DateEntry widget for the start date
start_label = ttk.Label(date_frame, text="Start Date:")
start_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
start_cal = DateEntry(date_frame, width=12, background="darkblue", foreground="white", date_pattern="dd/MM/yyyy")
start_cal.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Create a DateEntry widget for the end date
end_label = ttk.Label(date_frame, text="End Date:")
end_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
end_cal = DateEntry(date_frame, width=12, background="darkblue", foreground="white", date_pattern="dd/MM/yyyy")
end_cal.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Create a label and entry widget for the writing schedule
schedule_label = ttk.Label(root, text="Writing Schedule (in pages per day):")
schedule_label.pack(pady=5)
schedule_entry = ttk.Entry(root)
schedule_entry.pack()

# Create a button to calculate the expected page numbers
calculate_button = ttk.Button(root, text="Calculate Pages", command=calculate_pages)
calculate_button.pack(pady=5)

# Create a text widget to display the expected page numbers
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=5)

# Start the GUI main loop
root.mainloop()
