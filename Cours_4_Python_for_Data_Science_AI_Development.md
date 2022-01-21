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
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")
```
Output: 
go see Pink Floyd
move on

##### Logical operators: not, Or, And

