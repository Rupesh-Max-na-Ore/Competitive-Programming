You're quite close to a working CSES-compliant Java solution. Here's how to properly **read input** and **print output** as expected by the CSES Online Judge:

---

### ✅ CSES Input Format for this Problem

You're given:

```
n m
a[0] a[1] ... a[n-1]
```

Example:

```
3 5
2 0 2
```

---

### ✅ Recommended Java Input/Output for CSES

CSES prefers:

* Fast I/O (`Scanner` is acceptable for small `n`, but `BufferedReader` is better).
* Output using `System.out.println()`.

---

## ✅ Final Working Java Code for CSES: `Array_Description`

```java
package CSES.Dynamic;

import java.util.*;
import java.io.*;

public class Array_Description {

    static final int MOD = 1_000_000_007;

    public static int Array_paths(int n, int m, int[] a) {
        int[][] dp = new int[n + 1][m + 2];

        // Base Case Initialization
        if (a[0] == 0) {
            for (int j = 1; j <= m; j++) {
                dp[1][j] = 1;
            }
        } else {
            dp[1][a[0]] = 1;
        }

        // DP Transitions
        for (int i = 2; i <= n; i++) {
            if (a[i - 1] != 0) {
                int val = a[i - 1];
                dp[i][val] = (
                    ((dp[i - 1][val - 1] + dp[i - 1][val]) % MOD + dp[i - 1][val + 1]) % MOD
                );
            } else {
                for (int j = 1; j <= m; j++) {
                    dp[i][j] = (
                        ((dp[i - 1][j - 1] + dp[i - 1][j]) % MOD + dp[i - 1][j + 1]) % MOD
                    );
                }
            }
        }

        // Final Answer
        if (a[n - 1] == 0) {
            int sum = 0;
            for (int j = 1; j <= m; j++) {
                sum = (sum + dp[n][j]) % MOD;
            }
            return sum;
        } else {
            return dp[n][a[n - 1]];
        }
    }

    public static void main(String[] args) throws IOException {
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
}
```

---

## 🔍 Tips for CSES Java Submissions

| Aspect      | Suggestion                                            |
| ----------- | ----------------------------------------------------- |
| Input       | Use `BufferedReader` and `String.split()`             |
| Output      | Use `System.out.println()`                            |
| I/O Classes | Avoid `Scanner` and `System.out.print` in tight loops |
| Time Limit  | Use `int` or `long` carefully (no BigInteger needed)  |
| Modular Ops | Always `% MOD` after every addition                   |

---

Would you like this version to also **print the DP table step-by-step** for debugging/learning?
----


## How to take normal input from Scanner?
You can replace the `BufferedReader` and `readLine()` code with `Scanner` if you're okay with slightly slower input (which is acceptable for most problems on CSES up to \~10⁵ inputs).

Here’s how to take the same input using `Scanner`:

---

### ✅ Using `Scanner` instead of `BufferedReader`

Replace this:

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String[] line1 = br.readLine().split(" ");
int n = Integer.parseInt(line1[0]);
int m = Integer.parseInt(line1[1]);

String[] line2 = br.readLine().split(" ");
int[] a = new int[n];
for (int i = 0; i < n; i++) {
    a[i] = Integer.parseInt(line2[i]);
}
```

With this:

```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int m = sc.nextInt();

int[] a = new int[n];
for (int i = 0; i < n; i++) {
    a[i] = sc.nextInt();
}
```

---

### 🧾 Full Example Using `Scanner`

```java
import java.util.*;

public class Array_Description {
    static final int MOD = 1_000_000_007;

    public static int Array_paths(int n, int m, int[] a) {
        int[][] dp = new int[n + 1][m + 2];

        if (a[0] == 0) {
            for (int j = 1; j <= m; j++) {
                dp[1][j] = 1;
            }
        } else {
            dp[1][a[0]] = 1;
        }

        for (int i = 2; i <= n; i++) {
            if (a[i - 1] != 0) {
                int val = a[i - 1];
                dp[i][val] = (
                    ((dp[i - 1][val - 1] + dp[i - 1][val]) % MOD + dp[i - 1][val + 1]) % MOD
                );
            } else {
                for (int j = 1; j <= m; j++) {
                    dp[i][j] = (
                        ((dp[i - 1][j - 1] + dp[i - 1][j]) % MOD + dp[i - 1][j + 1]) % MOD
                    );
                }
            }
        }

        if (a[n - 1] == 0) {
            int sum = 0;
            for (int j = 1; j <= m; j++) {
                sum = (sum + dp[n][j]) % MOD;
            }
            return sum;
        } else {
            return dp[n][a[n - 1]];
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.println(Array_paths(n, m, a));
    }
}
```

---

### 📌 When to Use `Scanner`

* ✅ Convenient for small/medium inputs.
* ❌ Slower for large datasets (`BufferedReader` or custom readers preferred).

Let me know if you want a version that reads from file or handles performance for `n > 10⁵`.
