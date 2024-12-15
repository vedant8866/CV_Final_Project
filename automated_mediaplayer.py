# import cv2 
# import mediapipe as mp
# import pyautogui
# import time

# def count_fingers(lst):
#     cnt = 0

#     thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

#     if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
#         cnt += 1


#     return cnt 

# cap = cv2.VideoCapture(0)

# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)


# start_init = False 

# prev = -1

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:

#         hand_keyPoints = res.multi_hand_landmarks[0]

#         cnt = count_fingers(hand_keyPoints)

#         if not(prev==cnt):
#             if not(start_init):
#                 start_time = time.time()
#                 start_init = True

#             elif (end_time-start_time) > 0.2:
#                 if (cnt == 1):
#                     pyautogui.press("right")
                
#                 elif (cnt == 2):
#                     pyautogui.press("left")

#                 elif (cnt == 3):
#                     pyautogui.press("up")

#                 elif (cnt == 4):
#                     pyautogui.press("down")

#                 elif (cnt == 5):
#                     pyautogui.press("space")

#                 prev = cnt
#                 start_init = False


        


#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     cv2.imshow("window", frm)

#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         cap.release()
#         break

################################################################################################

# import cv2 
# import mediapipe as mp
# import pyautogui
# import time

# def count_fingers(lst):
#     cnt = 0

#     thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

#     if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
#         cnt += 1


#     return cnt 

# cap = cv2.VideoCapture(0)

# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)


# start_init = False 

# prev = -1

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:

#         hand_keyPoints = res.multi_hand_landmarks[0]

#         cnt = count_fingers(hand_keyPoints)

#         if not(prev==cnt):
#             if not(start_init):
#                 start_time = time.time()
#                 start_init = True

#             elif (end_time-start_time) > 0.2:
#                 if (cnt == 1):
#                     pyautogui.press("right")
                
#                 elif (cnt == 2):
#                     pyautogui.press("left")

#                 elif (cnt == 3):
#                     pyautogui.press("up")

#                 elif (cnt == 4):
#                     pyautogui.press("down")

#                 elif (cnt == 5):
#                     pyautogui.press("space")

#                 prev = cnt
#                 start_init = False


        


#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     cv2.imshow("295", frm)

#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         cap.release()
#         break

# import cv2 
# import mediapipe as mp
# import pyautogui
# import time

# def count_fingers(lst):
#     cnt = 0
#     thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

#     if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
#         cnt += 1

#     return cnt 

# cap = cv2.VideoCapture(0)
# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)

# start_init = False 
# prev = -1

# # Dictionary to map finger counts to actions
# finger_action = {
#     1: "Going Right (1 Finger)",
#     2: "Going Left (2 Fingers)",
#     3: "Going Up (3 Fingers)",
#     4: "Going Down (4 Fingers)",
#     5: "Pause/Play (5 Fingers) थांबू नकोस "
# }

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     # Convert frame to RGB and process with MediaPipe hands
#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:
#         hand_keyPoints = res.multi_hand_landmarks[0]
#         cnt = count_fingers(hand_keyPoints)

#         # If the finger count changes, initialize the action
#         if not(prev == cnt):
#             if not start_init:
#                 start_time = time.time()
#                 start_init = True
#             elif (end_time - start_time) > 0.2:  # Debounce for 0.2 seconds
#                 if cnt == 1:
#                     pyautogui.press("right")
#                 elif cnt == 2:
#                     pyautogui.press("left")
#                 elif cnt == 3:
#                     pyautogui.press("up")
#                 elif cnt == 4:
#                     pyautogui.press("down")
#                 elif cnt == 5:
#                     pyautogui.press("space")
                
#                 # Update previous count
#                 prev = cnt
#                 start_init = False

#         # Display action on the frame
#         if cnt in finger_action:
#             cv2.putText(frm, finger_action[cnt], (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

#         # Draw landmarks and connections on the hand
#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     # Display the frame with landmarks and instructions
#     cv2.imshow("Hand Gesture Control", frm)

#     # Exit on pressing the 'ESC' key
#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         cap.release()
#         break


# import cv2 
# import mediapipe as mp
# import pyautogui
# import time
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont

# def count_fingers(lst):
#     cnt = 0
#     thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

#     if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
#         cnt += 1

#     if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
#         cnt += 1

#     return cnt 

# # Function to put non-English text on the OpenCV frame using Pillow
# def put_non_english_text_on_frame(frame, text, position, font_path='arial.ttf', font_size=32, color=(255, 255, 255)):
#     # Convert the OpenCV frame (numpy array) to a Pillow Image
#     pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     draw = ImageDraw.Draw(pil_image)

#     # Load the font (You may need to download a TTF font that supports the desired language)
#     font = ImageFont.truetype(font_path, font_size)

#     # Draw the text on the image using Pillow
#     draw.text(position, text, font=font, fill=color)

#     # Convert the Pillow Image back to an OpenCV frame
#     frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     return frame

# cap = cv2.VideoCapture(0)
# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)

# start_init = False 
# prev = -1

# # Dictionary to map finger counts to actions
# finger_action = {
#     1: "Going Right (1 Finger)",  
#     2:  "Going Left (2 Fingers)",  
#     3: "Going Up (3 Fingers)",   
#     4: "Going Down (4 Fingers)",  
#     5: "Pause/Play (5 Fingers) तू बघत राहा पण थांबू नकोस "     
# }

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     # Convert frame to RGB and process with MediaPipe hands
#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:
#         hand_keyPoints = res.multi_hand_landmarks[0]
#         cnt = count_fingers(hand_keyPoints)

#         # If the finger count changes, initialize the action
#         if not(prev == cnt):
#             if not start_init:
#                 start_time = time.time()
#                 start_init = True
#             elif (end_time - start_time) > 0.2:  # Debounce for 0.2 seconds
#                 if cnt == 1:
#                     pyautogui.press("right")
#                 elif cnt == 2:
#                     pyautogui.press("left")
#                 elif cnt == 3:
#                     pyautogui.press("up")
#                 elif cnt == 4:
#                     pyautogui.press("down")
#                 elif cnt == 5:
#                     pyautogui.press("space")
                
#                 # Update previous count
#                 prev = cnt
#                 start_init = False

#         # Display non-English (e.g., Hindi) action on the frame using Pillow
#         if cnt in finger_action:
#             frm = put_non_english_text_on_frame(frm, finger_action[cnt], (10, 50), font_path="path_to_hindi_font.ttf", font_size=40, color=(0, 255, 0))

#         # Draw landmarks and connections on the hand
#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     # Display the frame with landmarks and instructions
#     cv2.imshow("Hand Gesture Control", frm)

#     # Exit on pressing the 'ESC' key
#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         cap.release()
#         break

# import cv2
# import mediapipe as mp
# import pyautogui
# import pywhatkit as kit
# import time
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont

# def count_fingers(lst):
#     cnt = 0
#     thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

#     if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
#         cnt += 1

#     if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
#         cnt += 1

#     if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
#         cnt += 1

#     if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
#         cnt += 1

#     if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
#         cnt += 1

#     return cnt

# # Function to send a WhatsApp message
# def send_whatsapp_message():
#     phone_number = "+919767161003"  # Replace with the recipient's phone number
#     message = "Hello, this is an automated message!"
    
#     # Schedule message to be sent in the next minute
#     kit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
#     print(f"Message scheduled for {phone_number}")

# # Function to put non-English text on the OpenCV frame using Pillow
# def put_non_english_text_on_frame(frame, text, position, font_path='arial.ttf', font_size=32, color=(255, 255, 255)):
#     # Convert the OpenCV frame (numpy array) to a Pillow Image
#     pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     draw = ImageDraw.Draw(pil_image)

#     # Load the font (You may need to download a TTF font that supports the desired language)
#     font = ImageFont.truetype(font_path, font_size)

#     # Draw the text on the image using Pillow
#     draw.text(position, text, font=font, fill=color)

#     # Convert the Pillow Image back to an OpenCV frame
#     frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     return frame

# # Video Capture setup
# cap = cv2.VideoCapture(0)
# drawing = mp.solutions.drawing_utils
# hands = mp.solutions.hands
# hand_obj = hands.Hands(max_num_hands=1)

# start_init = False
# prev = -1

# # Dictionary to map finger counts to actions
# finger_action = {
#     1: "Going Right (1 Finger)",  
#     2:  "Going Left (2 Fingers)",  
#     3: "Going Up (3 Fingers)",   
#     4: "Going Down (4 Fingers)",  
#     5: "Pause/Play (5 Fingers)"  # Marathi example
# }

# while True:
#     end_time = time.time()
#     _, frm = cap.read()
#     frm = cv2.flip(frm, 1)

#     # Convert frame to RGB and process with MediaPipe hands
#     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

#     if res.multi_hand_landmarks:
#         hand_keyPoints = res.multi_hand_landmarks[0]
#         cnt = count_fingers(hand_keyPoints)

#         # If the finger count changes, initialize the action
#         if not (prev == cnt):
#             if not start_init:
#                 start_time = time.time()
#                 start_init = True
#             elif (end_time - start_time) > 0.2:  # Debounce for 0.2 seconds
#                 if cnt == 1:
#                     pyautogui.press("right")
#                 elif cnt == 2:
#                     pyautogui.press("left")
#                 elif cnt == 3:
#                     pyautogui.press("up")
#                 elif cnt == 4:
#                     pyautogui.press("down")
#                 elif cnt == 5:
#                     # Trigger WhatsApp message when 5 fingers are detected
#                     send_whatsapp_message()

#                 # Update previous count
#                 prev = cnt
#                 start_init = False

#         # Display non-English (e.g., Hindi or Marathi) action on the frame using Pillow
#         if cnt in finger_action:
#             frm = put_non_english_text_on_frame(frm, finger_action[cnt], (10, 50), font_path="path_to_font.ttf", font_size=40, color=(0, 255, 0))

#         # Draw landmarks and connections on the hand
#         drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

#     # Display the frame with landmarks and instructions
#     cv2.imshow("Hand Gesture Control", frm)

#     # Exit on pressing the 'ESC' key
#     if cv2.waitKey(1) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2 
import mediapipe as mp
import pyautogui
import time

# Function to count fingers
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

# Initialize the camera and Haar Cascade for face detection
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

start_init = False 
prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a face is detected, proceed with hand gesture detection
    if len(faces) > 0:
        res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:
            hand_keyPoints = res.multi_hand_landmarks[0]

            cnt = count_fingers(hand_keyPoints)

            if not(prev == cnt):
                if not(start_init):
                    start_time = time.time()
                    start_init = True

                elif (end_time - start_time) > 0.2:
                    if (cnt == 1):
                        pyautogui.press("right")

                    elif (cnt == 2):
                        pyautogui.press("left")

                    elif (cnt == 3):
                        pyautogui.press("up")

                    elif (cnt == 4):
                        pyautogui.press("down")

                    elif (cnt == 5):
                        pyautogui.press("space")

                    prev = cnt
                    start_init = False

            drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    # Display the camera feed with face detection box (if a face is detected)
    for (x, y, w, h) in faces:
        cv2.rectangle(frm, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw rectangle around the face

    cv2.imshow("Hand Gesture Control with Face Detection", frm)

    if cv2.waitKey(1) == 27:  # Exit on pressing 'Esc' key
        cv2.destroyAllWindows()
        cap.release()
        break

