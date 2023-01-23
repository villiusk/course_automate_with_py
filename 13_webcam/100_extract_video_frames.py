# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

video = cv2.VideoCapture("video.mp4")
success, frame = video.read()

count = 1
while success:
  cv2.imwrite(f'images/{count}.jpg', frame)
  success, frame = video.read()
  count += 1