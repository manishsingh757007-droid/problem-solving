// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    // Helper to convert string like "[1,2,3,4,5]" into linked list
    public static ListNode deserialize(String data) {
        if (data == null || data.length() <= 2) return null; // "[]"
        data = data.substring(1, data.length() - 1); // remove brackets
        String[] parts = data.split(",");
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (String p : parts) {
            curr.next = new ListNode(Integer.parseInt(p.trim()));
            curr = curr.next;
        }
        return dummy.next;
    }

    // Helper to convert linked list back to string "[5,4,3,2,1]"
    public static String serialize(ListNode head) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        while (head != null) {
            sb.append(head.val);
            head = head.next;
            if (head != null) sb.append(",");
        }
        sb.append("]");
        return sb.toString();
    }
}

// 🔹 Solution class that driver expects
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next; // save next
            curr.next = prev;          // reverse link
            prev = curr;               // move prev forward
            curr = next;               // move curr forward
        }
        
        return prev; // new head
    }
}



