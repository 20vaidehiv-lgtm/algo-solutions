// Note: solutions/java/practice5.java is currently marked IN PROGRESS.
public class test_practice5 {
    static void check(int[] nums, int target, int expected) {
        int actual = new Solution().search(nums, target);
        if (actual != expected) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
    }

    public static void main(String[] args) {
        check(new int[]{-1, 0, 3, 5, 9, 12}, 9, 4);
        check(new int[]{-1, 0, 3, 5, 9, 12}, 2, -1);
        check(new int[]{5}, 5, 0);
        check(new int[]{2, 5}, 5, 1);
        System.out.println("OK");
    }
}

