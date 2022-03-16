import cv2

img=cv2.imread("put the name of pic with extension")
pedestrian_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

def pedestrian_detection(frame):
    pedestrians=pedestrian_cascade.detectMultiScale(frame,1.1,1)
    for(x,y,w,h) in pedestrians:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,'person',(x+6,y-6),font,0.5,(0,255,0),2)
    return frame
output=pedestrian_detection(img)

cv2.imwrite("new image name",output)

cap=cv2.VideoCapture('people.mp4') #same with video write the name of video with extension
ret,frame=cap.read()

frame_height,frame_width, _ =frame.shape

out =cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','p','G'),10,(frame_width,frame_height))
print("Processing Video...")
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        out.release()
        break
    output=pedestrian_detection(frame)
    out.write(output)
out.release()
print("Done processing Video")