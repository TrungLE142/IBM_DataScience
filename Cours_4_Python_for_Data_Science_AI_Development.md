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

When the number of arguments are unknown for a function, They can all be packed into a tuple:
```js 
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')
```

The arguments can also be packed into a dictionary as shown:
```js
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
```
Output 
Country : Canada
Province : Ontario
City : Toronto

Can the function be used to concatenate lists or tuples?
```js
# Write your code below and press Shift+Enter to execute
l1= [1,2,3,4]
l2 = [5,6,7,8]
con(l1,l2)
# output: [1, 2, 3, 4, 5, 6, 7, 8]
```
### Part 4:Exception Handling

Some exemples for ErrorException
- 1/0 => ZeroDivisionError occurs when you try to divide by zero.
- y = a + 5 => NameError: it means that you tried to use the variable a when it was not defined.
-  a = [1, 2, 3]   then  a[10]   => IndexError: it occured because you tried to access data from a list using an index that does not exist for this list.

#### Try Except
```js
# potential code before try catch
try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception
```
Exemple: 
```js
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
```
If the input b is 0, the exception will be raised => "There was an error"
When  b= 2 , we obtain Success a = 0.5

#### Try Except Specific Example
We can define the excepts specific for the different cases
```js
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
```
"finally" allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except.
```js
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
```

### Part 5: Classes and Objects in Python

```js
# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
```
    Creating an instance of a class Circle
```js
    # Create an object RedCircle
    RedCircle = Circle(10, 'red')
    # affiche la value radius
    RedCircle.radius
    #affiche la value color
    RedCircle.color
    
    #We can change the object's data attributes:
    # Set the object attribute radius
    RedCircle.radius = 1
    
    # Use method to change the object attribute radius

    print('Radius of object:',RedCircle.radius)
    RedCircle.add_radius(2)
    print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
    
    # Call the method drawCircle
    RedCircle.drawCircle()
```
### Exercises for this chapiter
Create a classe 'analysedText' that can perform analysis on a given piece of text. Complete this class with the following methods 

- Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
- freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
- freqOf - returns the frequency of the word passed in argument.

```js
class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        text1 = text.replace('.' , '').replace('!' , '').replace(',' , '').replace('?' , '')
        # convert into lowercase
        self.fmtText = text1.lower()
        
    def freqAll(self):        
        new_dict= {}
        # split text into words to create a new list with this words
        new_list = self.fmtText.split(' ')
        # convert this new_list into new_set to remove the duplicate
        new_set = set(new_list)
        # use loop for to read each element in set and add them into the new dictionary with their numbers of apperances.
        for word in new_set :
            new_dict[word] = new_list.count(word)
        return new_dict
    
    def freqOf(self,word):
        # split text into words to create a new list with this words
        list = self.fmtText.split(' ')
        # variable to take the nb of occurence.
        freqword = 0
        for i in list:
            if i == word:
                freqword = list.count(i)
        return freqword    
```
