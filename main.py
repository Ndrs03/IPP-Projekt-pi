import record
#import upload
#import stats


while input("Sensor? ") != 'n':
	record.start_record(10)
	stats.update_csv()
	#upload.upload_file()



