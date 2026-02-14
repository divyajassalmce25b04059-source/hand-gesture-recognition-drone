import cv2
import mediapipe as mp
import math

# Direct access to the solutions
try:
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
except AttributeError:
    print("Error: Mediapipe 'solutions' not found. Please reinstall mediapipe.")
    exit()

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def recognize_gesture(landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb logic (horizontal check)
    if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # 4 Fingers logic (vertical check)
    for i in range(1, 5):
        if landmarks[tips[i]].y < landmarks[tips[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Command Logic
    if fingers == [1, 1, 1, 1, 1]: return "TAKEOFF"
    if fingers == [0, 0, 0, 0, 0]: return "LAND"
    if fingers == [0, 1, 0, 0, 0]: return "FORWARD"
    if fingers == [0, 1, 1, 0, 0]: return "BACKWARD"
    if fingers == [1, 1, 0, 0, 1]: return "FLIP"
    if fingers == [0, 0, 0, 0, 1]: return "EMERGENCY STOP"
    
    if get_distance(landmarks[4], landmarks[8]) < 0.05:
        return "ROTATE CW"

    if fingers[0] == 1 and fingers.count(1) == 1:
        return "MOVE LEFT" if landmarks[4].x < landmarks[17].x else "MOVE RIGHT"

    return "HOVERING"

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    display_text = "SCANNING..."

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            display_text = recognize_gesture(hand_lms.landmark)

    cv2.putText(frame, f"CMD: {display_text}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Drone Control", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()