import threading
import cv2
from deepface import DeepFace

# Initialize the video capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = cv2.imread("reference.jpg")

if reference_img is None:
    print("Error: reference.jpg not found or unable to load")
else:
    print("reference.jpg loaded successfully")

# Function to check face matching
def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img.copy())
        print("DeepFace result:", result)
        face_match = result['verified']
    except Exception as e:
        print("Error in DeepFace.verify:", e)
        face_match = False

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture video frame")
        break
    
    if counter % 30 == 0:
        try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
        except Exception as e:
            print("Error starting thread:", e)
    
    counter += 1
    
    if face_match:
        cv2.putText(frame, "Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "No Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    
    cv2.imshow("video", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
