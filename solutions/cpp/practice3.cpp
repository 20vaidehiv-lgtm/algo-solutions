// Problem: Move Zeroes
// Source: https://leetcode.com/problems/move-zeroes/
// Topic: Two Pointers, Arrays
// Status: Done

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
    return 0;
}
