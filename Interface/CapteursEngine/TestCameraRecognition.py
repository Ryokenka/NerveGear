import inspect

import cv2 as cv
import numpy as np
import mediapipe as mp




def detect_head(frame, face_cascade, eye_cascade, func_action_gauche, func_action_droit, func_action_milieu):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    x, y, w, h = 0, 0, 0, 0
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame, (x + int(w * 0.5), y + int(h * 0.5)), 4, (0, 255, 0), -1)

    eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)
    index = 0
    eye_1, eye_2 = [None, None, None, None], [None, None, None, None]
    for (ex, ey, ew, eh) in eyes:
        if index == 0:
            eye_1 = [ex, ey, ew, eh]
        elif index == 1:
            eye_2 = [ex, ey, ew, eh]
        cv.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
        index += 1

    if (eye_1[0] is not None) and (eye_2[0] is not None):
        left_eye, right_eye = (eye_1, eye_2) if eye_1[0] < eye_2[0] else (eye_2, eye_1)
        left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
        right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))

        delta_x, delta_y = right_eye_center[0] - left_eye_center[0], right_eye_center[1] - left_eye_center[1]
        angle = np.arctan(delta_y / delta_x) * 180 / np.pi if delta_x != 0 else 90 if delta_y > 0 else -90

        if angle > 10:
            cv.putText(frame, 'LEFT TILT :' + str(int(angle)) + ' degrees', (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 0), 2, cv.LINE_4)
            if func_action_gauche:
                func_action_gauche()
        elif angle < -10:
            cv.putText(frame, 'RIGHT TILT :' + str(int(angle)) + ' degrees', (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 0), 2, cv.LINE_4)
            if func_action_droit:
                func_action_droit()
        else:
            cv.putText(frame, 'STRAIGHT :', (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_4)
            if func_action_milieu:
                print("je devrais aller dans VC")
                func_action_milieu()

    return frame


def detect_hand(frame, hands, mp_drawing, func_action_doigts):
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            index_finger_MCP = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            index_dip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
            middle_dip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
            ring_dip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
            pinky_dip = landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]

            finger_states_tip = [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]
            finger_states_dip = [index_finger_MCP, index_dip, middle_dip, ring_dip, pinky_dip]
            up_fingers = sum(
                1 for i in range(len(finger_states_tip)) if finger_states_tip[i].y < finger_states_dip[i].y)
            finger_count = min(up_fingers, 5)
            if finger_count > 0 and func_action_doigts:
                func_action_doigts(finger_count)

            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(frame, f'Number: {finger_count}', (20, 40), font, 1, (0, 255, 0), 2, cv.LINE_AA)
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    return frame

def detect_2hand(frame, hands, mp_drawing, func_action_doigts):
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    if results.multi_hand_landmarks:
        left_hand_fingers = 0
        right_hand_fingers = 0
        for landmarks in results.multi_hand_landmarks:
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            index_finger_MCP = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            index_dip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
            middle_dip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
            ring_dip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
            pinky_dip = landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]

            finger_states_tip = [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]
            finger_states_dip = [index_finger_MCP, index_dip, middle_dip, ring_dip, pinky_dip]

            # Compter les doigts levés pour chaque main
            if landmarks.landmark[mp_hands.HandLandmark.WRIST].x < landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x:
                # Main gauche
                left_hand_fingers += sum(
                    1 for i in range(len(finger_states_tip)) if finger_states_tip[i].y < finger_states_dip[i].y)
            else:
                # Main droite
                right_hand_fingers += sum(
                    1 for i in range(len(finger_states_tip)) if finger_states_tip[i].y < finger_states_dip[i].y)

            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        # Afficher le nombre de doigts levés pour chaque main
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, f'Left hand: {left_hand_fingers}', (20, 40), font, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.putText(frame, f'Right hand: {right_hand_fingers}', (20, 80), font, 1, (0, 255, 0), 2, cv.LINE_AA)

        # Appeler la fonction d'action si au moins une main a des doigts levés
        if (left_hand_fingers > 0 or right_hand_fingers > 0) and func_action_doigts:
            print(left_hand_fingers, right_hand_fingers, left_hand_fingers+right_hand_fingers)
            func_action_doigts(left_hand_fingers+right_hand_fingers)

    return frame

def HeadAndHandTracking(func_action_gauche=None, func_action_droit=None, func_action_milieu=None,
                        func_action_doigts=None):
    print("Head and Hand tracking")
    #print("Function for func_action_droit1:", inspect.getsource(func_action_droit))
    if func_action_droit:
        print("je veux pouvoir aller à  droite")
    if func_action_gauche:
        print("je veux pourvoir aller a gauche")
    if func_action_milieu:
        print("je veux pourvoir aller au milieu")
    if func_action_doigts:
        print("je veux pourvoir utiliser les mains")

    capture = cv.VideoCapture(0)
    face_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_eye.xml')

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.8) as hands:
        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break

            # Détecter la tête
            if func_action_gauche or func_action_droit or func_action_milieu:

                frame = detect_head(frame, face_cascade, eye_cascade, func_action_gauche, func_action_droit,
                                    func_action_milieu)

            # Détecter les mains
            if func_action_doigts:
                frame = detect_2hand(frame, hands, mp_drawing, func_action_doigts)

            cv.imshow('Head and Hand Tracking', frame)
            if cv.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                break

    capture.release()
    cv.destroyAllWindows()


