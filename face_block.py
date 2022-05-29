import cv2 as cv
import face_recognition

import read_files

def face_block():
    known_faces = []
    people = read_files.people()
    for person_img in people:
        image = cv.imread(person_img)
        cv.imshow("image", image)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image_encoding = face_recognition.face_encodings(rgb_image)
        for encoding in image_encoding:
            known_faces.append(encoding)

    return known_faces

print(face_block())