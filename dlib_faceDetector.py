# dlib Frontal face detector to find the faces available in an Image
# Extract every frame from video capture
# Process the frame with dlib package to detect faces in Image
# Print the total no of faces available in the Image/Video
# Extract the co-ordinates of face using image utilities library and store then as 4 dimensions
# Draw the rectangle for every face using the extracted co-ordinates
# Destroy the windows and release the video capturing to avoid hardware failure.
from imutils import face_utils
import dlib
import cv2
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
while True:
    _, frame = cap.read()
    faces = detector(frame,0)
    if len(faces) > 0:
        text = "{} Nos of Faces Detected".format(len(faces))
        cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_DUPLEX,
        0.5, (0,125,255),1)
    for face in faces:
        (x, y, w, h) = face_utils.rect_to_bb(face)
        cv2.rectangle(frame, (x,w),(x+h,y+h), (255,120,64),2)
    cv2.imshow("Detecting Frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()