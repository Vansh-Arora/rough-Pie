package java_codes;

public class tilePlacement {

    public static int fit(int n, int m) {
        if (n == m) {
            return 2;
        }
        if (n < m)
            return n;
        int horizontalMoves = fit(n - 1, m);
        int verticalMoves = fit(n - m, m);
        return horizontalMoves + verticalMoves;

    }

    public static void main(String args[]) {
        System.out.println(fit(4, 2));
    }
}