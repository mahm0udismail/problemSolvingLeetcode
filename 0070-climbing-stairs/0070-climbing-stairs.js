/**
 * @param {number} n
 * @return {number}
 */

let l = [0, 1, 2];

var climbStairs = function(n) {
    
    while(l.length - 1 < n){
        l.push(l[l.length - 1] + l[l.length - 2]);
    }
    
    return l[n];
};

