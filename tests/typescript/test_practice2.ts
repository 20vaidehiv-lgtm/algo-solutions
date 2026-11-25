import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import path from "node:path";

const solutionPath = path.join(import.meta.dirname, "..", "..", "solutions", "typescript", "practice2.ts");
const output = execFileSync(process.execPath, ["--experimental-strip-types", solutionPath], {
  encoding: "utf8",
});
assert.ok(output.includes("All 3 Two Sum TypeScript test cases passed!"), `Unexpected output: ${output}`);
console.log("practice2 TypeScript Two Sum: passed");

