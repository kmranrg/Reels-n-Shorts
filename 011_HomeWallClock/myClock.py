import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    # Calculate angles for clock hands
    second_angle = (seconds / 60) * 360
    minute_angle = ((minutes + seconds / 60) / 60) * 360
    hour_angle = ((hours % 12 + minutes / 60) / 12) * 360

    # Update clock hands
    canvas.delete("clock_hands")
    draw_hand(60, second_angle, 2, "red")
    draw_hand(50, minute_angle, 5, "black")
    draw_hand(30, hour_angle, 5, "black")

    # Update the clock every 1000 milliseconds (1 second)
    root.after(1000, update_clock)

def draw_hand(length, angle, width, color):
    radians = math.radians(90 - angle)
    x1 = 150  # Center X coordinate
    y1 = 150  # Center Y coordinate
    x2 = x1 + length * math.cos(radians)
    y2 = y1 - length * math.sin(radians)
    canvas.create_line(x1, y1, x2, y2, width=width, fill=color, tags="clock_hands")

root = tk.Tk()
root.title("Analog Wall Clock")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create clock face
canvas.create_oval(50, 50, 250, 250, outline="black", fill="white")

# Mark the hours 1 to 12
for hour in range(1, 13):
    angle = math.radians(90 - (hour * 30))  # Each hour is 30 degrees apart
    x = 150 + 80 * math.cos(angle)  # Position of the hour marker
    y = 150 - 80 * math.sin(angle)
    canvas.create_text(x, y, text=str(hour), fill="black", font=("Helvetica", 12, "bold"))

# Start the clock
update_clock()

root.mainloop()