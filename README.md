# Intro_To_Selfdriving_Cars
My project i've develop during the Udacity Nanodegree program: Learn the essentials of building a self-driving car, including probability, C++, machine learning, and linear algebra.

For more informations visit [Udacity.com - Intro to Self-Driving Cars - Nanodegree](https://udacity.com/course/intro-to-self-driving-cars--nd113)

# Projects
During the nanodegree there were multiple projects to plan, develop and publish for review. All projects were reviewed by Udacity mentors. When i've received ideas or tips to improve my code, i've added it to the specific project afterward.

## Joy ride
The task of this project was implementing a simple time or location based algorithm in python, which let's a virutal car (simulated in Unity3D) park parallel.

![Overview](/screenshots/car_parking_parallel.gif?raw=true)

For this project i've used both the time-based value and available x/y coordinates. The project gave a first preview of the so called jupyter notebook and working enviroment.

The juypter notebook and source code can be found in the folder called "Project_1 - Joy Ride" 


## Two dimensional histogram filter
In this project i was challenged to implement a so called "Two dimensional histogram filter" which let me localize a object in a 2D (array of arrays) world.
The main task was to implement the localizer.py and helpers.py files. 
The main parts of the algorithm are the "sense"- and "move"-function:
- sense: Try to decrease the uncertainity about the location by recalulate the location beliefs using measured-sensor-data (in this case the color of the specific field (red or green)
- move: Moves the robot to a new location (delta-x and -y). This increase the uncertainity because movement is never exact, on the other hand the next measurement will decrease the uncertainity using the previously named "sense"-function

The juypter notebook and source code can be found in the folder called "Project_2 - Two dimensional histogram filter" 
 

# About
Made with 💗 & 💻 by Kevin Hubert

More about me can be found here
- :octocat: [GitHub](https://github.com/KevinHubert-Dev) 
- 🏠 [Homepage](http://Kevin-Hubert.de/)