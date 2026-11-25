public class test_practice1 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] inputs = {"()", "()[]{}", "(]", "([])", "([)]", "{[]}", "", "("};
        boolean[] expected = {true, true, false, true, false, true, true, false};

        for (int i = 0; i < inputs.length; i++) {
            boolean actual = sol.isValid(inputs[i]);
            if (actual != expected[i]) {
                throw new AssertionError("Input " + inputs[i] + ": expected " + expected[i] + " but got " + actual);
            }
        }
        System.out.println("OK");
    }
}

