public class test_practice6 {
    static void check(String s, String t, boolean expected) {
        boolean actual = new Solution().isAnagram(s, t);
        if (actual != expected) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
    }

    public static void main(String[] args) {
        check("anagram", "nagaram", true);
        check("rat", "car", false);
        check("a", "a", true);
        check("ab", "a", false);
        System.out.println("OK");
    }
}

