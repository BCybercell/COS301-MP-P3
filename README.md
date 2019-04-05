## Phase 3 of COS 301 mini-project. 

# Facial Recognition- Ocean(Group 12)  
This project mainly focuses on designing next-gen ATM's for FNB as part of a assignment for COS 301.
We are tasked with implementing the **Facial Recognition** subsystem which involves receiving an image from the **Authentication** subsystem and matching that image to a user id on our database. We then send back the user id or an exception to **Authentication** subsystem. We also have to maintain or database with data from the **Client Information System**.

We plan on implementing these features in **Python** and hosting our services via an API.

## Usage
Teams can use our Facial recognition services by sending a post request with an image to the following url: [Authenticate User](https://cos301frocean.herokuapp.com/AuthUser/).   
The AuthUser function will use this image to identify and recognize users in our database if they are present.  
An example of what is returned when a user is recognized succesfully:  
        ```json
            {"status": true, "userID": "0"}
        ```  
If the user is is not recognized the following will be returned:  
        ```json
            {"status": false, "Exception": "Not Authenticated"}
        ```         
  
The **Client Information System** can use the following link for sending an updated user list [Client](https://cos301frocean.herokuapp.com/Clients/)  
    Examples: 
        https://cos301frocean.herokuapp.com/Clients/data={"Operation":"subscribed","ID":["21","31",...]} 

## Git Structure Example
Compact view for demo purposes.  
 ![alt text](https://github.com/BCybercell/COS301-MP-P3/blob/master/horizontal.png "GitFlow")

 
### Project Management
[Slack](https://cos301-phase3-group12.slack.com/)  
[Trello](https://trello.com/b/tbFG3ZUq/phase-3)

### Team Members
- *Deane Roos*  
- *Kyle Olivier*  
- *Richard McFadden*  
- *Tegan Carton-Barber*  

### Resources

[IOT Facial Recognition](https://us.norton.com/internetsecurity-iot-how-facial-recognition-software-works.html)  
[How Face ID Works... Probably - Computerphile](https://youtu.be/mwTaISbA87A)  
[Detecting Faces (Viola Jones Algorithm) - Computerphile](https://www.youtube.com/watch?v=uEJ71VlUmMQ&t=48s)  
[A Simple Introduction to Facial Recognition (with Python codes)](https://www.analyticsvidhya.com/blog/2018/08/a-simple-introduction-to-facial-recognition-with-python-codes/)  
[Implementing Face Detection using Python and OpenCV](https://medium.com/analytics-vidhya/how-to-build-a-face-detection-model-in-python-8dc9cecadfe9)  
[Face Recognition library](https://face-recognition.readthedocs.io/en/latest/face_recognition.html)
