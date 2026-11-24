// Checks solutions/javascript/practice6.js (Longest Common Subsequence).
const assert = require("assert");
const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(
  path.join(__dirname, "..", "..", "solutions", "javascript", "practice6.js"),
  "utf8"
);
const longestCommonSubsequence = new Function(src + "\nreturn longestCommonSubsequence;")();

const cases = [
  ["abcde", "ace", 3],
  ["abc", "abc", 3],
  ["abc", "def", 0],
  ["", "abc", 0],
  ["abc", "", 0],
  ["bl", "yby", 1],
  ["oxcpqrsvwf", "shmtulqrypy", 2],
];

for (const [text1, text2, expected] of cases) {
  const actual = longestCommonSubsequence(text1, text2);
  assert.strictEqual(actual, expected, `LCS(${text1}, ${text2}) expected ${expected} but got ${actual}`);
}

console.log("practice6 LCS: all cases passed");
