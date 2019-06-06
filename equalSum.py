def equalSum(array):

    current_sum = []
    total = sum(array)
    equSumHelper(array, current_sum, total)

def equSumHelper(array, current_sum, total):
    if sum(current_sum) == total - sum(current_sum):
        print(current_sum)
        return
    for i in range(len(array)):
        newArray = array[i+1:]
        cs = current_sum + [array[i]]
        equSumHelper(newArray, cs, total)

array = [15, 5, 20, 10, 35, 15, 10]
equalSum(array)