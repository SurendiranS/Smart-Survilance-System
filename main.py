import cv2
import face_recognition
print("Library imported Successfully")


cap = cv2.VideoCapture(0)

while True:
	success, img = cap.read()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	loc = face_recognition.face_locations(img)
	if len(loc) == 1:
		encode = face_recognition.face_encodings(img,loc)
		cv2.rectangle(img, (loc[0][3],loc[0][0]), (loc[0][1],loc[0][2]), (255,0,255), 2)
	elif len(loc) < 1:
		print("NO face Detected")
	else:
		print("Many faces Detected")
		for i in loc:
			cv2.rectangle(img, (i[3],i[0]), (i[1],i[2]), (255,0,255), 2)

	cv2.imshow("VideoCapture",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break;
	print(loc)