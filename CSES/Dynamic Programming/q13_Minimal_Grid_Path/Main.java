import java.util.*;

public class Main {
    static class Pair {
        int i, j;
        Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] grid = new String[n];
        for (int i = 0; i < n; i++) {
            grid[i] = sc.next();
        }

        boolean[][] seen = new boolean[n][n];
        Queue<Pair> frontier = new LinkedList<>();
        frontier.add(new Pair(0, 0));

        StringBuilder ans = new StringBuilder();
        ans.append(grid[0].charAt(0));

        int maxd = 2 * n - 2;

        for (int d = 1; d <= maxd; d++) {
            char best = 'Z' + 1;
            List<Pair> candidates = new ArrayList<>();

            for (Pair p : frontier) {
                int i = p.i, j = p.j;
                if (i + 1 < n) best = (char)Math.min(best, grid[i + 1].charAt(j));
                if (j + 1 < n) best = (char)Math.min(best, grid[i].charAt(j + 1));
            }

            for (Pair p : frontier) {
                int i = p.i, j = p.j;
                if (i + 1 < n && grid[i + 1].charAt(j) == best) candidates.add(new Pair(i + 1, j));
                if (j + 1 < n && grid[i].charAt(j + 1) == best) candidates.add(new Pair(i, j + 1));
            }

            frontier.clear();
            for (Pair p : candidates) {
                int i = p.i, j = p.j;
                if (!seen[i][j]) {
                    seen[i][j] = true;
                    frontier.add(p);
                }
            }

            // clear seen for next round (optional depending on re-use logic)
            for (Pair p : frontier) {
                seen[p.i][p.j] = false;
            }

            ans.append(best);
        }

        System.out.println(ans.toString());
    }
}

// Still TLEon java with 2 TCs


// import java.util.*;

// public class MinimalGridPath {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int n = Integer.parseInt(sc.nextLine());
//         char[][] grid = new char[n][n];
//         String[][] dp = new String[n][n];

//         for (int i = 0; i < n; i++) {
//             String line = sc.nextLine().trim();
//             for (int j = 0; j < n; j++) {
//                 grid[i][j] = line.charAt(j);
//             }
//         }

//         // Fill from bottom-right to top-left
//         for (int i = n - 1; i >= 0; i--) {
//             for (int j = n - 1; j >= 0; j--) {
//                 if (i == n - 1 && j == n - 1) {
//                     dp[i][j] = String.valueOf(grid[i][j]);
//                 } else {
//                     String down = (i + 1 < n) ? dp[i + 1][j] : "~";
//                     String right = (j + 1 < n) ? dp[i][j + 1] : "~";
//                     dp[i][j] = grid[i][j] + (down.compareTo(right) < 0 ? down : right);
//                 }
//             }
//         }

//         System.out.println(dp[0][0]);
//     }
// }





// Top down approach


// import java.util.*;

// public class MinimalGridPath {
//     static String[][] memo;
//     static char[][] grid;
//     static int n;

//     static String dfs(int i, int j) {
//         if (i >= n || j >= n) return "~";  // acts like infinity
//         if (i == n - 1 && j == n - 1) return String.valueOf(grid[i][j]);

//         if (memo[i][j] != null) return memo[i][j];

//         String down = dfs(i + 1, j);
//         String right = dfs(i, j + 1);

//         memo[i][j] = grid[i][j] + (down.compareTo(right) < 0 ? down : right);
//         return memo[i][j];
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         n = Integer.parseInt(sc.nextLine());
//         grid = new char[n][n];
//         memo = new String[n][n];

//         for (int i = 0; i < n; i++) {
//             String line = sc.nextLine().trim();
//             for (int j = 0; j < n; j++) {
//                 grid[i][j] = line.charAt(j);
//             }
//         }

//         System.out.println(dfs(0, 0));
//     }
// }
