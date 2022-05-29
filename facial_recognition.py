import cv2 as cv
import face_recognition
from simple_facerec import SimpleFacerec

def facial_recognition(image: Str) -> List[int]:
    img = cv.imread(image)
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
