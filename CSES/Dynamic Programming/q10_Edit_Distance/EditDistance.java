/*
 * CSES Problem Set
      Edit Distance

Task
Submit
Results
Statistics
Tests








CSES - Edit Distance




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



The edit distance between two strings is the minimum number of operations required to transform one string into the other.
The allowed operations are:

Add one character to the string.
Remove one character from the string.
Replace one character in the string.

For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.
Your task is to calculate the edit distance between two strings.
Input
The first input line has a string that contains n characters between A–Z.
The second input line has a string that contains m characters between A–Z.
Output
Print one integer: the edit distance between the strings.
Constraints

1 \le n,m \le 5000

Example
Input:
LOVE
MOVIE

Output:
2
 */

import java.util.Scanner;

public class EditDistance {

    public static int edit_dist(String s1, String s2){
        int n,m;
        n = s1.length();
        m = s2.length();

        int[][] dp = new int[n+1][m+1];

        // Base Cases
        for(int i = 0; i<= n; i++) dp[i][0] = i;
        for(int i = 0; i<= m; i++) dp[0][i] = i;

        for(int i = 1; i <=n ; i++ ){
            for( int j =1; j<=m; j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) dp[i][j] = dp[i-1][j-1];
                else{
                    int minno = Math.min(dp[i-1][j-1], Math.min(dp[i][j-1], dp[i-1][j]));
                    dp[i][j] = 1 + minno;
                }
            }
        }
        return dp[n][m];

    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        System.out.println(edit_dist(s1,s2));

        sc.close();
    }
}

/*
//2 Array Space optimized way

import java.util.Scanner;

public class EditDistanceOptimized {

    public static int edit_dist(String s1, String s2){
        int n = s1.length();
        int m = s2.length();

        // Always use smaller string for space optimization
        if (m < n) {
            String temp = s1; s1 = s2; s2 = temp;
            int tmp = n; n = m; m = tmp;
        }

        // Now: s1.length() = n <= s2.length() = m
        int[] prev = new int[m + 1];
        int[] curr = new int[m + 1];

        // Initialize base case: transforming "" to s2[0..j]
        for (int j = 0; j <= m; j++) prev[j] = j;

        for (int i = 1; i <= n; i++) {
            curr[0] = i; // base case: transforming s1[0..i] to ""

            for (int j = 1; j <= m; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    curr[j] = prev[j - 1];
                } else {
                    curr[j] = 1 + Math.min(
                        prev[j],        // delete
                        Math.min(
                            curr[j - 1],    // insert
                            prev[j - 1]     // replace
                        )
                    );
                }
            }

            // Move current row to previous for next iteration
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }

        return prev[m];
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        System.out.println(edit_dist(s1, s2));
        sc.close();
    }
}
 */