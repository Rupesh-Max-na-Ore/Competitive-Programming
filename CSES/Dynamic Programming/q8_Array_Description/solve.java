// For CP cses submissions
import java.util.*;
import java.io.*;

public class solve {
    static final int MOD = 1_000_000_007;

    public static int Array_paths(int n, int m, int[] a) {
        int[][] dp = new int[n + 1][m + 2];

        // Base Case Initialization
        if (a[0] == 0) {
            for (int j = 1; j <= m; j++) {
                dp[1][j] = 1;
            }
        } else {
            dp[1][a[0]] = 1;
        }

        // DP Transitions
        for (int i = 2; i <= n; i++) {
            if (a[i - 1] != 0) {
                int val = a[i - 1];
                dp[i][val] = (
                    ((dp[i - 1][val - 1] + dp[i - 1][val]) % MOD + dp[i - 1][val + 1]) % MOD
                );
            } else {
                for (int j = 1; j <= m; j++) {
                    dp[i][j] = (
                        ((dp[i - 1][j - 1] + dp[i - 1][j]) % MOD + dp[i - 1][j + 1]) % MOD
                    );
                }
            }
        }

        // Final Answer
        if (a[n - 1] == 0) {
            int sum = 0;
            for (int j = 1; j <= m; j++) {
                sum = (sum + dp[n][j]) % MOD;
            }
            return sum;
        } else {
            return dp[n][a[n - 1]];
        }
    }

    public static void main(String[] args) throws IOException {
        // Fast Input for CSES
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line1 = br.readLine().split(" ");
        int n = Integer.parseInt(line1[0]);
        int m = Integer.parseInt(line1[1]);

        String[] line2 = br.readLine().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(line2[i]);
        }

        // Compute and Output
        int ans = Array_paths(n, m, a);
        System.out.println(ans);
    }
}
