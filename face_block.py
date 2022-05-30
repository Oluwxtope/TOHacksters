'''
face_block.py contains core function to run FaceBlock
'''

# Package imports: cv2, face_recognition, numpy
import cv2 as cv
import face_recognition
import numpy as np

# Module imports: read_files - processes the names of image files for ease of access
import read_filename

def face_block() -> None:
    '''
    face_block() indexes the faces of users in images/people and iterates thru
    pics in images/pics blurring out the faces of users found
    '''
    # 1. create list of files to iterate thru
    people_filepath = "images/people"
    people_filenames = read_filename.read_filenames(people_filepath)
    pics_filepath = "images/pics"
    pics_filenames = read_filename.read_filenames(pics_filepath)
    final_filepath = "images/final"

    # 2. identify people that want their face blurred from the images/people folder
    known_face_encodings = [] # saves face encodings of people who want face blurred
    for person_img in people_filenames:
        person_filepath = people_filepath + "/" + person_img
        image = cv.imread(person_filepath) 
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB) # covert to rgb from bgr for face_recognition package
        image_encoding = face_recognition.face_encodings(rgb_image) # encode faces in image
        for encoding in image_encoding: # append each encoded face to known_face_encodings array
            known_face_encodings.append(encoding)
    
    # 3. iterate thru images/pics and blur faces of users in known_face_encodings
    faces_to_blur = [] # keeps track of faces to blur
    for pic_img in pics_filenames:
        pic_filepath = pics_filepath + "/" + pic_img
        image = cv.imread(pic_filepath)
        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_image) # save locations of faces in image
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
        
        # check which faces to blur in each encoding in the image
        faces_to_blur = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding) # compare each face in pic to user faces
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            to_blur = False # by default faces aren't to be blurred
            if matches[best_match_index]:
                to_blur = True
            faces_to_blur.append(to_blur)
        
        # pixelate their faces with blur
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
                        cv.rectangle(image, (startX, startY), (endX, endY), (B, G, R), -1)
        
        # display the resulting image
        # cv.imshow(pic_img, image)
        # cv.waitKey(5)

        # save result
        try:
            saved = cv.imwrite(final_filepath + "/" + pic_img, image)
            print(pic_img + " was processed and saved successfully.")
        except:
            print("ERROR: " + pic_img + " wasn't saved!")
            continue

face_block()