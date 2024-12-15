import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk

# Gesture function to count fingers
def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:  # Index finger
        cnt += 1
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:  # Middle finger
        cnt += 1
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:  # Ring finger
        cnt += 1
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:  # Pinky finger
        cnt += 1
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:  # Thumb
        cnt += 1
    return cnt

# Gesture function to detect if all fingers are up (turn light ON)
def all_fingers_up(lst):
    return count_fingers(lst) == 5

# Gesture function to detect if all fingers are down (turn light OFF)
def all_fingers_down(lst):
    return count_fingers(lst) == 0

# Create the main application window using Tkinter
root = tk.Tk()
root.title("Virtual Light Control")
root.geometry("800x400")  # Set size of the window to accommodate both

# Create two frames: one for the camera feed and one for the light control
frame1 = tk.Frame(root, width=400, height=400)
frame1.grid(row=0, column=0)
frame2 = tk.Frame(root, width=400, height=400)
frame2.grid(row=0, column=1)

# Create a canvas for displaying the virtual light
canvas = tk.Canvas(frame2, width=300, height=300, bg="white")
canvas.pack()

# Draw the virtual light (circle) and set its initial color to red
light = canvas.create_oval(100, 100, 200, 200, fill="red", outline="red")

# Function to change the light color based on the gesture
def change_light_color(state):
    if state == "on":
        canvas.itemconfig(light, fill="green")  # Light ON (green)
    elif state == "off":
        canvas.itemconfig(light, fill="red")  # Light OFF (red)

# Setup MediaPipe for hand gesture detection
cap = cv2.VideoCapture(0)
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

# Function to update the camera feed in the Tkinter window
def update_frame():
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)  # Flip frame horizontally

    # Process the frame for hand landmarks
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]

        # Detect the gesture and change the light color accordingly
        if all_fingers_up(hand_keyPoints):
            change_light_color("on")  # Turn light ON (green)
        elif all_fingers_down(hand_keyPoints):
            change_light_color("off")  # Turn light OFF (red)

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    # Convert the frame to a format that Tkinter can display (BGR -> RGB)
    img = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter
    img_pil = Image.fromarray(img)  # Convert to PIL image
    imgtk = ImageTk.PhotoImage(image=img_pil)

    # Update the canvas with the new image
    label_img.imgtk = imgtk
    label_img.configure(image=imgtk)

    # Keep updating the frame every 10 milliseconds
    label_img.after(10, update_frame)

# Create a label in frame1 to hold the camera feed
label_img = tk.Label(frame1)
label_img.pack(fill=tk.BOTH, expand=True)

# Start updating the camera feed
update_frame()

# Start the Tkinter main loop
root.mainloop()

cap.release()
cv2.destroyAllWindows()