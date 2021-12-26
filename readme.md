## Ex3 OOP class - ariel CS

In this assigment we were given the following interfaces:

| Interface                       | Description                                                        |
|---------------------------------|--------------------------------------------------------------------|
| GraphAlgoInterface              | This interface represents a directed weighted grpah                |
| GraphInterface                  | This interface allows us to run some basic algorithms on our graph |

We were also given an `main.py` file with some static methods to test the names of our function and some basic 
functionality.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
    - `GUI`: the folder where all the Gui related files are
- `data`: the folder which contains all of our graphs are 
- `test` : a folder with our unittests


## Testing
this project was test using the UniTest library. the tests can be run by an IDE of choice.


## Running the program
To run this project, first of all make sure you have all the dependncies:

    pip install pygame
    pip install pygame_gui

after that you can download and run the project with:

    git clone https://github.com/Daniel-Ros/OOP4.git
    cd OOP4
    python Ex3.py

## images

##  Results

These are the final results that I was able to get

| size   | algorithm        | time to finish in Millisecons |
|--------|------------------|-------------------------------|
 | 100    | shortestPath     | 45                            |
 | 100    | shortestPathDist | 26                            |
 | 100    | center           | 1703                          |
 | 1000   | shortestPath     | 45                            |
 | 1000   | shortestPathDist | 26                            |
 | 1000   | center           | 1703                          |
 | 1000   | tsp              | 36                            |
 | 10000  | shortestPath     | 342                           |
 | 10000  | tsp              | 1124                          |
 | 10000  | center           | 529873                        |
 | 100000 | isConnected      | 8095                          |
 | 100000 | shortestPath     | 5500                          |
 | 100000 | tsp              | 27946                         |
 | 100000 | center           | > 30 min                      |



## Assigment Instructions
[here](https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit)