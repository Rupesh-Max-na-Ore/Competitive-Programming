import java.util.*;

public class CountingNumbers {

    static long[][][][] dp;
    static int[] digits;

    static long solve(long x) {
        if (x < 0) return 0;
        // if (x == 0) return 1; // special case
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
// Correctedv version, above doesn't pass cases where a=0
/*static int[] digits;
    static int[][][][] dp; 
    // dp[pos][prev+1][tight][leading]
    // prev = -1 mapped to index 0, digits 0–9 mapped to 1–10

    static int solve(int pos, int prev, boolean tight, boolean leading, int n) {
        if (pos == n) {
            return leading ? 0 : 1; // valid if at least one digit placed
        }

        int prevIdx = prev + 1;
        int tightIdx = tight ? 1 : 0;
        int leadIdx = leading ? 1 : 0;

        if (dp[pos][prevIdx][tightIdx][leadIdx] != -1) {
            return dp[pos][prevIdx][tightIdx][leadIdx];
        }

        int limit = tight ? digits[pos] : 9;
        int total = 0;

        for (int d = 0; d <= limit; d++) {
            if (!leading && d == prev) continue; // avoid consecutive same digits

            boolean newLeading = leading && (d == 0);
            int newPrev = newLeading ? -1 : d;

            total += solve(
                pos + 1,
                newPrev,
                tight && (d == limit),
                newLeading,
                n
            );
        }

        return dp[pos][prevIdx][tightIdx][leadIdx] = total;
    }

    static int countValid(int x) {
        if (x < 0) return 0;

        String s = String.valueOf(x);
        int n = s.length();
        digits = new int[n];
        for (int i = 0; i < n; i++) digits[i] = s.charAt(i) - '0';

        dp = new int[n][11][2][2]; // pos, prev (-1..9 => 11), tight, leading
        for (int[][][] arr3 : dp)
            for (int[][] arr2 : arr3)
                for (int[] arr1 : arr2)
                    Arrays.fill(arr1, -1);

        return solve(0, -1, true, true, n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        if (a == 0) {
            System.out.println(countValid(b) + 1); // include 0
        } else {
            System.out.println(countValid(b) - countValid(a - 1));
        }
    } */