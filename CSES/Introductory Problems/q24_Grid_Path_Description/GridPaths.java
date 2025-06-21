import java.util.*;
//toPass
public class GridPaths {

    static final int N = 7;
    static boolean[][] visited = new boolean[N][N];
    static int[] reserved = new int[49];
    static int steps = 0;
    static int paths = 0;
    static String s;

    static boolean inBounds(int i, int j) {
        return i >= 0 && i < N && j >= 0 && j < N;
    }

    static void solve(int r, int c) {
        if (r == 6 && c == 0) {
            if (steps == 48) paths++;
            return;
        }

        if (visited[r][c] ||
                (
                        ((c >= 1 && c <= 5 && !visited[r][c + 1] && !visited[r][c - 1]) &&
                                ((r == 0 && visited[r + 1][c]) || (r == 6 && visited[r - 1][c])))
                                ||
                                ((r >= 1 && r <= 5 && !visited[r + 1][c] && !visited[r - 1][c]) &&
                                        ((c == 0 && visited[r][c + 1]) || (c == 6 && visited[r][c - 1])))
                                ||
                                (r >= 1 && r <= 5 && c >= 1 && c <= 5 && visited[r + 1][c] && visited[r - 1][c] && !visited[r][c + 1] && !visited[r][c - 1])
                                ||
                                (r >= 1 && r <= 5 && c >= 1 && c <= 5 && visited[r][c + 1] && visited[r][c - 1] && !visited[r + 1][c] && !visited[r - 1][c])
                )
        ) {
            return;
        }

        visited[r][c] = true;

        if (reserved[steps] != -1) {
            switch (reserved[steps]) {
                case 0: // U
                    if (r > 0 && !visited[r - 1][c]) {
                        steps++;
                        solve(r - 1, c);
                        steps--;
                    }
                    break;
                case 1: // D
                    if (r < 6 && !visited[r + 1][c]) {
                        steps++;
                        solve(r + 1, c);
                        steps--;
                    }
                    break;
                case 2: // L
                    if (c > 0 && !visited[r][c - 1]) {
                        steps++;
                        solve(r, c - 1);
                        steps--;
                    }
                    break;
                case 3: // R
                    if (c < 6 && !visited[r][c + 1]) {
                        steps++;
                        solve(r, c + 1);
                        steps--;
                    }
                    break;
            }
            visited[r][c] = false;
            return;
        }

        if (r < 6 && !visited[r + 1][c]) {
            steps++;
            solve(r + 1, c);
            steps--;
        }
        if (r > 0 && !visited[r - 1][c]) {
            steps++;
            solve(r - 1, c);
            steps--;
        }
        if (c > 0 && !visited[r][c - 1]) {
            steps++;
            solve(r, c - 1);
            steps--;
        }
        if (c < 6 && !visited[r][c + 1]) {
            steps++;
            solve(r, c + 1);
            steps--;
        }

        visited[r][c] = false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        s = scanner.nextLine();

        for (int i = 0; i < 48; i++) {
            char ch = s.charAt(i);
            switch (ch) {
                case '?':
                    reserved[i] = -1;
                    break;
                case 'U':
                    reserved[i] = 0;
                    break;
                case 'D':
                    reserved[i] = 1;
                    break;
                case 'L':
                    reserved[i] = 2;
                    break;
                case 'R':
                    reserved[i] = 3;
                    break;
            }
        }

        solve(0, 0);
        System.out.println(paths);
    }
}
