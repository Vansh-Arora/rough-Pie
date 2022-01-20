package java_codes;

public class grid_movement {
    public static void move(int i, int j, int m, int n, String ans) {
        if (i == m - 1 && j == n - 1) {
            System.out.println(ans);
            return;
        }
        if (i >= m || j >= n)
            return;
        move(i + 1, j, m, n, ans + 'D');
        move(i, j + 1, m, n, ans + 'R');

    }

    public static void main(String args[]) {
        move(0, 0, 3, 3, "");
    }
}