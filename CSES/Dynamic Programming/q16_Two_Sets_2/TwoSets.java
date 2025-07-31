import java.util.Scanner;
// Accepted
public class TwoSets {
    static final int MOD = 1_000_000_007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long total = (long) n * (n + 1) / 2;

        // If total ain't even, can never have 2 partions with equal sum
        if (total % 2 != 0) {
            System.out.println(0);
            return;
        }

        int target = (int) (total / 2);
        long[][] dp = new long[n + 2][target + 1];

        // base case
        dp[n + 1][target] = 1;

        for (int i = n; i >= 1; i--) {
            for (int j = 0; j <= target; j++) {
                dp[i][j] = dp[i + 1][j]; // skip i
                if (j + i <= target) {
                    dp[i][j] = (dp[i][j] + dp[i + 1][j + i]) % MOD; // take i
                }
            }
        }

        long inv2 = modInverse(2, MOD);
        System.out.println(dp[1][0] * inv2 % MOD);
    }

    // Fermat’s Little Theorem: a^(MOD-2) % MOD = inverse of a % MOD
    static long modInverse(long a, int mod) {
        return pow(a, mod - 2, mod);
    }

    static long pow(long base, long exp, int mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
}
