/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return null;
};

target = 8;
nums = [1,2,3,4,4,5,6];
console.log(twoSum(nums, target));