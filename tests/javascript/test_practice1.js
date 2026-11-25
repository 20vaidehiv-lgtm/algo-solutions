const assert = require("assert");
const { isValid } = require("../../solutions/javascript/practice1");

const cases = [
  ["()", true],
  ["()[]{}", true],
  ["(]", false],
  ["([])", true],
  ["([)]", false],
  ["{[]}", true],
  ["", true],
  ["(", false],
];

for (const [input, expected] of cases) {
  assert.strictEqual(isValid(input), expected, `isValid(${JSON.stringify(input)})`);
}

console.log("practice1 Valid Parentheses: all cases passed");

