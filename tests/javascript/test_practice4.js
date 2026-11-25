// Note: solutions/javascript/practice4.js is currently marked IN PROGRESS.
const assert = require("assert");
const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(
  path.join(__dirname, "..", "..", "solutions", "javascript", "practice4.js"),
  "utf8"
);
const groupAnagrams = new Function(src + "\nreturn groupAnagrams;")();

const normalize = (groups) =>
  groups.map((g) => [...g].sort()).sort((a, b) => a.join(",").localeCompare(b.join(",")));

assert.deepStrictEqual(
  normalize(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
  normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
);
assert.deepStrictEqual(groupAnagrams([""]), [[""]]);
assert.deepStrictEqual(groupAnagrams(["a"]), [["a"]]);

console.log("practice4 Group Anagrams: all cases passed");

