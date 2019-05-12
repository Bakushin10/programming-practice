function twoNumberSum(array, targetSum){
    const complement = {}

    for(const num of array){
        comp = targetSum - num
        if(complement[num]){
            return [num, comp]
        }else{
            complement[comp] = true
        }
    }
    return []
}

inp = [3,5,-4,8,11,1,-1,6]
target = 10
console.log(twoNumberSum(inp, target))