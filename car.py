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

# Gesture function to control the car movement
def control_car(lst):
    fingers = count_fingers(lst)

    # Accelerate with index finger
    if fingers == 1:
        return "accelerate"

    # Turn right with index and middle fingers
    elif fingers == 2:
        return "turn_right"

    # Turn left with index, middle, and ring fingers
    elif fingers == 3:
        return "turn_left"

    # Move backward with index, middle, ring, and pinky fingers
    elif fingers == 4:
        return "move_backward"

    # Stop the car with all five fingers
    elif fingers == 5:
        return "stop"

    return "none"

# Create the main application window using Tkinter
root = tk.Tk()
root.title("Hand Gesture Car Game")
root.geometry("800x600")  # Set the window size

# Create a canvas to represent the car and game area
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

# Draw the car on the canvas
car = canvas.create_rectangle(350, 500, 450, 550, fill="red")

# Function to update the car's position based on gestures
def update_car_position(gesture):
    if gesture == "accelerate":
        canvas.move(car, 0, -10)  # Move car up
    elif gesture == "turn_right":
        canvas.move(car, 10, 0)  # Move car right while accelerating
    elif gesture == "turn_left":
        canvas.move(car, -10, 0)  # Move car left while accelerating
    elif gesture == "move_backward":
        canvas.move(car, 0, 10)  # Move car down (backward)
    elif gesture == "stop":
        # No movement (car stops)
        pass

# Setup MediaPipe for hand gesture detection
cap = cv2.VideoCapture(0)
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

# Function to update the camera feed in the Tkinter window
def update_frame():
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)  # Flip the frame horizontally

    # Process the frame for hand landmarks
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]

        # Get the gesture and control the car accordingly
        gesture = control_car(hand_keyPoints)
        update_car_position(gesture)

        # Draw the hand landmarks on the frame
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    # Convert the frame to a format that Tkinter can display (BGR -> RGB)
    img = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter
    img_pil = Image.fromarray(img)  # Convert to PIL image
    imgtk = ImageTk.PhotoImage(image=img_pil)

    # Update the camera feed in the Tkinter window
    label_img.imgtk = imgtk
    label_img.configure(image=imgtk)

    # Keep updating the frame every 10 milliseconds
    label_img.after(10, update_frame)

# Create a label in the Tkinter window to display the camera feed
label_img = tk.Label(root)
label_img.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Start updating the camera feed
update_frame()

# Start the Tkinter main loop
root.mainloop()

cap.release()
cv2.destroyAllWindows()
