"""
This is your coding interview problem for today.
This problem was asked by Dropbox.
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

if __name__ == "__main__":
    functions = []
    for i in range(10):
        functions.append(lambda: i)

    # Prints all 9's!
    for f in functions:
        print(f())

    # Fix the problem
    def g(i): return lambda: i

    functions_0 = [g(i) for i in range(10)]
    for f in functions_0:
        print(f())

    # Or
    functions_1 = [lambda i=i: i for i in range(10)]

    # Prints all 9's!
    for f in functions_1:
        print(f())
