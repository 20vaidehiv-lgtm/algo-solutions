// Problem: Longest Common Subsequence
// Source: https://leetcode.com/problems/longest-common-subsequence/
// Topic: Dynamic Programming, String
// Status: ✅ Done

function longestCommonSubsequence(text1, text2) {
  const m = text1.length;
  const n = text2.length;

  // dp[i][j] = LCS length of text1[0..i) and text2[0..j)
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[m][n];
}

