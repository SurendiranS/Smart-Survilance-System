import os
os.system("clear")
print("Starting....")
import cv2
import face_recognition
import numpy
print("Library imported Successfully")

print("Initializing Camera")
cap = cv2.VideoCapture(0)
print("Camera Initialized Successfully")

knownFaces = []
knownNames = []

while True:
	n = int(input("\n\nPress 1 to Detect\nPress 2 to Register\nEnter Your choice : "))
	if n == 1:
		while  True:
			success, img = cap.read()
			locs = face_recognition.face_locations(img)
			encoding = face_recognition.face_encodings(img,locs)
			cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
			for face,loc in zip(encoding,locs):
				result = face_recognition.compare_faces(knownFaces, face, 0.5)
				match = "UNKNOWN"
				if True in result:
					match = knownNames[result.index(True)]
				cv2.rectangle(img, (loc[3],loc[0]), (loc[1],loc[2]), (0,255,0), 2)
				cv2.rectangle(img, (loc[3],loc[2]-25), (loc[1],loc[2]), (0,255,0),cv2.FILLED)
				cv2.putText(img, match, (loc[3]+6, loc[2]-6), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,255,255), 1)
			cv2.imshow("Searching",img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				cv2.destroyWindow("Searching")
				break;
	elif n == 2:
		name = input("Enter Your Name : ")
		while True:
			success, img = cap.read()
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			loc = face_recognition.face_locations(img)
			if len(loc) == 1:
				cv2.rectangle(img, (loc[0][3],loc[0][0]), (loc[0][1],loc[0][2]), (255,255,255), 1)
			elif len(loc) < 1:
				print("NO face Detected")
			else:
				print("Many faces Detected")
				for i in loc:
					cv2.rectangle(img, (i[3],i[0]), (i[1],i[2]), (255,0,255), 2)
			img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
			cv2.imshow("VideoCapture",img)
			if cv2.waitKey(1) & 0xFF == ord('q') and len(loc) == 1:
				encode = face_recognition.face_encodings(img,loc)[0]
				knownFaces.append(encode)
				knownNames.append(name)
				cv2.destroyWindow("VideoCapture")
				break;
			print(loc)
		print(knownFaces)
		print(knownNames)
	else:
		break
