import record
import upload


while input("Sensor? ") != 'n':

	record.start_record()
	upload.upload_file()



