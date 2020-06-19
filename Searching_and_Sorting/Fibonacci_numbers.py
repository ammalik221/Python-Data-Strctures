"""
Example of recursion in Python 3.0
"""

def fibonacci(pos):
    if pos < 0:
        print("Enter valid number (>=0)")
    elif pos == 0 or pos == 1:
        return pos
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)
    return -1
  
if __name__ == "__main__":
    print(fibonacci(9))
    print(fibonacci(1))
    print(fibonacci(27))
