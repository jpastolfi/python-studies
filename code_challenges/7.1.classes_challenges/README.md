Challenges
You have decided to use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are able to pick up and deliver objects was promising and now you want to start programming the logic. These code challenges will use your knowledge of Classes to solve some example scenarios. Try solving the five challenge problems below!

1. Setting Up Our Robot
Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of important data related to the robot.

2. Adding Robot Logic
Now we want to add some logic to our robot. It would be very useful to be able to control our robot, so we are going to create a control_bot method which changes the speed and direction. We are also going to create a method called adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles.

3. Enhanced Constructor
It can be tedious manually setting the values for each instance variable after we have created an object from the DriveBot class. We can enhance our constructor to automatically assign the values we provide to the instance variables. Instead of taking zero parameters, we are going to make the constructor take three parameters. 

4. Controlling Them All
We want to add a new feature that allows the user to control multiple robots at once. The robots should be able to all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all called all_disabled. We can accomplish this using class variables.

5. Identifying Robots
In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it is created. If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. This can be accomplished by using a class variable counter which increments and is assigned to an instance variable for the ID whenever the constructor is called. 