// Note: solutions/javascript/practice7.js is currently marked IN PROGRESS.
const assert = require("assert");
const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(
  path.join(__dirname, "..", "..", "solutions", "javascript", "practice7.js"),
  "utf8"
);
const merge = new Function(src + "\nreturn merge;")();

assert.deepStrictEqual(
  merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
  [[1, 6], [8, 10], [15, 18]]
);
assert.deepStrictEqual(merge([[1, 4], [4, 5]]), [[1, 5]]);
assert.deepStrictEqual(merge([[1, 4], [2, 3]]), [[1, 4]]);

console.log("practice7 Merge Intervals: all cases passed");

