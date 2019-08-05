# Intro_To_Selfdriving_Cars
My project i've develop during the Udacity Nanodegree program: Learn the essentials of building a self-driving car, including probability, C++, machine learning, and linear algebra.

For more informations visit [Udacity.com - Intro to Self-Driving Cars - Nanodegree](https://udacity.com/course/intro-to-self-driving-cars--nd113)

# Projects
During the nanodegree there were multiple projects to plan, develop and publish for review. All projects were reviewed by Udacity mentors. When i've received ideas or tips to improve my code, i've added it to the specific project afterward.

## Joy ride
The task of this project was implementing a simple time or location based algorithm in python, which let's a virutal car (simulated in Unity3D) park parallel.

![Parallel_Parking_Project_GIF](/screenshots/car_parking_parallel.gif?raw=true)

For this project i've used both the time-based value and available x/y coordinates. The project gave a first preview of the so called jupyter notebook and working enviroment.

The juypter notebook and source code can be found in the folder called "Project_1 - Joy Ride" 


## Two dimensional histogram filter
In this project i was challenged to implement a so called "Two dimensional histogram filter" which let me localize a object in a 2D (array of arrays) world.
The main task was to implement the localizer.py and helpers.py files. 
The main parts of the algorithm are the "sense"- and "move"-function:
- sense: Try to decrease the uncertainity about the location by recalulate the location beliefs using measured-sensor-data (in this case the color of the specific field (red or green)
- move: Moves the robot to a new location (delta-x and -y). This increase the uncertainity because movement is never exact, on the other hand the next measurement will decrease the uncertainity using the previously named "sense"-function

The juypter notebook and source code can be found in the folder called "Project_2 - Two dimensional histogram filter" 
 

## Matrix class (python)
Project 3 was about implementing a matrix-class using python. The class contains a matrix-class which can be used to do the following mathematical caluclations with the created matrix-objects:

- dot product
- determinant (for 1x1 and 2x2 matrices)
- trace
- inverse
- transpose
- add
- substract
- negate
- multiply (with constant)
- multiply with other matrix)

Afterwards the matrix-class was used to implement the kalman-filter for movement predictions in 2D-world (array of arrays).

The juypter notebooks and source code can be found in the folder called "Project_3 - Matrix class (python)"


## Translate Python to C++
After implementing the histogram-filter in project 2, this following project focus on implementing the same functionality in c++ instead of python.
This was done to show the differences (mainly: code-complexity vs. run-time) of the two language. 

Just by implemeting the same functionality to c++ a major run-time impact could be measured on the other hand the code is much more complexe.

The source code can be found in the folder called "Project_4 - Translate Python to C++"

The code uses c++11 functionality.

The following commands can be used to run the code

Run tests
``` Shell
g++ -std=c++11 -o test.exe tests.cpp
./test.exe

# Example output:
# ! - normalize function worked correctly!
# ! - blur function worked correctly!
# ! - initialize_beliefs function worked correctly!
# ! - move function worked correctly with zero blurring
# ! - sense function worked correctly
```

Run simulate
``` Shell
g++ -std=c++11 simulate.cpp
```

> **Info from Udacity**: There's one last item to note here - if you try to run tests.cpp, it actually uses the Simulation class from this file, and so trying to run tests.cpp while the main() function within simulate.cpp is uncommented will result in an error! In order to do so, the first step is to uncomment all the lines at the bottom of the file (simulate.cpp) around the main() function.

## Implementing a Route planner
Route planning is a big thing in navigation and navigation is essentially for self-driving cars. In the project of the course, i was challenged to implement different types of path-finding algorithms. There are multiple classes like
- Depth-first
- Breadth-first
- Cheapest-first
they have advantages and disadvantages.


![Binary_Tree_Search-Breath-_Vs_Depth_First](screenshots/binary_tree_search.png?raw=true)
Image source - http://mishadoff.com/blog/dfs-on-binary-tree-array/

At the end of the lecture the project was to implement the so called "A*" (spoken: A-Star) algorithm which is a path-finding algorithm of the class "Cheapest-first" which ensures to find the lowest cost for the specific path, if a solution exists.

The A* algorithm is a so called informed search algorithm because next to the known cost of the path to the next node it uses heuristics to estimate the futhermore costs . The heuristics makes the A* algorithm more efficient compares to breadth-first algorithms.

My implementation of the A* algorithm can be found by openening the project folder called "Project_5 - Implement Route Planner

## Reconstructing Trajectories
The information with can be measured with different sensor can be very rich of more complex informations, which can be calculated by the given informations
Example:
- Time and Acceleration give informations about a speed
- Time and Speed can give informations of distance traveld
- Distance traveled and speed can be backward caluclated to the elapsed time
- and so on...

As an example this project provided just four different types of measured values: time, displacement, yaw-rate and acceleration.
Based on the given information it was my task to find out the line/curve traveled by the car in different situations (different datasets).

This projects mainly contains trigonometry and derivatives.
The given datasets and task including my solution (Reconstructing Trajectories.ipynb) can be found in the folder called "Project_6 - Reconstructing Trajectories"


## Traffic Light Classifier
At the end of the nanodegree there was a lecture about machine learning and computer vision. The task for this project was the following:
> use your knowledge of computer vision techniques to build a classifier for images of traffic lights! You'll be given a dataset of traffic light images in which one of three lights is illuminated: red, yellow, or green.

The project contains multiple steps to solve the problem:

1.) Loading and visualizing data

2.) Preprocessing - standardize, even the input and the results

3.) Feature extraction - get information of standardized images

4.) Classification - Classify the input based on the feature extraction

5.) Evaluate - Increase the accurarcy, analyse problems and find better fitting solutions

To pass the project and finish the nanodegree, i had to have a accurancy >90% and the algorithm was not allowed to classify a red traffic light as a green one.

In the end my solution reached an accurany of ~97.0%
In the jupyter-notebook are some notes of mine about ideas how to improve the code to reach a higher accurancy. 

Information: To reduce the size of the repository, i've decided to not upload all +1000 traffic-light picture from the course. Instead i've picked 3-5 from each traffic-light-classification-class (red, yellow, green) from both given datasets: training and test.

All of the image have different sizes, ratio-aspect and a different quality (hue, startion and brightness)

Here are some examples:

![Traffic_Light_Example_Images](Project_7&#32;-&#32;Traffic-Light-Classifier/images/all_lights_small.png?raw=true)



# Conclusion 

I am really happy that i've successfully completed all projects in the given time and learned all the required skills to do so. Due to the reviews made by Udacity-Mentors i've got additional inspirations and feedback, what parts of my projects were good and where (and especially how) i could do better.

I'm looking forward to enroll the next nanodegree "Become a Self-Driving Car Engineer", which is based on the "Intro to Self-Driving-Cars" nanodegree i've completed now.

To get an insight into the world of self-driving-cars and their technological basics, I can recommend the Nanodegree to everyone.


If you interested in more informations about the course or have any questions feel free the get in touch with me.

# About
Made with 💗 & 💻 by Kevin Hubert

More about me can be found here
- :octocat: [GitHub](https://github.com/KevinHubert-Dev) 
- 🏠 [Homepage](http://Kevin-Hubert.de/)