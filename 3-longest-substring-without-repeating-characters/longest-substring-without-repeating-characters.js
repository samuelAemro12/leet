/**
 * @param {string} s
 * @return {number}
 */
//  the longest substring should be a no duplicate charachters
var lengthOfLongestSubstring = (x) =>{
    var count = 0;
    var charSet = new Set();
    var j = 0;
    for(i=0; i< x.length; i++){
        while (charSet.has(x[i])){
            charSet.delete(x[j]);
            j++;
        }
        charSet.add(x[i]);
        count =Math.max(count, i - j +1);
        }
    
    return count;
}
var x = "asdgergtewrgrgrtgtrmk";
console.log(lengthOfLongestSubstring(x));