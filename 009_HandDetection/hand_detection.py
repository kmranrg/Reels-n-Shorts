import cv2
import mediapipe as mp

# initialize mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# initialize MediaPipe Drawing Module for drawing landmarks
mp_drawing = mp.solutions.drawing_utils

# set up video capture from webcam (0 for the default camera)
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert the BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # display the result
    cv2.imshow('Hand Detection',frame)

    # exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()