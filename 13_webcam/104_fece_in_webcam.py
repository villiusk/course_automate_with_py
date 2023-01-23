# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# NOTE: This script does not work on Repl. 
# It only works when run on a computer with a webcam

import cv2

video = cv2.VideoCapture(1)
success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 0
while success:
  faces = face_cascade.detectMultiScale(frame, 1.1, 4)
  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
  output.write(frame)
  success, frame = video.read()
  count += 1
  print(count)

output.release()