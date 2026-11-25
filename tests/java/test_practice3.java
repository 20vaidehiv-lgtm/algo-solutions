public class test_practice3 {
    static void check(int[] prices, int expected) {
        int actual = new Solution().maxProfit(prices);
        if (actual != expected) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
    }

    public static void main(String[] args) {
        check(new int[]{7, 1, 5, 3, 6, 4}, 5);
        check(new int[]{7, 6, 4, 3, 1}, 0);
        check(new int[]{2, 4, 1}, 2);
        check(new int[]{}, 0);
        System.out.println("OK");
    }
}

