import java.util.*;

public class CountingNumbers {

    static long[][][][] dp;
    static int[] digits;

    static long solve(long x) {
        if (x < 0) return 0;
        String s = Long.toString(x);
        int n = s.length();
        digits = new int[n];
        for (int i = 0; i < n; i++) digits[i] = s.charAt(i) - '0';

        // Initialize memo table: pos (0..n), prev (-1..9) shifted by +1 → (0..10),
        // tight (0/1), leading (0/1)
        dp = new long[n + 1][11][2][2];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j < 11; j++)
                for (int k = 0; k < 2; k++)
                    Arrays.fill(dp[i][j][k], -1);

        return dfs(0, -1, 1, 1, n);
    }

    static long dfs(int pos, int prev, int tight, int leading, int n) {
        if (pos == n) {
            return leading == 1 ? 0 : 1; // valid if number formed
        }

        int prevIdx = prev + 1; // shift to handle -1
        if (dp[pos][prevIdx][tight][leading] != -1)
            return dp[pos][prevIdx][tight][leading];

        int limit = (tight == 1 ? digits[pos] : 9);
        long total = 0;

        for (int d = 0; d <= limit; d++) {
            if (leading == 0 && d == prev) continue; // adjacent digits must differ
            int newTight = (tight == 1 && d == limit) ? 1 : 0;
            int newLeading = (leading == 1 && d == 0) ? 1 : 0;
            total += dfs(pos + 1, (newLeading == 1 ? -1 : d), newTight, newLeading, n);
        }

        return dp[pos][prevIdx][tight][leading] = total;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong(), b = sc.nextLong();
        long ans = solve(b) - solve(a - 1);
        System.out.println(ans);
    }
}
