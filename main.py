import tkinter as tk
import requests
import json
from tkinter import ttk

# Stock ticker api key Alpha Vantage
api_key = 'Q4T92EGO527AR75C'

# Create the main window
root = tk.Tk()

# Set window title and theme
root.title("Dashboard")
style = ttk.Style(root)
style.theme_use('classic')  # You can change the theme if needed

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to fill the screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create frames for each quadrant
frame1 = tk.Frame(root, background="darkturquoise")
frame2 = tk.Frame(root, background="darkturquoise")
frame3 = tk.Frame(root, background="darkturquoise")
frame4 = tk.Frame(root, background="darkturquoise")

# Place the header at the top
header = tk.Label(root, text="Dashboard", font=("Helvetica", 20))
header.pack(pady=1)

# Divide the window into quadrants
frame1.place(relx=0, rely=0.0, relwidth=0.5, relheight=0.5)
frame2.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.5)
frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
frame4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# # Create content for each quadrant
label1 = tk.Label(frame1, text="Stock Ticker", font=("Helvetica", 12))
label1.pack(pady=10)

def stock_ticker():
    symbol = 'WWD'

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=WWD&interval=5min&apikey=Q4T92EGO527AR75C'
    
    try:
        r = requests.get(url)
        data = r.json()
        latest_timestamp = max(data['Time Series (5min)'], key=lambda x: x)
        stock_price = data['Time Series (5min)'][latest_timestamp]['4. close']

        label1.config(text=f"Stock Ticker: {symbol} - Latest Price: {stock_price}")

    except Exception as e:
        label1.config(text=f"Error fetching data: {str(e)}")

    label1.after(3600000, stock_ticker)

stock_ticker()


label2 = tk.Label(frame2, text="Bulls Record", font=("Helvetica", 12))
label2.pack(pady=10)

def bulls_record():
    nba_endpoint = 'https://www.balldontlie.io/api/v1/teams'
    bulls_id = 5
    url1 = f'{nba_endpoint}/{bulls_id}'
    response = requests.get(url1)

    try:
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract relevant information (e.g., win and loss records)
        full_name = data['full_name']

        label2.config(text=f"Team: {full_name}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

    label2.after(3600000, bulls_record)

# Call the function to get and print the Bulls' record
bulls_record()



label3 = tk.Label(frame3, text="Quadrant 3", font=("Helvetica", 12))
label3.pack(pady=10)

label4 = tk.Label(frame4, text="Quadrant 4", font=("Helvetica", 12))
label4.pack(pady=10)


# Run the Tkinter event loop
root.mainloop()
