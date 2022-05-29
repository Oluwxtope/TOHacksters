'''
face_block.py contains core function to run FaceBlock
'''

# Package imports: cv2, face_recognition, numpy
import cv2 as cv
import face_recognition
import numpy as np

# Module imports: read_files - processes the names of image files for ease of access
import read_files

def face_block() -> None:
    # 1. identify people that want their face blurred from the images/people folder
    known_face_encodings = [] # saves face encodings of people who want face blurred
    known_faces_to_blur = [] # will contain true for all faces to blur, will be used as zip pair
    people = read_files.people()
    for person_img in people:
        image = cv.imread(person_img)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image_encoding = face_recognition.face_encodings(rgb_image)
        for encoding in image_encoding:
            known_face_encodings.append(encoding)
            known_faces_to_blur.append(True)

    faces_to_blur = []
    pics = read_files.pics()
    for pic_img in pics:
        image = cv.imread(pic_img)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        faces_to_blur = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            to_blur = False
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                to_blur = known_faces_to_blur[best_match_index]
            faces_to_blur.append(to_blur)
        
        # Display the results
        for (top, right, bottom, left), to_blur in zip(face_locations, faces_to_blur):
            if to_blur:
                # pixelated blur
                # divide the input image into NxN blocks
                blocks = 7
                xSteps = np.linspace(left, right, blocks + 1, dtype="int")
                ySteps = np.linspace(top, bottom, blocks + 1, dtype="int")
                # loop over the blocks in both the x and y direction
                for i in range(1, len(ySteps)):
                    for j in range(1, len(xSteps)):
                        # compute the starting and ending (x, y)-coordinates
                        # for the current block
                        startX = xSteps[j - 1]
                        startY = ySteps[i - 1]
                        endX = xSteps[j]
                        endY = ySteps[i]
                        # extract the ROI using NumPy array slicing, compute the
                        # mean of the ROI, and then draw a rectangle with the
                        # mean RGB values over the ROI in the original image
                        roi = image[startY:endY, startX:endX]
                        (B, G, R) = [int(x) for x in cv.mean(roi)[:3]]
                        cv.rectangle(image, (startX, startY), (endX, endY),
                            (B, G, R), -1)
        
        # Display the resulting image
        cv.imshow('Image', image)
        cv.waitKey(0)

face_block()