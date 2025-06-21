import java.util.*;
//toPass2
public class GridPaths2 {

    static final int RIGHT = 0, LEFT = 1, DOWN = 2, UP = 3;
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static String str;
    static int[][] vis = new int[7][7];

    static boolean isValid(int a, int b, int c) {
        return a >= b && a < c;
    }

    static int countPaths(int x, int y, int pos) {
        if (pos == str.length()) return (x == 6 && y == 0) ? 1 : 0;
        if (x == 6 && y == 0) return 0;
        if (vis[x][y] == 1) return 0;

        boolean[] visited = new boolean[4];
        Arrays.fill(visited, false);

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k], ny = y + dy[k];
            if (isValid(nx, 0, 7) && isValid(ny, 0, 7)) {
                visited[k] = vis[nx][ny] == 1;
            }
        }

        if (!visited[DOWN] && !visited[UP] && visited[RIGHT] && visited[LEFT]) return 0;
        if (!visited[RIGHT] && !visited[LEFT] && visited[DOWN] && visited[UP]) return 0;

        if (isValid(x - 1, 0, 7) && isValid(y + 1, 0, 7) && vis[x - 1][y + 1] == 1)
            if (!visited[RIGHT] && !visited[UP]) return 0;

        if (isValid(x + 1, 0, 7) && isValid(y + 1, 0, 7) && vis[x + 1][y + 1] == 1)
            if (!visited[RIGHT] && !visited[DOWN]) return 0;

        if (isValid(x - 1, 0, 7) && isValid(y - 1, 0, 7) && vis[x - 1][y - 1] == 1)
            if (!visited[LEFT] && !visited[UP]) return 0;

        if (isValid(x + 1, 0, 7) && isValid(y - 1, 0, 7) && vis[x + 1][y - 1] == 1)
            if (!visited[LEFT] && !visited[DOWN]) return 0;

        vis[x][y] = 1;
        int numOfPaths = 0;

        if (str.charAt(pos) == '?') {
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k], ny = y + dy[k];
                if (isValid(nx, 0, 7) && isValid(ny, 0, 7)) {
                    numOfPaths += countPaths(nx, ny, pos + 1);
                }
            }
        } else {
            char ch = str.charAt(pos);
            if (ch == 'R' && y + 1 < 7) numOfPaths += countPaths(x, y + 1, pos + 1);
            else if (ch == 'L' && y - 1 >= 0) numOfPaths += countPaths(x, y - 1, pos + 1);
            else if (ch == 'U' && x - 1 >= 0) numOfPaths += countPaths(x - 1, y, pos + 1);
            else if (ch == 'D' && x + 1 < 7) numOfPaths += countPaths(x + 1, y, pos + 1);
        }

        vis[x][y] = 0;
        return numOfPaths;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        str = sc.next();
        System.out.println(countPaths(0, 0, 0));
    }
}
