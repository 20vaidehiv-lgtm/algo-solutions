import java.util.Arrays;

public class test_practice2 {
    static void check(int[] nums, int target, int[] expected) {
        int[] actual = new Solution().twoSum(nums, target);
        if (!Arrays.equals(actual, expected)) {
            throw new AssertionError("expected " + Arrays.toString(expected) + " but got " + Arrays.toString(actual));
        }
    }

    public static void main(String[] args) {
        check(new int[]{2, 7, 11, 15}, 9, new int[]{0, 1});
        check(new int[]{3, 2, 4}, 6, new int[]{1, 2});
        check(new int[]{3, 3}, 6, new int[]{0, 1});
        check(new int[]{1, 2, 3}, 10, new int[]{});
        System.out.println("OK");
    }
}

