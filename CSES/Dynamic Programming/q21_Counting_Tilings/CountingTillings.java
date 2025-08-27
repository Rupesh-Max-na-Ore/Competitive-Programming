import java.io.*;
import java.util.*;

public class CountingTillings {
    static final int MOD = 1000000007;
    static int n, m;
    static long[][] dp; // dp[col][mask]

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // dp[col][mask]: number of ways up to column col with given mask
        dp = new long[m + 1][1 << n];
        dp[0][0] = 1;

        for (int col = 0; col < m; col++) {
            for (int mask = 0; mask < (1 << n); mask++) {
                if (dp[col][mask] == 0) continue;
                // generate next masks via DFS
                generateNextMasks(mask, 0, 0, col);
            }
        }

        System.out.println(dp[m][0] % MOD);
    }

    // DFS generates all valid next masks
    static void generateNextMasks(int currMask, int row, int nextMask, int col) {
        if (row == n) {
            dp[col + 1][nextMask] = (dp[col + 1][nextMask] + dp[col][currMask]) % MOD;
            return;
        }
        if ((currMask & (1 << row)) != 0) {
            // already filled → move to next row
            generateNextMasks(currMask, row + 1, nextMask, col);
        } else {
            // place vertical domino
            generateNextMasks(currMask, row + 1, nextMask | (1 << row), col);

            // place horizontal domino (check row+1 exists and is free)
            if (row + 1 < n && (currMask & (1 << (row + 1))) == 0) {
                generateNextMasks(currMask, row + 2, nextMask, col);
            }
        }
    }
}
