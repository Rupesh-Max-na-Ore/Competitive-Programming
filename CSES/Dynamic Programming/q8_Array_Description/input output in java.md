In **Java**, there are multiple ways to handle **input and output**, and the choice depends on:

* Input **size** (small or large),
* Need for **speed**,
* Need for **parsing convenience**,
* Use case (e.g., **CSES/CP**, **file I/O**, **standard input**, etc.).

Below is a **comparison of major I/O techniques** in Java, with detailed explanation, pros/cons, and sample code for each.

---

## 🔸 1. `Scanner` (Easy and Readable)

### ✅ Pros:

* Simple and intuitive to use.
* Works well with space-separated and line-based input.

### ❌ Cons:

* **Slower** for large input (especially in CP).

### 📄 Sample Code:

```java
import java.util.*;

public class ScannerInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // read integer
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();  // read each element
        }
        System.out.println(Arrays.toString(a));
    }
}
```

---

## 🔸 2. `BufferedReader` + `StringTokenizer` (Fast and Flexible)

### ✅ Pros:

* Much **faster than Scanner**.
* Good for large inputs (e.g., CP like CSES).
* Allows reading **lines** quickly.

### ❌ Cons:

* A bit more verbose.
* Must manually split and parse.

### 📄 Sample Code:

```java
import java.io.*;
import java.util.*;

public class BufferedReaderInput {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());  // first line
        int[] a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine()); // second line
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(Arrays.toString(a));
    }
}
```

---

## 🔸 3. `DataInputStream` (Ultra-Fast, Low-Level)

### ✅ Pros:

* Fastest among all standard input methods.
* Used in **competitive programming** with very large input.

### ❌ Cons:

* Low-level, must parse manually.
* No support for whitespace splitting.

### 📄 Sample Code:

```java
import java.io.*;

public class DataInputStreamExample {
    public static void main(String[] args) throws IOException {
        DataInputStream dis = new DataInputStream(System.in);
        int n = Integer.parseInt(dis.readLine());
        String[] nums = dis.readLine().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(nums[i]);
        }
        System.out.println(Arrays.toString(a));
    }
}
```

---

## 🔸 4. `Console` (for Interactive / Secure Input)

### ✅ Pros:

* Can hide password input.
* Useful in **interactive applications**.

### ❌ Cons:

* Not supported in some environments (e.g., some IDEs).
* Not useful in competitive programming.

### 📄 Sample Code:

```java
import java.io.Console;

public class ConsoleInput {
    public static void main(String[] args) {
        Console console = System.console();
        if (console == null) {
            System.out.println("Console not available");
            return;
        }
        String name = console.readLine("Enter your name: ");
        char[] password = console.readPassword("Enter password: ");
        System.out.println("Welcome " + name);
    }
}
```

---

## 🔸 5. `Scanner` + `File` (File Input)

### ✅ Pros:

* Easy file reading.
* Useful for testing with input files.

### ❌ Cons:

* Slower than `BufferedReader`.

### 📄 Sample Code:

```java
import java.util.*;
import java.io.*;

public class FileScannerInput {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("input.txt"));
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        System.out.println(Arrays.toString(a));
    }
}
```

---

## 🔸 6. `BufferedReader` + `BufferedWriter` (Efficient Input & Output)

### ✅ Pros:

* High-performance I/O (especially with large input/output).
* BufferedWriter allows **fast output** compared to `System.out.println()`.

### ❌ Cons:

* Slightly more verbose.

### 📄 Sample Code:

```java
import java.io.*;

public class BufferedIO {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String[] parts = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            bw.write(parts[i] + "\n");  // fast output
        }
        bw.flush();  // very important!
    }
}
```

---

## ✅ Summary Comparison Table

| Method                  | Speed        | Ease of Use | Parsing Needed | Use Case                      |
| ----------------------- | ------------ | ----------- | -------------- | ----------------------------- |
| `Scanner`               | ❌ Slow       | ✅ Easy      | ❌ No           | Small/medium input            |
| `BufferedReader` + `ST` | ✅ Fast       | ✅ Moderate  | ✅ Yes          | Competitive programming (CP)  |
| `DataInputStream`       | 🚀 Very Fast | ❌ Verbose   | ✅ Yes          | CP with huge input            |
| `Console`               | ❌ Limited    | ✅ Easy      | ❌ No           | Secure input (e.g., password) |
| `Scanner` + `File`      | ❌ Slow       | ✅ Easy      | ❌ No           | Testing from input files      |
| `BufferedReader` + `BW` | ✅ Fastest    | ❌ Verbose   | ✅ Yes          | Efficient full I/O            |

---

Let me know your context (e.g., competitive programming, real-world app, or file testing), and I’ll recommend the **best pattern** or write a **custom template**.
----

## Isn't it bad to ... throws Exception on a method for real world application development? Isn't Try catch more recommended? Why is that?

You're absolutely right to ask this. In **real-world Java applications**, there is an important distinction between:

### ✅ `throws Exception`

and

### ✅ `try { ... } catch (...) { ... }`

They serve **different purposes**, and their usage depends on the context (scripts, competitive programming, production code, etc.).

---

## 🔍 What does `throws Exception` do?

```java
public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    ...
}
```

* It tells the compiler:

  > “If any `IOException` happens here, I won’t handle it — I’ll let it propagate up.”

* **Useful when**:

  * You're writing a quick script or test (e.g., for coding contests like CSES, Leetcode).
  * You don’t care about graceful error handling (e.g., if the input is invalid, crash fast).
  * You want simpler code for fast prototyping.

---

## 🔍 What does `try-catch` do?

```java
public static void main(String[] args) {
    try {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ...
    } catch (IOException e) {
        System.err.println("Input error occurred: " + e.getMessage());
    }
}
```

* **Handles** the exception **locally**.

* Lets you log errors, provide user-friendly messages, or recover from issues.

* Often used with `finally` for cleanup:

  ```java
  finally {
      br.close(); // e.g., closing file handles
  }
  ```

* **Essential in real-world apps**:

  * To maintain robustness and prevent crashes.
  * To provide debugging information and logs.
  * To isolate failures and continue running other tasks (like threads or services).

---

## 🔄 When to use which?

| Context                      | Use `throws Exception`         | Use `try-catch`              |
| ---------------------------- | ------------------------------ | ---------------------------- |
| Competitive programming      | ✅ Yes, for brevity             | ❌ Not necessary              |
| Scripts / Internal tools     | ✅ OK                           | ✅ Better if reused           |
| Production web app / service | ❌ No (Never propagate blindly) | ✅ Always handle or log       |
| Libraries / APIs             | ✅ Define custom exceptions     | ✅ Catch or rethrow carefully |
| Android / GUI app            | ❌ Avoid UI crashes             | ✅ Show error dialogs         |

---

## 🧪 Example Comparison

### 1. `throws IOException`

```java
public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int x = Integer.parseInt(br.readLine());
    System.out.println("You entered: " + x);
}
```

### 2. `try-catch`

```java
public static void main(String[] args) {
    try {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        System.out.println("You entered: " + x);
    } catch (IOException e) {
        System.err.println("I/O error: " + e.getMessage());
    } catch (NumberFormatException e) {
        System.err.println("Invalid number: " + e.getMessage());
    }
}
```

---

## ✅ Final Recommendation

* For **real-world development**:
  Use `try-catch` blocks, with appropriate logging and custom exception handling.

* For **contests, quick scripts, or educational code**:
  Use `throws Exception` or `throws IOException` for simplicity and brevity.

Let me know if you'd like a template to structure Java input/output with proper exception handling!

----

