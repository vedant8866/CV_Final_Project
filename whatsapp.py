import cv2
import mediapipe as mp
import pyautogui
import time
import pywhatkit as kit
import tkinter as tk
from threading import Thread
from tkinter import messagebox

# Gesture functions
def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2
    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:  # Index finger
        cnt += 1
    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:  # Middle finger
        cnt += 1
    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:  # Ring finger
        cnt += 1
    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:  # Pinky finger
        cnt += 1
    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:  # Thumb
        cnt += 1
    return cnt

def well_done(lst):
    thumb_up = (lst.landmark[4].y < lst.landmark[3].y < lst.landmark[2].y)
    pinky_up = (lst.landmark[20].y < lst.landmark[19].y)
    all_other_fingers_down = all(lst.landmark[tip].y > lst.landmark[base].y
                                 for tip, base in [(8, 6), (12, 10), (16, 14)])
    return thumb_up and pinky_up and all_other_fingers_down

# Detection thread
def gesture_detection():
    cap = cv2.VideoCapture(0)
    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=1)

    start_init = False
    prev = -1

    while running:
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)
        res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:
            hand_keyPoints = res.multi_hand_landmarks[0]
            if well_done(hand_keyPoints):
                kit.sendwhatmsg_instantly("+918468813811", "Hii, how are you doing?", 10)
                time.sleep(3)

            cnt = count_fingers(hand_keyPoints)
            if cnt != prev:
                if cnt == 1:
                    pyautogui.press("right")
                elif cnt == 2:
                    pyautogui.press("left")
                elif cnt == 3:
                    pyautogui.press("up")
                elif cnt == 4:
                    pyautogui.press("down")
                elif cnt == 5:
                    pyautogui.press("space")
                prev = cnt
            drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

        cv2.imshow("Gesture Detection", frm)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Start and stop control
def start_detection():
    global running, detection_thread
    running = True
    detection_thread = Thread(target=gesture_detection)
    detection_thread.start()
    messagebox.showinfo("Info", "Gesture Detection Started!")

def stop_detection():
    global running
    running = False
    detection_thread.join()
    messagebox.showinfo("Info", "Gesture Detection Stopped!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Gesture Detection App")
root.geometry("400x200")

running = False
detection_thread = None

tk.Label(root, text="Hand Gesture Detection", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Start Detection", command=start_detection, bg="green", fg="white", width=20).pack(pady=10)
tk.Button(root, text="Stop Detection", command=stop_detection, bg="red", fg="white", width=20).pack(pady=10)

root.mainloop()
