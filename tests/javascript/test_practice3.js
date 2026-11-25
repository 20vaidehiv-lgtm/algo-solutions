const assert = require("assert");
const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(
  path.join(__dirname, "..", "..", "solutions", "javascript", "practice3.js"),
  "utf8"
);
const twoSum = new Function(src + "\nreturn twoSum;")();

assert.deepStrictEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
assert.deepStrictEqual(twoSum([3, 2, 4], 6), [1, 2]);
assert.deepStrictEqual(twoSum([3, 3], 6), [0, 1]);
assert.deepStrictEqual(twoSum([1, 2, 3], 10), []);

console.log("practice3 Two Sum: all cases passed");

