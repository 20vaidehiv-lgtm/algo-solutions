const assert = require("assert");
const { execFileSync } = require("child_process");
const path = require("path");

const solutionPath = path.join(__dirname, "..", "..", "solutions", "javascript", "practice2.js");

const cases = [
  ["521", "Sum: 4"],
  ["111", "Sum: 1"],
  ["886996", "Sum: 0"],
  ["9", "Sum: 9"],
];

for (const [input, expected] of cases) {
  const output = execFileSync(process.execPath, [solutionPath], {
    input: `${input}\n`,
    encoding: "utf8",
  });
  assert.ok(output.includes(expected), `Input ${input}: expected "${expected}" in "${output.trim()}"`);
}

console.log("practice2 Alternating Digit Sum: all cases passed");

