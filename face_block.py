# Main face_block file

from ast import Name
import cv2 as cv
import face_recognition
import numpy as np

import read_files # Use the directory names

def face_block():
    # Iterate thru each image in images/people and store an array known_face_encodings
    # with all image encodings present of people who don't want their faces in pics
    known_face_encodings = []
    known_face_names = []
    people = read_files.people()
    for person_img in people:
        image = cv.imread(person_img)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image_encoding = face_recognition.face_encodings(rgb_image)
        for encoding in image_encoding:
            known_face_encodings.append(encoding)
            known_face_names.append(person_img)
    # Iterate thru ...
    faces_to_blur = []
    face_names = []
    pics = read_files.pics()
    for pic_img in pics:
        image = cv.imread(pic_img)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
        
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        # Display the resulting image
        cv.imshow('Image', image)
        cv.waitKey(0)

face_block()