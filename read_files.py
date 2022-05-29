'''
read_files.py module functions assists with reading the names of each file in the people
and pics folders so that navigating and interacting with images within will be
easier in face_block.py
'''

# Package imports: os
import os

def people() -> list[str]:
    '''
    people() returns an array of file path names for each image in the images/people folder
    '''
    people = []
    for person in os.listdir("images/people"):
        if person != ".DS_Store":
            people.append("images/people/" + person)
    return people

def pics() -> list[str]:
    '''
    pics() returns an array of file path names for each image in the images/pics folder
    '''
    pics = []
    for person in os.listdir("images/pics"):
        if person != ".DS_Store":
            pics.append("images/pics/" + person)
    return pics