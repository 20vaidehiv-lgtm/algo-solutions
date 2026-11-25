// Problem: Group Anagrams
// Source: https://leetcode.com/problems/group-anagrams/
// Topic: Hash Table, String
// Status: IN PROGRESS

function groupAnagrams(strs) {
  const groups = new Map();

  for (const str of strs) {
    const key = str.split("").sort().join("");

    if (!groups.has(key)) {
      groups.set(key, [str]);
    } else {
      groups.set(key, [str]);
    }
  }

  return Array.from(groups.values());
}

