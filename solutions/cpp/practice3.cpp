// Problem: Move Zeroes
// Source: https://leetcode.com/problems/move-zeroes/
// Topic: Two Pointers, Arrays
// Status: Done

#include <cassert>
#include <vector>

using namespace std;

void moveZeroes(vector<int>& nums) {
    int insertPos = 0;

    for (int num : nums) {
        if (num != 0) {
            nums[insertPos++] = num;
        }
    }

    while (insertPos < static_cast<int>(nums.size())) {
        nums[insertPos++] = 0;
    }
}

int main() {
    vector<int> nums1 = {0, 1, 0, 3, 12};
    moveZeroes(nums1);
    assert((nums1 == vector<int>{1, 3, 12, 0, 0}));

    vector<int> nums2 = {0};
    moveZeroes(nums2);
    assert((nums2 == vector<int>{0}));

    vector<int> nums3 = {};
    moveZeroes(nums3);
    assert(nums3.empty());

    vector<int> nums4 = {1, 2, 3};
    moveZeroes(nums4);
    assert((nums4 == vector<int>{1, 2, 3}));

    vector<int> nums5 = {0, 0, 0};
    moveZeroes(nums5);
    assert((nums5 == vector<int>{0, 0, 0}));

    vector<int> nums6 = {1, 0, 2, 0, 3, 0};
    moveZeroes(nums6);
    assert((nums6 == vector<int>{1, 2, 3, 0, 0, 0}));

    return 0;
}
