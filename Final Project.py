import tkinter as tk
from tkinter import messagebox

# Mock weather data
mock_weather_data = [
    {"name": "New York", "main": {"temp": 22}, "weather": [{"description": "clear sky"}]},
    {"name": "Los Angeles", "main": {"temp": 28}, "weather": [{"description": "sunny"}]},
    {"name": "Chicago", "main": {"temp": 15}, "weather": [{"description": "partly cloudy"}]},
    {"name": "Houston", "main": {"temp": 30}, "weather": [{"description": "hot"}]},
    {"name": "Phoenix", "main": {"temp": 35}, "weather": [{"description": "very hot"}]},
    {"name": "Philadelphia", "main": {"temp": 18}, "weather": [{"description": "cool"}]},
    {"name": "San Antonio", "main": {"temp": 25}, "weather": [{"description": "clear sky"}]},
    {"name": "San Diego", "main": {"temp": 24}, "weather": [{"description": "mild"}]},
    {"name": "Dallas", "main": {"temp": 27}, "weather": [{"description": "warm"}]},
    {"name": "San Jose", "main": {"temp": 20}, "weather": [{"description": "foggy"}]}
]

def fetch_weather(location):
    weather_data = next((city for city in mock_weather_data if city['name'].lower() == location.lower()), None)
    return weather_data

def display_weather():
    location = location_entry.get()
    weather = fetch_weather(location)
    if weather:
        result_label.config(text=f"Weather in {weather['name']}:\nTemperature: {weather['main']['temp']}°C\nDescription: {weather['weather'][0]['description']}")
    else:
        result_label.config(text="Location not found in mock data.")

def on_enter(e):
    fetch_button.config(bg="#218838")  # Darker green on hover

def on_leave(e):
    fetch_button.config(bg="#28a745")  # Original green

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#f0f4f8")

# Create a header frame
header_frame = tk.Frame(root, bg="#007bff", bd=5)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Weather Information", font=("Helvetica", 16), bg="#007bff", fg="white")
header_label.pack(pady=10)

# Create and place the widgets
location_label = tk.Label(root, text="Enter location:", font=("Helvetica", 12), bg="#f0f4f8")
location_label.pack(pady=5)

location_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
location_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Weather", command=display_weather, font=("Helvetica", 12), bg="#28a745", fg="white", relief=tk.GROOVE)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f4f8")
result_label.pack(pady=10)

# Bind hover events
fetch_button.bind("<Enter>", on_enter)
fetch_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f4f8")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()