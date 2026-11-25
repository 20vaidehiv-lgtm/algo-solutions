public class test_practice4 {
    static void check(int[] nums, boolean expected) {
        boolean actual = new Solution().containsDuplicate(nums);
        if (actual != expected) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
    }

    public static void main(String[] args) {
        check(new int[]{1, 2, 3, 1}, true);
        check(new int[]{1, 2, 3, 4}, false);
        check(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true);
        check(new int[]{}, false);
        System.out.println("OK");
    }
}

