import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

# Set window title and theme
root.title("Dashboard")
style = ttk.Style(root)
style.theme_use('clam')  # You can change the theme if needed

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to fill the screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create frames for each quadrant
frame1 = tk.Frame(root, background="lightblue")
frame2 = tk.Frame(root, background="lightgreen")
frame3 = tk.Frame(root, background="lightcoral")
frame4 = tk.Frame(root, background="lightgoldenrodyellow")

# Place the header at the top
header = tk.Label(root, text="Dashboard", font=("Helvetica", 20))
header.pack(pady=1)

# Divide the window into quadrants
frame1.place(relx=0, rely=0.0, relwidth=0.5, relheight=0.5)
frame2.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.5)
frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
frame4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# Create content for each quadrant
label1 = tk.Label(frame1, text="Quadrant 1", font=("Helvetica", 12))
label1.pack(pady=10)

label2 = tk.Label(frame2, text="Quadrant 2", font=("Helvetica", 12))
label2.pack(pady=10)

label3 = tk.Label(frame3, text="Quadrant 3", font=("Helvetica", 12))
label3.pack(pady=10)

label4 = tk.Label(frame4, text="Quadrant 4", font=("Helvetica", 12))
label4.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
