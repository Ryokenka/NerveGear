# Importing the required dependencies
import cv2 # for video rendering
import dlib # for face and landmark detection
import imutils
# for calculating dist b/w the eye landmarks
from scipy.spatial import distance as dist
# to get the landmark ids of the left and right eyes
# you can do this manually too
from imutils import face_utils

# defining a function to calculate the EAR
def calculate_EAR(eye):

    # calculate the vertical distances
    y1 = dist.euclidean(eye[1], eye[5])
    y2 = dist.euclidean(eye[2], eye[4])

    # calculate the horizontal distance
    x1 = dist.euclidean(eye[0], eye[3])

    # calculate the EAR
    EAR = (y1+y2) / x1
    return EAR

# Variables
blink_thresh = 0.35
succ_frame = 2
count_frame = 0
blink_count = 0

# Eye landmarks
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

# Initializing the Models for Landmark and
# face Detection
detector = dlib.get_frontal_face_detector()
landmark_predict = dlib.shape_predictor(
    'shape_predictor_68_face_landmarks.dat')

# Open a connection to the webcam (0 indicates the default camera)
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = imutils.resize(frame, width=640)

    # converting frame to gray scale to pass to detector
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecting the faces
    faces = detector(img_gray)
    for face in faces:
        # landmark detection
        shape = landmark_predict(img_gray, face)

        # converting the shape class directly to a list of (x,y) coordinates
        shape = face_utils.shape_to_np(shape)

        # parsing the landmarks list to extract lefteye and righteye landmarks
        lefteye = shape[L_start: L_end]
        righteye = shape[R_start: R_end]

        # Calculate the EAR
        left_EAR = calculate_EAR(lefteye)
        right_EAR = calculate_EAR(righteye)

        # Avg of left and right eye EAR
        avg = (left_EAR + right_EAR) / 2
        if avg < blink_thresh:
            count_frame += 1  # incrementing the frame count
            if count_frame >= succ_frame:
                blink_count += 1
                if blink_count == 2:
                    cv2.putText(frame, 'Double Blink Detected', (30, 30),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 1)
                count_frame = 0  # Reset count_frame when text is displayed
        else:
            count_frame = 0  # Reset count_frame if the condition is not met
            blink_count = 0  # Reset blink_count if the condition is not met

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cam.release()
cv2.destroyAllWindows()