# Recursion for Beginners: 

### [Recursion for Beginners: A Beginner's Guide to Recursion - YouTube Video](https://youtu.be/AfBqVVKg4GE)

- Automate the Boring Stuff with Python  
    By: Al Sweigart (Presenter in Video)

- [Link to Slides used in the Presentation](https://docs.google.com/presentation/d/149zzXcV_34DIZ50OJIfau1L0GDpMvc9VDk2szPVELsI/edit#slide=id.g469f1aa928_0_97)

### [Al's Recursion Examples on GitHub](https://github.com/asweigart/recursion_examples)

## Sierpinski Triangle (Example of Recursion)
![](https://xtrp.io/api/content/static_files/generating-the-sierpinski-triangle-in-vanilla-javascript-with-html5-canvas-with-some-mathematical-background/fractal.jpg)

[Python code to Recreate the above Image](https://github.com/asweigart/recursion_examples/blob/master/sierpinskiTriangle.py)

## Recursion in  Programming

In programming, recursion is when a function calls itself.

If you really want to understand recursion, you must first understand "Stacks"!

- `Stack`: A data structure that holds a sequence of data and only lets you interact with the topmost item.
    - Can think of a `Stack` like a stack of playing cards or pancakes
        - The one on the top always gets removed first
    - So a `Stack` is a `First-In, Last-Out (FILO)` or `Last-In, First-Out (LIFO)` data structure.
    - Adding to the top of the `Stack` is called **pushing**
        - In Python, this would be `.append()`
    - Removing from the `Stack` is called **popping**
        - In Python, this would be `.pop()`

## How Function Calls Work
- When you call a ***function inside another function***, each function called with be added to a stack internally.

- ***Once the last function is reached***, the computer goes back through the *"call stack"* and preforms each function one-by-one in the order each function was called, *starting with the most recent* and working its way *back to the first one called*.

- Therefore, ***function calls*** are similar to the way that recursion operates.

**Example:**

```
### Simple Functions to Explain Call Stacks ###
# Define function `a`
def a():
    # Print the start of function `a` to console
    print('Start of a()')
    # Call on function `b`
    b()
    # Print the end of function `a` to console
    print('End of a()')

# Define function `b`
def b():
    # Print the start of function `b` to console
    print('Start of b()')
    # Call on function `c`
    c()
    # Print the end of function `b` to console
    print('End of b()')

# Define function `c`
def c():
    # Print the start of function `c` to console
    print('Start of c()')
    # Print the end of function `c` to console
    print('End of c()')

# Call function `a` to start the call stack
a()

######### OUTPUT ########
Start of a()  # First, adds function `a` to the call stack
Start of b()  # Then, adds function `b` to the call stack
Start of c()  # Lastly, adds function `c` to the call stack
End of c()  # First, completes function `c`
End of b()  # Then, completes function `b`
End of a()  # Lastly, completes function `a`
```

![Image of the code above](https://raw.githubusercontent.com/jmmiddour/CSPT19/main/Recusion_for_Beginners/call_stack_example.jpg?token=APLSS6MKQ3HJIGXEOJUUT3TAQNFVA)

In Python, there is a limit of `1000` function calls  by default before you go into "stack overflow". At that point you will end up getting an error `RecursionError: maximum recursion depth exceeded`.
- This is the reason that you have to always have at least one "base case" and one "recursive case".

**Factorial Recursive Example:**

[Factorial Recursive Code](https://github.com/asweigart/recursion_examples/blob/master/factorialByRecursion.py)

![Factorial Recursive Example](https://raw.githubusercontent.com/jmmiddour/CSPT19/main/Recusion_for_Beginners/factorial_example.jpg?token=APLSS6O3NXA657KWW63TPCTAQNG4S)

[Factorial Emulating Recursive Function using Iteration](https://github.com/asweigart/recursion_examples/blob/master/factorialEmulateRecursion.py)

### When Should you use Recursion?

- When the problem has a tree-like structure.
- When the problem requires backtracking. Such as traversing trees, graphs, and/or linked lists

Otherwise, you do not have to use recursion

### Tail Call Optimization/Elimination

What if the problem is big enough that it really does require more than 1000 functions calls? Such as `factorial(1001)`.

In code, "tail call optimization/elimination" is when the recursive function call is the last thing in the function before it returns:

```
def recursiveFunc(params):
    # blah blah blah
    return recursiveFunc(params) # RECURSIVE CASE
```

(The recursive function call comes at the “tail” of the function.)

You won’t need to hold on to local variables, because there’s no code after the recursive function call that will need them.

There is no need to keep the frame object on the call stack. Which means that the call stack never grows in size.

You can go beyond 1000 function calls because the call stack isn’t growing.

TCO prevents stack overflows.

[Factorial Tail Call Optimization Code](https://github.com/asweigart/recursion_examples/blob/master/factorial_tailCallOptimization.py)

Tail call optimization is a compiler trick. However, CPython (the Python compiler) doesn't implement it, and it never will.

**You can not use Tail Call Optimization in Python**

## Fibonacci Sequence

### Recursive

```
def fib(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        # BASE CASE
        return 1
    else:
        # RECURSIVE CASE
        return fib(nthNumber - 2) + fib(nthNumber - 1)
```

- The above code is not very efficient because it is actually repeating itself several times when not needed, "under the hood"

![Image of what the above code is doing under the hood](https://raw.githubusercontent.com/jmmiddour/CSPT19/main/Recusion_for_Beginners/fibonacci_recursive_visualization.jpg?token=APLSS6NDB57HU7GSWMNGPK3AQNKWK)

### Recursive using MEMOIZATION

```
# Creates a cache to hold the values already calculated
FIB_CACHE = {}

def fib(nthNumber):
    # If the value is already in the cache, no need to re-calculate it
    if nthNumber in FIB_CACHE:
        return FIB_CACHE[nthNumber]

    # This is the BASE CASE
    if nthNumber == 1 or nthNumber == 2:
        return 1
    
    else:
        # RECURSIVE CASE
        FIB_CACHE[nthNumber] = fib(nthNumber - 2) + fib(nthNumber - 1)
        return FIB_CACHE[nthNumber]
```

- By using "memoization" you can keep the code DRY under the hood as you can see in the image below.

![Fibonacci Recursive with Memoization](https://raw.githubusercontent.com/jmmiddour/CSPT19/main/Recusion_for_Beginners/fibonacci_recursive_memoization.jpg?token=APLSS6LA2G6JMLQJHZOS53LAQNK5Y)

Another way to use "memoization" is with a built-in function in Python in the `functools` library using a `lru_cache` (LRU: Least Recently Used):

```
import functools

@functools.lru_cache()
def fib(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        # BASE CASE
        return 1
    else:
        # RECURSIVE CASE
        return fib(nthNumber - 2) + fib(nthNumber - 1)
```
