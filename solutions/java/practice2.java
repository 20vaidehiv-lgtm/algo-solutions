// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum/
// Note: Use a hash map to store seen values and find complements in one pass

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }

        return new int[0];
    }
}

