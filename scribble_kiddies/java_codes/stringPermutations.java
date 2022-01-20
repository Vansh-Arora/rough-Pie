package java_codes;

public class stringPermutations {
    public static void generate(String S, String ans) {
        if (S.length() == 0) {
            System.out.println(ans);
            return;
        }
        for (int i = 0; i < S.length(); i++) {
            generate(S.substring(0, i) + S.substring(i + 1), ans + S.charAt(i));
        }
    }

    public static void main(String args[]) {
        String S = "ABC";
        generate(S, "");
    }
}