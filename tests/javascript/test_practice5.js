const assert = require("assert");
const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(
  path.join(__dirname, "..", "..", "solutions", "javascript", "practice5.js"),
  "utf8"
);
const maxSubArray = new Function(src + "\nreturn maxSubArray;")();

assert.strictEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
assert.strictEqual(maxSubArray([1]), 1);
assert.strictEqual(maxSubArray([5, 4, -1, 7, 8]), 23);
assert.strictEqual(maxSubArray([-3, -2, -5]), -2);

console.log("practice5 Maximum Subarray: all cases passed");

