import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import path from "node:path";

const solutionPath = path.join(import.meta.dirname, "..", "..", "solutions", "typescript", "practice1.ts");
const output = execFileSync(process.execPath, ["--experimental-strip-types", solutionPath], {
  encoding: "utf8",
});
assert.ok(output.includes("All 9 test cases passed!"), `Unexpected output: ${output}`);
console.log("practice1 TypeScript Valid Parentheses: passed");

