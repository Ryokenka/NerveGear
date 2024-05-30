import cv2 as cv
import numpy as np
import mediapipe as mp

from Interface.GameEngine.VirtualController import MinecraftEngine



def HeadTracking(func_action_gauche=None, func_action_droit=None, func_action_milieu=None):
	capture = cv.VideoCapture(0)
	face_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_frontalface_default.xml')
	eye_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_eye.xml')

	while True:
		ret, frame = capture.read()
		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 5)
		x, y, w, h = 0, 0, 0, 0
		for (x, y, w, h) in faces:
			cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv.circle(frame, (x + int(w * 0.5), y +
							int(h * 0.5)), 4, (0, 255, 0), -1)
		eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)
		index = 0
		eye_1 = [None, None, None, None]
		eye_2 = [None, None, None, None]
		for (ex, ey, ew, eh) in eyes:
			if index == 0:
				eye_1 = [ex, ey, ew, eh]
			elif index == 1:
				eye_2 = [ex, ey, ew, eh]
			cv.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey),
						(ex + ew, ey + eh), (0, 0, 255), 2)
			index = index + 1
		if (eye_1[0] is not None) and (eye_2[0] is not None):
			if eye_1[0] < eye_2[0]:
				left_eye = eye_1
				right_eye = eye_2
			else:
				left_eye = eye_2
				right_eye = eye_1
			left_eye_center = (
				int(left_eye[0] + (left_eye[2] / 2)),
			int(left_eye[1] + (left_eye[3] / 2)))

			right_eye_center = (
				int(right_eye[0] + (right_eye[2] / 2)),
			int(right_eye[1] + (right_eye[3] / 2)))

			left_eye_x = left_eye_center[0]
			left_eye_y = left_eye_center[1]
			right_eye_x = right_eye_center[0]
			right_eye_y = right_eye_center[1]

			delta_x = right_eye_x - left_eye_x
			delta_y = right_eye_y - left_eye_y

			# Slope of line formula + FIX IF delta_x == 0
			if delta_x != 0:
				angle = np.arctan(delta_y / delta_x)
				# Converting radians to degrees
				angle = (angle * 180) / np.pi
			else:
				angle = 90 if delta_y > 0 else -90



			# Provided a margin of error of 10 degrees
			# (i.e, if the face tilts more than 10 degrees
			# on either side the program will classify as right or left tilt)
			if angle > 10:
				cv.putText(frame, 'RIGHT TILT :' + str(int(angle))+' degrees',
						(20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
						(0, 0, 0), 2, cv.LINE_4)
				func_action_gauche()
				#mouvement_gauche_droite_cam("gauche")
			elif angle < -10:
				cv.putText(frame, 'LEFT TILT :' + str(int(angle))+' degrees',
						(20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
						(0, 0, 0), 2, cv.LINE_4)
				func_action_droit()
			else:
				cv.putText(frame, 'STRAIGHT :', (20, 30),
						cv.FONT_HERSHEY_SIMPLEX, 1,
						(0, 0, 0), 2, cv.LINE_4)
				func_action_milieu()

		cv.imshow('Frame', frame)

		if cv.waitKey(1) & 0xFF == 27:
			break
	capture.release()
	cv.destroyAllWindows()

def HeadEtHandTracking(MC, func_action_gauche=None, func_action_droit=None, func_action_milieu=None, func_action_doigts=None):
	print("HeadEtHandTracking")

	# Initialize Mediapipe Hand module

	mp_drawing = mp.solutions.drawing_utils
	mp_hands = mp.solutions.hands

	# Initialize Opencv webcam capture
	cap = cv.VideoCapture(0)
	face_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_frontalface_default.xml')
	eye_cascade = cv.CascadeClassifier('../CapteursEngine/haarcascade_eye.xml')

	print("Initialize Opencv webcam capture")

	# Initialize Hand module
	with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:

		while cap.isOpened():
			ret, frame = cap.read()
			if not ret:
				break

			# Convert BGR image to RGB
			rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

			# Process the frame to detect hand landmarks
			results = hands.process(rgb_frame)

			if results.multi_hand_landmarks :
				print("Boucle principale")
				#POUR LES DOIGTS
				if 1 == 1:
					print("Je lance les doigts")
					for landmarks in results.multi_hand_landmarks:
						# Calculate finger states
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
						if finger_count > 0:
							if func_action_doigts is not None:
								func_action_doigts(finger_count)

						# Display the detected number on the frame
						font = cv.FONT_HERSHEY_SIMPLEX
						cv.putText(frame, f'Number: {finger_count}', (20, 40), font, 1, (0, 255, 0), 2, cv.LINE_AA)

						# Draw landmarks on the frame
						mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)


			#POUR LA TETE
			if func_action_gauche is not None:
				print("je fais la tete")

				faces = face_cascade.detectMultiScale(rgb_frame, 1.1, 5)
				x, y, w, h = 0, 0, 0, 0
				for (x, y, w, h) in faces:
					cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
					cv.circle(frame, (x + int(w * 0.5), y +
									   int(h * 0.5)), 4, (0, 255, 0), -1)
				eyes = eye_cascade.detectMultiScale(rgb_frame[y:(y + h), x:(x + w)], 1.1, 4)
				index = 0
				eye_1 = [None, None, None, None]
				eye_2 = [None, None, None, None]
				for (ex, ey, ew, eh) in eyes:
					if index == 0:
						eye_1 = [ex, ey, ew, eh]
					elif index == 1:
						eye_2 = [ex, ey, ew, eh]
					cv.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey),
								  (ex + ew, ey + eh), (0, 0, 255), 2)
					index = index + 1
				if (eye_1[0] is not None) and (eye_2[0] is not None):
					if eye_1[0] < eye_2[0]:
						left_eye = eye_1
						right_eye = eye_2
					else:
						left_eye = eye_2
						right_eye = eye_1
					left_eye_center = (
						int(left_eye[0] + (left_eye[2] / 2)),
						int(left_eye[1] + (left_eye[3] / 2)))

					right_eye_center = (
						int(right_eye[0] + (right_eye[2] / 2)),
						int(right_eye[1] + (right_eye[3] / 2)))

					left_eye_x = left_eye_center[0]
					left_eye_y = left_eye_center[1]
					right_eye_x = right_eye_center[0]
					right_eye_y = right_eye_center[1]

					delta_x = right_eye_x - left_eye_x
					delta_y = right_eye_y - left_eye_y

					# Slope of line formula + FIX IF delta_x == 0
					if delta_x != 0:
						angle = np.arctan(delta_y / delta_x)
						# Converting radians to degrees
						angle = (angle * 180) / np.pi
					else:
						angle = 90 if delta_y > 0 else -90

					if angle > 10:
						cv.putText(frame, 'RIGHT TILT :' + str(int(angle)) + ' degrees',
								   (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
								   (0, 0, 0), 2, cv.LINE_4)
						if func_action_gauche is not None:
							func_action_gauche()
						#MC.mouvement_gauche_droite_cam("gauche")
					elif angle < -10:
						cv.putText(frame, 'LEFT TILT :' + str(int(angle)) + ' degrees',
								   (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
								   (0, 0, 0), 2, cv.LINE_4)
					if func_action_droit is not None:
						func_action_droit()
						#MC.mouvement_gauche_droite_cam("droite")
					else:
						cv.putText(frame, 'STRAIGHT :', (20, 30),
								   cv.FONT_HERSHEY_SIMPLEX, 1,
								   (0, 0, 0), 2, cv.LINE_4)
					if func_action_milieu is not None:
						func_action_milieu()
						#MC.mouvement_gauche_droite_cam("milieu")

					cv.imshow('Finger Count', frame)


					if cv.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
						break

	cap.release()
	cv.destroyAllWindows()







