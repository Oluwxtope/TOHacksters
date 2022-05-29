# FaceBlock

Say you're at an event and you're not feeling or *looking* your best, and just as you're feeling thankful there is no record of this travesty, your eyes are immediately stunned by a flash from a camera shutter. Maybe I'm being a bit too specific, but it's happened to most of us, and if it hasn't happened to you yet, then it's only a matter of time. We created FaceBlock as a cure to every shy persons nightmare of being included in photos or videos, and for event planners that don't want to go through the hassle of combing through photos and videos to remove people who don't want to be included.

# What it does

Our users who don't want their faces posted all over the internet sign up by uploading a clear picture of themselves and their name (*don't worry, we won't sell your data*) to our app to be stored in our database. Then event planners who recognize that people indeeed have the right to privacy upload photos and videos from their events to our app, and our efficiently engineered python script combs through each photo and video, and blurs out the faces of our users using the OpenCV and Face Recognition packages. The now edited photographs and videos are processed and exported to the uploaders for their use!

# How we built it

1. We encode the faces of every user in our database and store these encodings
2. When we receive a bunch of photos/videos from an organizer who is privacy conscious, we process each of the uploads and search for our users' faces in them
3. If we find any of our users, we blur them out and it's like they were never there! (with over ~80% accuracy in our tests)

# Challenges we faced

With our team having no experience with computer vision using OpenCV or Face Recognition (except for Angel), we had to read lots of documentations and watch videos to learn how to go about building this. It was quite challenging but we did it!

We also were unable to complete the front end of the project and host on a domain, record a demo video, and add the video blurring component of the app before the deadline but in the end we do have a working script that blurs peoples faces from in face_block.py and will continue rounding out the project.