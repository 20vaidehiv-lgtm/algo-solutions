// Problem: Longest Consecutive Sequence
// Source: https://leetcode.com/problems/longest-consecutive-sequence/
// Topic: Hash Table, Arrays
// Status: Done

#include <algorithm>
#include <cassert>
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
    vector<int> nums1 = {100, 4, 200, 1, 3, 2};
    assert(longestConsecutive(nums1) == 4);

    vector<int> nums2 = {};
    assert(longestConsecutive(nums2) == 0);

    vector<int> nums3 = {0};
    assert(longestConsecutive(nums3) == 1);

    vector<int> nums4 = {1, 2, 0, 1, 3, 2};
    assert(longestConsecutive(nums4) == 4);

    vector<int> nums5 = {-3, -2, -1, 0, 1};
    assert(longestConsecutive(nums5) == 5);

    vector<int> nums6 = {INT_MIN, INT_MIN + 1, INT_MAX};
    assert(longestConsecutive(nums6) == 2);

    return 0;
}
