
import cv2
from faceDetection import detect, drawBoundary, getRoIs
from dataGenerator import captureImage, getFaceRecNoListFromJSON, getNameFromFaceRecNo
from faceRecognition import recognizeFaces
from customClassifiers import trainClassifier
from frameDraw import addTextTopLeft, drawFacesInfo
import concurrent.futures
import threading
from face import Face
from emotionDetector import EmotionDetector


faceCascade = cv2.CascadeClassifier(
    "cascades/haarcascade_frontalface_default.xml")
customClassifier = cv2.face.LBPHFaceRecognizer_create()
customClassifier.read("cascades/classifier.yml")

video_capture = cv2.VideoCapture(0)
frameId = 0
faceId = 1
captureLimit = 100
detectEmotions = EmotionDetector()

faceRecNoList = getFaceRecNoListFromJSON()


while True:
    _, img = video_capture.read()
    if img is None:
        print("no camrea input!!")
        continue;
    
    faces = detect(img, frameId, faceCascade, "face")
    if(len(faces) > 0):
        # face detected
        # need to parrlely recognition and emotionalized

        # captureImage(RoI, faceId, imgId)
        # imgId += 1
        # faceRecognizerThread = threading.Thread(target = recognizeFaces, args=[customClassifier, RoI, coordinates, img])
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # face recognition thread
            faceRecognizerThread = executor.submit(
                recognizeFaces, customClassifier, faces,  img)  # returns a future object
            faces, img = faceRecognizerThread.result()

            # emotion recognition
            emotionRecognitionThread = executor.submit(
                detectEmotions, faces)
            faces = emotionRecognitionThread.result()

        # add face info to frame
        if(len(faces) > 0):
            drawFacesInfo(faces, img, faceRecNoList)

        frameId += 1  # increase frame number if face detected
    cv2.imshow("face detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
