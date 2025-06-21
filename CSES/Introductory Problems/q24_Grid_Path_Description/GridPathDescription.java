import java.util.*;

public class GridPathDescription {
    static final int N = 7;
    static boolean[][] visited = new boolean[N][N];
    static String path;
    static int count = 0;

    // Directions: U, D, L, R
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static char[] dir = { 'U', 'D', 'L', 'R' };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        path = scanner.next();
        scanner.close();

        visited[0][0] = true;
        dfs(0, 0, 0);
        System.out.println(count);
    }

    static void dfs(int x, int y, int step) {
        // If already reached the end at step 48
        if (x == 6 && y == 0) {
            if (step == 48) count++;
            return;
        }

        // If steps exhausted
        if (step >= 48) return;

        // Prune dead ends
        if (isTrapped(x, y)) return;

        char move = path.charAt(step);
        for (int i = 0; i < 4; i++) {
            if (move != '?' && move != dir[i]) continue;

            int nx = x + dx[i];
            int ny = y + dy[i];

            if (inBounds(nx, ny) && !visited[nx][ny]) {
                visited[nx][ny] = true;
                dfs(nx, ny, step + 1);
                visited[nx][ny] = false;
            }
        }
    }

    static boolean inBounds(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    // Prune if the path is trapped (to avoid TLE)
    static boolean isTrapped(int x, int y) {
        // If moving horizontally is blocked and both vertical directions are unvisited, it is a trap
        if (x > 0 && x < N - 1 && !visited[x - 1][y] && !visited[x + 1][y]) {
            if (y == 0 || y == N - 1 || (visited[x][y - 1] && visited[x][y + 1])) return true;
        }

        // If moving vertically is blocked and both horizontal directions are unvisited, it is a trap
        if (y > 0 && y < N - 1 && !visited[x][y - 1] && !visited[x][y + 1]) {
            if (x == 0 || x == N - 1 || (visited[x - 1][y] && visited[x + 1][y])) return true;
        }

        return false;
    }
}
