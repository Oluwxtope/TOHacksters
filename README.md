# FaceBlock

Say you're at an event and you're not feeling or *looking* your best, and just as you're feeling thankful there is no record of this travesty, your eyes are immediately stunned by a flash from a camera shutter. Maybe I'm being a bit too specific, but it's happened to most of us, and if it hasn't happened to you yet, then it's only a matter of time. We created FaceBlock as a cure to every shy persons nightmare of being included in photos or videos, and for event planners that don't want to go through the hassle of combing through photos and videos to remove people who don't want to be included.
<br>

# What it does

Our users who don't want their faces posted all over the internet sign up by uploading a clear picture of themselves and their name (*don't worry, we won't sell your data*) to our app to be stored in our database. Then event planners who recognize that people indeeed have the right to privacy upload photos and videos from their events to our app, and our efficiently engineered python script combs through each photo and video, and blurs out the faces of our users using the OpenCV and Face Recognition packages. The now edited photographs and videos are processed and exported to the uploaders for their use!
<br>  

# How we built it

1. We encode the faces of every user in our database and store these encodings  
2. When we receive a bunch of photos/videos from an organizer who is privacy conscious, we process each of the uploads and search for our users' faces in them  
3. If we find any of our users, we blur them out and it's like they were never there! (with over ~90% accuracy in our tests*)  
   \* Tests conducted on professionally captured images with near-perfect lighting and on white people

# Future of FaceBlock

1. Improve accurary of face scanning and blurring. Current known issues are:  
   - Difficulty detecting faces identified if face is obstructed by accessory ie glasses  
   - Difficulty detecting faces identified if image has low lighting  
   - Can sometimes confuse faces especially with black people  
2. Reduce processing time by downscaling image and then processing facial data. We will have to examine the tradeoff between accuracy and faster processing time quantitatively  
3. Implement video face blurring