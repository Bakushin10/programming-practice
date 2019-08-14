def minNumberOfJumps(array):
    # Write your code here.
    currentJump, i, current = 0, 0, 0
    minJump = float("inf")
    #for current in range(1, array[0]):
    minJump = min(minJump, minNumberOfJumpsHelper(array, current, i, array[current], currentJump, float("inf")))
    return minJump

def minNumberOfJumpsHelper(array, current, i, loop, currentJump, jump):
    if current > len(array): return
    if current == len(array) - 1:
        if currentJump < jump:
            jump = currentJump
            print(jump)
        return jump
    loop = array[current]
    
    while i <= loop and i + current < len(array):
        jump = minNumberOfJumpsHelper(array, current + i, 1, 0, currentJump + 1 ,jump)
        i += 1
    return jump

inp = [3,4,2,1,2,3,7,1,1,1]
inp = [5,1,1]
inp = [2, 1, 2, 3, 1, 1, 1]
print(minNumberOfJumps(inp))