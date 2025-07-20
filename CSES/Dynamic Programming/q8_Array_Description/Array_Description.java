

import java.util.Scanner;

public class Array_Description {
    public static int Array_paths(int n, int m, int a[]){
        int[][] dp = new int[n+1][m+2];

        // Base Case
        if(a[0]==0){ //not fixed start
            for(int j = 1; j<=m; j++){
                dp[1][j] = 1;
            }
        }else dp[1][a[0]] = 1;

        for(int i=2; i<=n; i++){
            if(a[i-1]!=0){ //fixed point in path
                dp[i][a[i-1]] += dp[i-1][a[i-1]-1]
                                + dp[i-1][a[i-1]]
                                + dp[i-1][a[i-1]+1];
            }else{ //1 to m points
                for(int j = 1; j<=m; j++){
                    dp[i][j] += dp[i-1][j-1]
                                + dp[i-1][j]
                                + dp[i-1][j+1];
                }
            }
        }

        if(a[n-1]==0){//1 to m valid end pts.
            int sum = 0;
            for(int j = 1; j<=m; j++){
                sum += dp[n][j];
            }
            return sum;
        }
        // else if fixed pt end
        return dp[n][a[n-1]];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a[]= new int[n];
        for(int i=0; i<n; i++) a[i] = sc.nextInt();
        System.out.println(Array_paths(n, m, a)); 
    }

    /* //Another faster way to take i/o
     * public static void main(String[] args) throws IOException {
        // Fast Input for CSES
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line1 = br.readLine().split(" ");
        int n = Integer.parseInt(line1[0]);
        int m = Integer.parseInt(line1[1]);

        String[] line2 = br.readLine().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(line2[i]);
        }

        // Compute and Output
        int ans = Array_paths(n, m, a);
        System.out.println(ans);
    }
      */
}
