# COURSE 4: PYTHON FOR DATA SCIENCE
## Week1: Python Basics
## Week2: Python Data Structures
## Week3:Python Programming Fundamentals
### Part 1:Conditions and Branching
##### Condition Statements
###### Inequality and equality operator
We can apply the inequality and equality operator on strings, interger, numeric...
```js
#Output False
"ACDC" == "Michael Jackson"

#Output True
"ACDC" != "Michael Jackson"
```
These operations are also used to compare the letters/words/symbols according to the ASCII value of letters.
Note: Upper Case Letters have different ASCII code than Lower Case Letters, which means the comparison between the letters in Python is case-sensitive.

##### if, else, elif statement

```js 
# example
# Output:go see Pink Floyd    move on
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")
```


##### Logical operators: not, Or, And


### Part 2: Loops
#### Range
It is helpful to think of the range object as an ordered list

#### For
The for loop enables you to execute a code block multiple times.
```js 
# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
```
This code block will return 1982 1980 1973

In Python we can directly access the elements in the list as follows:
```js
for year in dates:  
    print(year)   
```
We can change the elements in a list:
```js
# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
```
We can access the index and the elements of a list as follows:
```js
# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
```
#### While
With for, we dont know when we want to stop the loop. With While, we use a condition to stop our program. The code block will keep being executed until the given logical condition returns a False boolean value.

A while loop iterates merely until the condition year != 1973 is not met
```js 
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
```
Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop
```js
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    Rating = PlayListRatings[i]
    print(Rating)
    i = i + 1
 ```
 Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange'
    
 ```js 
 squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
```
### Part 3: Functions in Python
A function is a reusable block of code which performs operations specified in the function

```js
# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    
result = Mult(12,2)
print(result)

# Use mult() multiply two floats
Mult(10.0, 3.14)

# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")
```

If there is no return statement, the function returns None.
```js
# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)
```
#### Default argument values

```js 
# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)
```
```js 
# Test the value with default value and with input

isGoodRating()
isGoodRating(10)
#this album sucks it's rating is 4
#this album is good its rating is 10
```


