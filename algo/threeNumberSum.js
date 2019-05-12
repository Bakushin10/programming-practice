function threeNumberSum(array, targetSum){
    //sort the array
    array.sort((a,b) => a - b);
    const ans = []
    for(let i = 0; i < array.length; i++){
        let left = i + 1;
        let right = array.length - 1
        while(left < right){
            sumTotal = array[i] + array[right] + array[left]
            if (sumTotal == target){
                ans.push([array[i], array[right], array[left]])
                left ++;
            }
            else if (sumTotal < targetSum){
                left ++;
            }else if (sumTotal > targetSum){
                right -- ;
            }
        }
    }
    return ans
}

target = 0
array = [12,3,1,2,-6,5,-8,6]

console.log(threeNumberSum(array, target))