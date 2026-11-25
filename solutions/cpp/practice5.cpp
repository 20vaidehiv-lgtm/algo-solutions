// Problem: Longest Consecutive Sequence
// Source: https://leetcode.com/problems/longest-consecutive-sequence/
// Topic: Hash Table, Arrays
// Status: Done

#include <algorithm>
#include <climits>
#include <unordered_set>
#include <vector>

using namespace std;

int longestConsecutive(vector<int>& nums) {
    unordered_set<int> values(nums.begin(), nums.end());
    int longest = 0;

    for (int num : values) {
        long long start = static_cast<long long>(num) - 1;
        if (start >= INT_MIN && values.count(static_cast<int>(start))) {
            continue;
        }

        long long current = num;
        int length = 0;
        while (current <= INT_MAX && values.count(static_cast<int>(current))) {
            ++length;
            ++current;
        }
        longest = max(longest, length);
    }

    return longest;
}

int main() {
    return 0;
}
