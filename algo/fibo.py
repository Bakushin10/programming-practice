import sys

def fibonacci():
    line = sys.stdin.readline()

    """ check the input """
    line = line.split()
    if len(line) != 3:
        return "takes 3 inputs"

    try:
        """ check if all 3 inputs are integer """
        val1 = int(line[0])
        val2 = int(line[1])
        val3 = int(line[2])
    except:
        return "input onlt takes integer"

    return fibonacciHelper(int(line[0]), int(line[1]), int(line[2]), 3)

def fibonacciHelper(a1, a2, target, current):

    if target == 1:
        return a1
    if target == 2:
        return a2
    if target == current:
        return a1 + a2
    else:
        """
        recursively update the input
        we know next a3 = a1 + a2 so update accordingly
        update the current
        """
        return fibonacciHelper(a2, a1 + a2, target, current + 1)

print(fibonacci())
