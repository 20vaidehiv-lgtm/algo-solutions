public class test_practice8 {
    public static void main(String[] args) {
        int[] nums = {-2, 3, -2, -1};
        int expected = 12;
        int actual = new Solution().maxProduct(nums);
        if (actual != expected) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
        System.out.println("OK");
    }
}
