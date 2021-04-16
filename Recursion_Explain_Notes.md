# Recursion

### [Python: RECURSION Explained - YouTube Video](https://www.youtube.com/watch?v=wMNrSM5RFMc&t=454s)

### Example:
- Find the Factorial of 5
    - The mathematical expression is `5!` 
        - The `!` stands for factorial.

Five Factorial = `5! = 1 * 2 * 3 * 4 * 5 = 120`

***Note:*** Mathematical Rules for Factorials
- `0! = 1` 
- `1! = 1`

### Algorithm to find a factorial for any number = `n!`

#### The Iterative Algorithm

```
######### Pseudocode: #########

funtion getFactorial (5)

    # First set `factorial` to 1, based on the rule above 
    #   that states 0! = 1, that is why you set the starting value at 1 
    #   and not 0. This will hold the running total
    factorial = 1
    
    # The loop to go through all the numbers in the range of 5
    for x = 1 to 5
    
        # Multiplies the prior factorial value by the current value 
        #   in the loop to increament the running total of the factorial
        factorial = factorial * x
```

#### The Recursive Algorithm

- A recursive function breaks the problem down into smaller problems, and calls itself for
each of the smaller problems.

- It includes a "base case" (or the case on which it will terminate to prevent an infinite loop) and a "recursive" (what to do each time it calls itself) case.
- Some examples of the recursive case and base case for getting the factorial of a number using recursion:

    | Factorial Algorithm | Recursive Case | Base Cases |
    | --- | --- | --- |
    | `5!` = 5 * 4 * 3 * 2 * 1 | 5 * `4!` | `0! = 1` and `1! = 1` |
    | `4!` = 4 * 3 * 2 * 1 | 4 * `3!` | `0! = 1` and `1! = 1` |
    | `3!` = 3 * 2 * 1 | 3 * `2!` | `0! = 1` and `1! = 1` |

```
Recursive Function Calls:

getFactorial(5) == 5 * getFactorial(4) --> continue...

    getFactorial(4) == 4 * getFactorial(3) --> continue...

        getFactorial(3) == 3 * getFactorial(2) --> continue...

            getFactorial(2) == 2 * getFactorial(1) --> continue...

                getFactorial(1) == Base Case --> STOP and RETURN to start, step by step

                    All function calls in the range have been stored! 
                        The base case has been reached!

Now that we have reached the base case, the function works its way 
    back up to the starting call, one function call at a time and 
        returns each value to the proper variable in the method 
            requested (i.e. either overwrites the value each time 
                or appends the value with each function call):

        factorial == 1 (the base case)
        
            factorial == 2 (!2)
            
                factorial == 6 (!3)
                
                    factorial == 24 (!4)
                    
                        factorial == 120 (!5)

So the final value returned is == 120 
```
- Open function calls until you hit your base case, return by solving each in our way back to our original function.

#### The Recursive Function will look like this:

```
######### Pseudocode #########
function getFactorial(n)

    # Define the base case to stop the function calls
    if n < 2, return 1
    
    # If the base case defined above has not been reached
    else 
    
    # Do this until base case has hit and store values
    return n * getFactorial(n-1)
```

## Recursion Pros & Cons 

Typically, no calculations are done until the base case is reached.

So for very large problems (millions of recursive calls) you may run out of memory since you'll have millions of open function calls.

`1,0000,000! = 1,000,000 * 999,999!`   Now Find 999,999!

`999,999! = 9999,999 * 999,998!`  Now Find 999,998!

### Cons: 
1. Does not scale up like iteration. Requires more memory.
2. In many languages iterative solutions are way faster.
3. Sometimes recursion is a little more abstract or harder to understand than iterative solutions.

### Pro:
1. In some cases extremely fast and easy to code.
2. Extremely practical for tree traversals, binary search and graphs.

## The Code:
```
# Recursive solution for getting the Factorial of a number
def get_recursive_factorial (n):
        # Check for edge case of a negitive number
        if n < 0:
            return -1
        
        # Set the base case
        elif n < 2:
            return 1
        
        # Recursively call the function 
        #   until reaching the base case
        else:
            return n * get_recursive_factorial (n-1)

print("6! recursive",get_recursive_factorial(6))
OUTPUT --> 720
```
---
```
# Iterative solution for getting the Factorial of a number
def get_iterative_factorial(n):
    # Check for edge case of negitive number
    if n < 0:
        return -1

    # Iteratively get the factorial
    else:
        # Set variable for resulting factorial value
        #   Starting at 1 (lowest possible value)
        fact = 1
        
        # Iterate through the range of the number passed in
        for i in range(1, n+1):
            # For each value from 1 to n 
            # Multiple current factorial value by i (current value)
            fact *= i
        
        # Return the resulting value after iteration completes
        return fact

print("6! iterative",get_iterative_factorial(6))
OUTPUT --> 720
```
