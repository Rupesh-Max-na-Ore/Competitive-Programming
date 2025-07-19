import java.util.*;

public class td_1d {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();  // number of books
        int x = sc.nextInt();  // budget

        int[] prices = new int[n];
        int[] pages = new int[n];

        for (int i = 0; i < n; i++) {
            prices[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }

        int maxPages = knapsackSpaceOptimized(n, x, prices, pages);
        System.out.println(maxPages);
    }

    // Space-optimized 1D DP solution: O(n*x) time, O(x) space
    public static int knapsackSpaceOptimized(int n, int x, int[] prices, int[] pages) {
        int[] dp = new int[x + 1];

        for (int i = 0; i < n; i++) {
            for (int j = x; j >= prices[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - prices[i]] + pages[i]);
            }
        }

        return dp[x];
    }
}
