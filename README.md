# Peek Finder in Python
## Problem
This is the python version of repository <a href="Peek Finder in Java">https://github.com/ahmadsedi/peek_finder</a><br>
Given a list of integers -representing for example series of weather temperature in one area- we need a function to find the 'peek' number. 
A number is called a peek, if the difference between that number and its 
previous number is the greatest in the series. For example in array of {1, 2, 5, 6} the peek is happening at index 2, 
because at index 2 we have 5 which is 3 more than the index 1 that is 2.
Examples: <br>
[1, 2, 5, 6] -> 2 <br>
[3, 4, 1] -> 1 <br>
[1] -> 0 <br>
[] -> -1 <br>

## Setup/Requirements
* python3 -m venv .venv
* source .venv/bin/activate
* pip install pytest
