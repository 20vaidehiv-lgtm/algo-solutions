import java.util.ArrayList;
import java.util.List;

public class MergeTwoSortedListsTest {
    static ListNode build(int... vals) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;
        for (int v : vals) {
            tail.next = new ListNode(v);
            tail = tail.next;
        }
        return dummy.next;
    }

    static List<Integer> toList(ListNode head) {
        List<Integer> out = new ArrayList<>();
        for (ListNode n = head; n != null; n = n.next) {
            out.add(n.val);
        }
        return out;
    }

    static void check(int[] a, int[] b, List<Integer> expected) {
        List<Integer> actual = toList(new Solution().mergeTwoLists(build(a), build(b)));
        if (!actual.equals(expected)) {
            throw new AssertionError("expected " + expected + " but got " + actual);
        }
    }

    public static void main(String[] args) {
        check(new int[]{1, 2, 4}, new int[]{1, 3, 4}, List.of(1, 1, 2, 3, 4, 4));
        check(new int[]{}, new int[]{}, List.of());
        check(new int[]{}, new int[]{0}, List.of(0));
        check(new int[]{5}, new int[]{}, List.of(5));
        check(new int[]{1, 2}, new int[]{3, 4}, List.of(1, 2, 3, 4));
        System.out.println("OK");
    }
}
