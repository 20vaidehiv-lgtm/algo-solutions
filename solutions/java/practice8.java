// Problem: Maximum Product Subarray
// Source: https://leetcode.com/problems/maximum-product-subarray/
// Topic: Dynamic Programming, Arrays
// Status: ✅ Done

class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            int prevMax = maxProd;
            maxProd = Math.max(num, Math.max(prevMax * num, minProd * num));
            minProd = Math.min(num, Math.min(prevMax * num, minProd * num));

            result = Math.max(result, maxProd);
        }

        return result;
    }


}

