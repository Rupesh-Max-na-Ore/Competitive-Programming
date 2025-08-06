// import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class IncreasingSubsequence {

    public static void main(String[] args) throws IOException {
        // Setup BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Read input
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        // Initialize DP table
        int[]dp = new int[n + 1];

        // Bottom-up DP
        for (int i = n - 1; i >= 0; i--) {
            for (int par = i; par >= 0; par--) {
                int pick = 0;
                int notPick = dp[par];

                if (par == 0 || arr[i] > arr[par - 1]) {
                    pick = 1 + dp[i + 1]; // arr[i] included, so pass i+1 as par (1-based)
                }

                dp[par] = Math.max(pick, notPick);
            }
        }

        // Output the result
        System.out.println(dp[0]);
    }

    // public static void main(String[] args) throws IOException {
    //     // Setup BufferedReader
    //     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    //     // Read input
    //     int n = Integer.parseInt(br.readLine());
    //     String[] input = br.readLine().split(" ");
    //     int[] arr = new int[n];

    //     for (int i = 0; i < n; i++) {
    //         arr[i] = Integer.parseInt(input[i]);
    //     }

    //     // Initialize DP table
    //     int[][] dp = new int[n + 1][n + 1]; // dp[i][par], 1-based indexing for par

    //     // Bottom-up DP
    //     for (int i = n - 1; i >= 0; i--) {
    //         for (int par = 0; par <= i; par++) {
    //             int pick = 0;
    //             int notPick = dp[i + 1][par];

    //             if (par == 0 || arr[i] > arr[par - 1]) {
    //                 pick = 1 + dp[i + 1][i + 1]; // arr[i] included, so pass i+1 as par (1-based)
    //             }

    //             dp[i][par] = Math.max(pick, notPick);
    //         }
    //     }

    //     // Output the result
    //     System.out.println(dp[0][0]);
    // }
    // // Same with scanner

    // public static void main (String args[] ){
    //     Scanner sc = new Scanner(System.in);

    //     int n = sc.nextInt();
    //     int[] arr = new int[n];

    //     for(int i = 0; i < n; i++) {
    //         arr[i] = sc.nextInt();
    //     }

    //     // dp[i][par] => LIS starting from index i with previous index = par - 1
    //     int[][] dp = new int[n + 1][n + 1];

    //     for (int i = n - 1; i >= 0; i--) {
    //         for (int par = 0; par <= i; par++) {
    //             int pick = 0;
    //             int notPick = dp[i + 1][par];
    //             if (par == 0 || arr[i] > arr[par - 1]) {
    //                 pick = 1 + dp[i + 1][i + 1];  // i+1 because we map index i to par = i+1
    //             }
    //             dp[i][par] = Math.max(pick, notPick);
    //         }
    //     }

    //     System.out.println(dp[0][0]);
    // }
}
