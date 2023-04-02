import cv2
vidcap = cv2.VideoCapture('video_path')
success, image = vidcap.read()
number = 0
#while success:
while count < 1000:
  cv2.imwrite("images_path" % number, image) # where you want to save images
  success, image = vidcap.read()
  number += 1