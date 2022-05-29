# Helper module that assists with reading the names of each file in the people
# and pics folders so that navigating and interacting with images within will be
# easier in face_block.py

import os

def people():
    people = []
    for person in os.listdir("images/people"):
        if person != ".DS_Store":
            people.append("images/people/" + person)
    return people

def pics():
    pics = []
    for person in os.listdir("images/pics"):
        if person != ".DS_Store":
            pics.append("images/pics/" + person)
    return pics