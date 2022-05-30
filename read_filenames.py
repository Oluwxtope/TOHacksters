'''
read_files.py module functions assists with reading the names of each file in the people
and pics folders so that navigating and interacting with images within will be
easier in face_block.py
'''

# Package imports: os
import os

def read_filenames(folder: str) -> list[str]:
    '''
    read_filenames(folder) takes in the pathway to a folder and returns a list
    with the names of the files in the folder
    requires: folder has ONLY files present
    '''
    filenames = []
    for file in os.listdir(folder):
        filenames.append(file)
    return filenames

# tests
print(read_filenames("images/people"))