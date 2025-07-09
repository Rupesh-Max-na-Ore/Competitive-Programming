import java.util.*;

public class MinimizingCoins {

    public static int minimizeCoins(int n, int x, int[] coins) {
        int INF = (int) 1e9;
        int[] dp = new int[x + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0; // base case

        for (int i = 1; i <= x; i++) {
            for (int j = 0; j < n; j++) {
                if (i - coins[j] >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }

        return dp[x] == INF ? -1 : dp[x];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] coins = new int[n];

        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        System.out.println(minimizeCoins(n, x, coins));
    }
}
