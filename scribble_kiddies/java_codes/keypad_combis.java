package java_codes;

public class keypad_combis {
    public static String[] keypad = { ".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "uv", "wx", "yz" };

    public static void make(String S, int n, int i, String ans) {
        if (i == n) {
            System.out.println(ans);
            return;
        }
        int idx = S.charAt(i) - '0';
        for (int j = 0; j < keypad[idx].length(); j++) {
            make(S, n, i + 1, ans + keypad[idx].charAt(j));
        }

    }

    public static void main(String[] args) {
        make("12", 2, 0, "");
    }
}
