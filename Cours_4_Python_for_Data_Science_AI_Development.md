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
##### Range¶
It is helpful to think of the range object as an ordered list

##### For
The for loop enables you to execute a code block multiple times.
```js 
# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
```
This code block will return 1982 1980 1973
