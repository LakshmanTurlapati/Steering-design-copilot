import tkinter as tk
from tkinter import Label, Entry, Button
import steering_copilot 

def calculate_button_clicked():
    try:
        wheelbase = float(wheelbase_entry.get())
        track = float(track_entry.get())
        turn_radius = float(turn_radius_entry.get())
        
        # Call the calculate_ackerman_angle function from calculations.py
        inner_angle, outer_angle = steering_copilot.calculate_ackerman_angle(wheelbase, track, turn_radius)
        
        inner_angle_label.config(text=f"Inner Wheel Angle: {inner_angle:.2f} degrees")
        outer_angle_label.config(text=f"Outer Wheel Angle: {outer_angle:.2f} degrees")
    except ValueError:
        inner_angle_label.config(text="Invalid input. Please enter numeric values.")

# Create the main application window
app = tk.Tk()
app.title("Ackerman Angle Calculator")

# Create labels, entry fields, and a calculate button
wheelbase_label = Label(app, text="Wheelbase (m):")
wheelbase_label.pack()
wheelbase_entry = Entry(app)
wheelbase_entry.pack()

track_label = Label(app, text="Track (m):")
track_label.pack()
track_entry = Entry(app)
track_entry.pack()

turn_radius_label = Label(app, text="Turn Radius (m):")
turn_radius_label.pack()
turn_radius_entry = Entry(app)
turn_radius_entry.pack()

calculate_button = Button(app, text="Calculate", command=calculate_button_clicked)
calculate_button.pack()

inner_angle_label = Label(app, text="")
inner_angle_label.pack()

outer_angle_label = Label(app, text="")
outer_angle_label.pack()

# Start the GUI application
app.mainloop()
