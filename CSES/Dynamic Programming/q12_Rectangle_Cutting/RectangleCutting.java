import java.util.Scanner;

public class RectangleCutting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); // height
        int b = sc.nextInt(); // width

        int[][] dp = new int[a + 1][b + 1];

        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= b; j++) {
                if (i == j) {
                    dp[i][j] = 0; // square, no cuts needed
                } else {
                    int minCuts = Integer.MAX_VALUE;

                    // vertical cuts (cut along height)
                    for (int k = 1; k < i; k++) {
                        minCuts = Math.min(minCuts, 1 + dp[k][j] + dp[i - k][j]);
                    }

                    // horizontal cuts (cut along width)
                    for (int k = 1; k < j; k++) {
                        minCuts = Math.min(minCuts, 1 + dp[i][k] + dp[i][j - k]);
                    }

                    dp[i][j] = minCuts;
                }
            }
        }

        System.out.println(dp[a][b]);
    }
}
