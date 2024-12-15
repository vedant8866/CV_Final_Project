import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
import random

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

# Gesture function to control the paddles
def control_paddle(lst):
    fingers = count_fingers(lst)

    # Move paddle right with index finger
    if fingers == 1:
        return "move_right"

    # Move paddle left with index and middle fingers
    elif fingers == 2:
        return "move_left"

    # No movement
    return "none"

# Create the main application window using Tkinter
root = tk.Tk()
root.title("Pong Game")
root.geometry("800x600")  # Set the window size

# Create a canvas to represent the game area
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

# Draw the paddles and ball on the canvas
player_paddle = canvas.create_rectangle(250, 550, 350, 570, fill="blue")  # Player paddle
opponent_paddle = canvas.create_rectangle(250, 20, 350, 40, fill="green")  # Opponent paddle
ball = canvas.create_oval(290, 290, 310, 310, fill="red")  # Ball

ball_dx = 5  # Ball's horizontal speed
ball_dy = 5  # Ball's vertical speed
score = 0
game_over = False

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

        # Get the gesture and control the paddle accordingly
        gesture = control_paddle(hand_keyPoints)

        # Update paddle position based on gesture
        if gesture == "move_right":
            canvas.move(player_paddle, 20, 0)  # Move paddle right
        elif gesture == "move_left":
            canvas.move(player_paddle, -20, 0)  # Move paddle left

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

# Ball movement function
def move_ball():
    global ball_dx, ball_dy, score, game_over

    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)

    # Ball collision with top or bottom walls
    if ball_pos[1] <= 0 or ball_pos[3] >= 600:
        ball_dy *= -1

    # Ball collision with paddles
    if check_ball_collision_with_paddle():
        ball_dx *= -1  # Change direction

    # Ball out of bounds (score loss)
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        score -= 1
        reset_ball()

    # Update score and check game over
    if score <= -5:
        game_over = True
        canvas.create_text(400, 300, text="Game Over", font=("Arial", 24), fill="black")

    canvas.after(30, move_ball)

# Ball reset function
def reset_ball():
    global ball_dx, ball_dy

    canvas.coords(ball, 290, 290, 310, 310)
    ball_dx = 5 * random.choice([1, -1])
    ball_dy = 5 * random.choice([1, -1])

# Check for ball collision with paddles
def check_ball_collision_with_paddle():
    ball_pos = canvas.coords(ball)
    player_paddle_pos = canvas.coords(player_paddle)
    opponent_paddle_pos = canvas.coords(opponent_paddle)

    # Check collision with the player paddle
    if ball_pos[2] >= player_paddle_pos[0] and ball_pos[0] <= player_paddle_pos[2] and \
       ball_pos[3] >= player_paddle_pos[1] and ball_pos[1] <= player_paddle_pos[3]:
        return True

    # Check collision with the opponent paddle
    if ball_pos[2] >= opponent_paddle_pos[0] and ball_pos[0] <= opponent_paddle_pos[2] and \
       ball_pos[1] <= opponent_paddle_pos[3] and ball_pos[3] >= opponent_paddle_pos[1]:
        return True

    return False

# Start the game
update_frame()
move_ball()

# Start the Tkinter main loop
root.mainloop()

cap.release()
cv2.destroyAllWindows()
