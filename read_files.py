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