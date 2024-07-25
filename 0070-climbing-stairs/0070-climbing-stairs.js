/**
 * @param {number} n
 * @return {number}
 */


var climbStairs = function(n) {
    let dictionary = {};
    return f(n , dictionary);
};

const f = (n, dictionary) => {
    if (n < 3) return n;
    if (dictionary[n]) return dictionary[n];

    dictionary[n] = f(n - 1, dictionary) + f(n - 2, dictionary);
    return dictionary[n];
}