import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
from datetime import datetime
import os


DAYS_IN_MONTH = {
    "01": 31,
    "02": 29,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30 ,
    "12": 31,
}

    
def increment_day(date):
    global DAYS_IN_MONTH
    new_day = int(date[-2:]) + 1
    new_month = int(date[-5:-3])
    new_year = int(date[0:4])
    
    if new_month > 9:
        day_limit = DAYS_IN_MONTH[str(new_month)]
    else:
        day_limit = DAYS_IN_MONTH[f"0{new_month}"]

    
    if new_day > day_limit:
        new_day = "01"
        new_month += 1
    else:
        if new_day < 10:
            new_day = f"0{new_day}"
        
    if new_month > 12:
        new_month = "01"
        new_year += 1
    else:
        if new_month < 10:
            new_month = f"0{new_month}"
            
    return f"{new_year}-{new_month}-{new_day}"


def skip_num_of_days(startingDate, daysToSkip):
    for i in range(int(daysToSkip)):
        startingDate = increment_day(startingDate)
    return startingDate

    
def plot_data(prices, dates, start,finish,from_dest, to_dest): 
    data = [{'DATE': date, 'PRICE': price} for date, price in zip(dates, prices)]

    # Convert date strings to datetime objects
    date_objects = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(date_objects, prices, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Price (in dollars)')
    plt.title(f'{from_dest} to {to_dest}  {start} ~ {finish}')

    # Format the X-axis to show dates in the "2023-10-26" format
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    
    # Set the X-axis ticks to display only the actual dates
    plt.xticks(date_objects, [date.strftime('%Y-%m-%d') for date in date_objects], rotation=45)
    # plt.yticks(prices, rotation=45)
    
    for i, price in enumerate(prices):
        plt.annotate(f'{price}', (date_objects[i], price), textcoords="offset points", xytext=(0, 10), ha='center')

    
    file_name = f'{from_dest} to {to_dest} {start} {finish}.png'
    count = 0
    while os.path.exists(file_name):
        count += 1
        file_name = f'{from_dest} to {to_dest} {start} {finish} ({count}).png'
    # Save the plot as an image file (e.g., PNG)
    plt.savefig(file_name, bbox_inches='tight')


def open_driver(driver, url):
    # Open the URL in the browser
    driver.get(url)
    
    timeout = 30
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "_filter_1jexs_1")))  
    # time.sleep(5)

def fetch(url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # Enable headless mode
    driver = webdriver.Firefox(options=options)
    
    print("Fetching...")
    while True:
        try:
            open_driver(driver, url)
            test = driver.find_elements(By.CSS_SELECTOR, "div._filter_1jexs_1")[-2]
            a = test.find_element(By.CSS_SELECTOR, "span._label_6io4k_32._label__right_6io4k_55")
            price = a.get_attribute("innerHTML")
            price = price[price.index("$")+1:].strip()
            
            # Double the price to account for 2 passengers
            price = str(int(price) * 2)
            
            # Close the WebDriver when done
            driver.quit()
            break
        except:
            print("Trying again...")
            time.sleep(1)
        
    return price  

def calculate_date_difference(date_str1, date_str2):
    # Convert date strings to datetime objects
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")

    # Calculate the difference in days
    difference = (date2 - date1).days

    return difference + 1

def make_url(dates_start, dates_finish, start_dest, end_dest):
    # Their url always shows directFlightsOnly as false, irregardless if it's true
    url_base = "https://www.travelist.co.il/flightsResults?directFlightsOnly=false&"
    url_ending = "adults=2&infants=0&children=0&seniors=0"
    
    url_dates =  f"singleDate={dates_start}&"    
    url_dests = f"from={start_dest}&to={end_dest}&"
    url_final = url_base + url_dates + url_dests + url_ending
    
    return url_final


def run_in_range(DATES_START, DATES_FINISH, FROM, TO, DELAY):
    # Start Timer
    start = time.time()
    print("Starting...")
    
    new_date = DATES_START
    url = make_url(DATES_START, DATES_FINISH, FROM, TO)

    prices = list()
    dates = list()
        
    difference = calculate_date_difference(DATES_START, DATES_FINISH)
    
    
    for i in range(difference):
        print(f"\nCycle {i+1}:\nurl = {url}\nDate = {new_date}\n")
        prices.append(int(fetch(url)))  
        dates.append(new_date)
        new_date = increment_day(new_date)
        url = make_url(new_date, DATES_FINISH, FROM, TO)
    
    plot_data(prices, dates, DATES_START, DATES_FINISH, FROM, TO)
    
    # End Timer
    end = time.time()
    print(f"Time: {end - start} seconds")
    
    return

def run_script():
    # Get the values from the input fields
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    from_location = from_location_entry.get()
    to_location = to_location_entry.get()
    delay = delay_entry.get()  # Get the delay value
        
    run_in_range(DATES_START = start_date, DATES_FINISH = end_date, FROM = from_location, TO = to_location, DELAY = delay)
    
    if int(delay) > 0:
        start_date = skip_num_of_days(start_date, delay)
        end_date = skip_num_of_days(end_date, delay)
        run_in_range(DATES_START=start_date, DATES_FINISH=end_date, FROM = to_location, TO = from_location, DELAY = delay)
    
    print("Finished")


# Create the main application window
root = tk.Tk()
root.title("Flight Price Checker")
root.geometry("250x250")  # Adjust the size as needed


start_date_label = ttk.Label(root, text="Start Date:")
start_date_entry = ttk.Entry(root, justify="center")
# today_date = datetime.now().strftime("%Y-%m-%d")
start_date_entry.insert(0, "2024-05-09")  # Set a default value


end_date_label = ttk.Label(root, text="End Date:")
end_date_entry = ttk.Entry(root, justify="center")
end_date_entry.insert(0, "2024-05-31")  # Set a default value

delay_label = ttk.Label(root, text="Delay (in days):")
delay_entry = ttk.Entry(root, justify="center")
delay_entry.insert(0, 7)


from_location_label = ttk.Label(root, text="From Location:")
from_location_entry = ttk.Entry(root, justify="center")
from_location_entry.insert(0, "TLV")

to_location_label = ttk.Label(root, text="To Location:")
to_location_entry = ttk.Entry(root, justify="center")
to_location_entry.insert(0, "VIE")



run_button = ttk.Button(root, text="Run Script", command=run_script)

# Arrange the widgets using grid layout with column and row weights
root.columnconfigure(0, weight=1)  # Make the left column expand
root.columnconfigure(1, weight=1)  # Make the right column expand
root.rowconfigure(5, weight=1)     # Make the last row expand

start_date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
start_date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

end_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
end_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

delay_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
delay_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

from_location_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
from_location_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

to_location_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
to_location_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

run_button.grid(row=5, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()    

    
   

	
    
   
 

    


