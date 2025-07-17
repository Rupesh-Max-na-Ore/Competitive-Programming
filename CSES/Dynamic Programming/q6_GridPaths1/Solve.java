import java.util.*;

/*
 * Grid Paths I

Task
Submit
Results
Statistics
Tests








CSES - Grid Paths I




addEventListener("DOMContentLoaded", function (e) {
    const mathElements = document.getElementsByClassName("math");
    const macros = {};
    for (let element of mathElements) {
        katex.render(element.textContent, element, {
            displayMode: element.classList.contains("math-display"),
            throwOnError: false,
            globalGroup: true,
            macros,
        });
    }
});


Time limit: 1.00 s
Memory limit: 512 MB



Consider an n \times n grid whose squares may have traps. It is not allowed to move to a square with a trap.
Your task is to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.
Input
The first input line has an integer n: the size of the grid.
After this, there are n lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.
Output
Print the number of paths modulo 10^9+7.
Constraints

1 \le n \le 1000

Example
Input:
4
....
.*..
...*
*...

Output:
3
 */

public class Solve {
    static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            grid[i] = sc.next().toCharArray();
        }

        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '*') {
                    dp[i][j] = 0;
                } else if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                } else {
                    if (i > 0) dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD;
                    if (j > 0) dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD;
                }
            }
        }

        System.out.println(dp[n-1][n-1]);
    }
}