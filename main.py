import record
import upload
import stats
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)

# Delay är satt så lågt som möjligt på sensorn vilket är ca 15s så minimum inspelningstid är ca 15s annars startas en till filmning innan sensorn hinner bli 0

while True:

	if GPIO.input(20):
		print("Sensor detected")
		record.start_record(20)	# filma 20 sek
		stats.update_csv()
		upload.upload_file()
		upload.upload_csv()
		print("All done!")
	else:
		time.sleep(2)

