# mycket taget från https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/

import cv2
import time
from datetime import datetime



def start_record(record_time):
	print ("Recording")
	cap = cv2.VideoCapture(0)  
	
	fps = 15
	width = 640
	height = 480
	today = datetime.now()
	filename = "files_to_upload/" + str(today.replace(microsecond=0)) + ".mp4"

	writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


	end_time = time.time() + record_time  
	while time.time() < end_time:
		ret, frame = cap.read()
		writer.write(frame)
		
	cap.release()
	cv2.destroyAllWindows()

	



