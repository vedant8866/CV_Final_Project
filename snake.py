import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
import random

# Snake Game Logic
class SnakeGame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake body
        self.direction = "Right"
        self.food = self.random_food()
        self.score = 0
        self.game_over = False
        self.snake_speed = 100
        self.update_snake()

    def random_food(self):
        return (random.randint(0, 19) * 20, random.randint(0, 19) * 20)

    def update_snake(self):
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Right":
            head_x += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20

        # Insert new head
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

        # Check if snake eats food
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])  # Add a new body segment
            self.food = self.random_food()  # Generate new food
            self.score += 1
            self.snake_speed -= 5  # Increase speed as score increases

    def check_game_over(self):
        head = self.snake[0]
        # Check if snake hits the wall or itself
        if head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 600 or head in self.snake[1:]:
            self.game_over = True
            self.canvas.create_text(300, 300, text="Game Over! Press Thumbs Up to Restart", font=("Arial", 14), fill="red")

    def draw_food(self):
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")

    def update_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_game_over()
            self.canvas.delete("all")
            self.update_snake()
            self.draw_food()
            self.canvas.create_text(300, 20, text=f"Score: {self.score}", font=("Arial", 14), fill="black")
            if not self.game_over:
                self.canvas.after(self.snake_speed, self.update_game)  # Game update rate

    def restart_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Reset snake
        self.direction = "Right"
        self.food = self.random_food()
        self.score = 0
        self.game_over = False
        self.snake_speed = 100
        self.update_game()

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

# Gesture function to control snake movement
def control_snake(lst):
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

    # Stop the snake with all five fingers
    elif fingers == 5:
        return "stop"

    return "none"

# Create the main application window using Tkinter
root = tk.Tk()
root.title("Gesture-Controlled Snake Game")
root.geometry("800x600")  # Set the window size

# Create a canvas to represent the game area
canvas = tk.Canvas(root, width=600, height=600, bg="lightblue")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Initialize SnakeGame instance
game = SnakeGame(canvas)

# Create a label for face and hand gesture window
label_img = tk.Label(root, width=200, height=200)
label_img.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

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

        # Get the gesture and control the snake accordingly
        gesture = control_snake(hand_keyPoints)

        if gesture == "accelerate":
            game.direction = "Right"
        elif gesture == "turn_right":
            game.direction = "Down"
        elif gesture == "turn_left":
            game.direction = "Up"
        elif gesture == "move_backward":
            game.direction = "Left"
        elif gesture == "stop":
            game.game_over = True  # End the game when all fingers are shown

        # Update the game
        game.update_game()

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

# Start updating the camera feed
update_frame()

# Start the Tkinter main loop
root.mainloop()

cap.release()
cv2.destroyAllWindows()
