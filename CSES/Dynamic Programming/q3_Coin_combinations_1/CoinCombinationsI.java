import java.util.*;

public class CoinCombinationsI {
    static final int MOD = 1_000_000_007;

    public static int countWays(int n, int x, int[] coins) {
        int[] dp = new int[x + 1];
        dp[0] = 1;  // base case: 1 way to make sum 0

        for (int i = 1; i <= x; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = (dp[i] + dp[i - coin]) % MOD;
                }
            }
        }

        return dp[x];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        System.out.println(countWays(n, x, coins));
    }
}
