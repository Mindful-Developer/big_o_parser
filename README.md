This library will be for time and space optimization analysis using Big O notation.

Complexity Analysis (Big O):
-
- Simple decorator user syntax that can be attached to any function or class to check complexity of function or functions within class.
  

- Attached to a function:
    - returns a formatted string. 
    - string will contain each line of the function followed by each line's complexities.
    - give entire functions complexity after the function
    

    Example output:
    
    @complexity                    time    space
    def linear_algo_2(items):      O(1)     O(1)
        total = 0                  O(1)     O(1)
        for item in items:         O(n)     O(n)
            total += item          O(1)     O(1)
        for item in items:         O(n)     O(n)
            total += item          O(1)     O(1)
        return total               O(1)     O(1)

                                   time    space
    ---------------------------------------------
    linear_algo_2(items)           O(n)     O(n)


- Attached to a class:
    - does function analysis on each function in the class
    - (maybe) class mapping (show how functions within a class are mapped to each other) (2nd tool?)


 
    
    