import cv2
import time
from datetime import datetime

RECORD_TIME = 5  #sekunder

cap = cv2.VideoCapture(0)  

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def start_record():
	today = datetime.now()
	filename = "files_to_upload/" + str(today.replace(microsecond=0)) + ".mp4"

	writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))


	end_time = time.time() + RECORD_TIME  # 5sek
	while time.time() < end_time:
		ret, frame = cap.read()
		writer.write(frame)

	
#def cleanup():
	
	#cap.release()
	#cv2.destroyAllWindows()

# mycket taget från https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
