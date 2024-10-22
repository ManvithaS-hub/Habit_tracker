import requests
from tkinter import *
from datetime import datetime
import webbrowser  # To open the Pixela graph page

# Constants
BACKGROUND_COLOR = "#f7f5dd"
BUTTON_COLOR = "#ffcc00"
HOVER_COLOR = "#ffdd44"
TEXT_COLOR = "#4d4d4d"
USERNAME = "manvitha"
TOKEN = "abcfeddefcba"
pixela_endpoint = "https://pixe.la/v1/users"


# Function to submit coding hours and open Pixela graph
def submit_hours():
    hours = no_hours.get()
    today = datetime.now()
    parms = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    # response=requests.post("https://pixe.la/v1/users",json=parms)
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "hours",
        "type": "float",
        "color": "ichou"
    }
    # response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
    # print(response.text)

    # Endpoint and payload for Pixela
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": hours,
    }
    headers = {"X-USER-TOKEN": TOKEN}

    # Submit the hours
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

    # Check if submission was successful
    if response.status_code == 200:
        print("Coding hours submitted successfully.")
        # Open the Pixela graph page after submission
        graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1.html"
        webbrowser.open(graph_url)  # Opens the Pixela graph in the default browser
    else:
        print(f"Error: {response.text}")


# Hover effect for buttons
def on_enter(e):
    submit.config(bg=HOVER_COLOR)


def on_leave(e):
    submit.config(bg=BUTTON_COLOR)


# GUI Setup
window = Tk()
window.title("Habit Tracker")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Canvas for the main content
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="card_front.png")  # Load background image if needed
canvas_image = canvas.create_image(400, 263, image=image)
canvas.grid(row=0, column=0, columnspan=2)

# Add a title text on the canvas
title = canvas.create_text(
    400, 100,
    text="Track Your Coding Hours",
    font=("Helvetica", 28, "bold"),
    fill=TEXT_COLOR
)

# Add a text label on the canvas
text = canvas.create_text(
    400, 180,
    text="How many hours did you code today?",
    width=500,
    font=("Helvetica", 20, "italic"),
    fill=TEXT_COLOR
)

# Entry for coding hours
no_hours = Entry(window, font=("Helvetica", 16), width=10, justify='center', bd=2)
canvas.create_window(400, 240, window=no_hours)

# Submit button
submit = Button(
    text="Submit",
    command=submit_hours,
    font=("Helvetica", 16, "bold"),
    bg=BUTTON_COLOR,
    fg="black",
    relief="raised",
    bd=3,
    padx=10,
    pady=5,
    activebackground=HOVER_COLOR
)
canvas.create_window(400, 300, window=submit)

# Bind hover effects to the button
submit.bind("<Enter>", on_enter)
submit.bind("<Leave>", on_leave)

# Run the application
window.mainloop()
