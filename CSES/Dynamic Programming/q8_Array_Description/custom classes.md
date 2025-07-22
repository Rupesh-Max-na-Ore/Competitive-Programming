## How to create custom error class in java?

In Java, you can create a **custom error or exception class** by extending either:

* `Exception` → for **checked exceptions** (must be declared or caught), or
* `RuntimeException` → for **unchecked exceptions** (do not need to be declared or caught).

---

## 🔧 Step-by-Step: Creating a Custom Exception Class

### ✅ Syntax 1: Custom Checked Exception

```java
// This must be caught or declared with `throws`
public class InvalidUserInputException extends Exception {
    public InvalidUserInputException(String message) {
        super(message);
    }

    public InvalidUserInputException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

### ✅ Syntax 2: Custom Unchecked Exception

```java
// Runtime exception - can optionally be caught
public class ResourceConflictException extends RuntimeException {
    public ResourceConflictException(String message) {
        super(message);
    }

    public ResourceConflictException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

---

## 🔍 When to use each?

| Base class         | Type      | Must be caught or declared? | Use case examples                             |
| ------------------ | --------- | --------------------------- | --------------------------------------------- |
| `Exception`        | Checked   | ✅ Yes                       | Validation, file not found, business rules    |
| `RuntimeException` | Unchecked | ❌ No                        | Illegal state, logic errors, null dereference |

---

## 🧪 Example Usage

```java
public class Demo {
    public static void main(String[] args) {
        try {
            validateAge(-5);
        } catch (InvalidUserInputException e) {
            System.err.println("Caught Exception: " + e.getMessage());
        }
    }

    public static void validateAge(int age) throws InvalidUserInputException {
        if (age < 0 || age > 150) {
            throw new InvalidUserInputException("Age must be between 0 and 150");
        }
        System.out.println("Age is valid");
    }
}
```

---

## ✅ Good Practices

* Always subclass `Exception` or `RuntimeException`, **not** `Throwable` or `Error`.
* Include multiple constructors:

  * `String message`
  * `String message, Throwable cause`
* Use custom exceptions to **signal specific, semantic errors** in your domain logic.
* Avoid overusing checked exceptions — they clutter signatures; use when recovery is expected.

---

Would you like a template for custom exceptions in a layered application (controller/service/repository)?

---

## What is checked and unchecked exception? Give examples with code.

In **Java**, exceptions are classified into **checked** and **unchecked** exceptions. This classification is based on how the compiler enforces exception handling.

---

### ✅ Definition

| Type                    | Description                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Checked Exception**   | Exceptions that must be declared in the method signature using `throws`, or caught using `try-catch`. Checked at **compile time**. |
| **Unchecked Exception** | Subclasses of `RuntimeException`. Not checked at compile time. Can be handled optionally.                                          |

---

## 1. ✅ Checked Exception (Compile-Time)

### 🔹 Common Examples:

* `IOException`
* `SQLException`
* `ParseException`

### 📌 Code Example

```java
import java.io.*;

public class CheckedExample {
    public static void main(String[] args) {
        try {
            readFile("data.txt");
        } catch (IOException e) {
            System.out.println("Caught IOException: " + e.getMessage());
        }
    }

    // Must declare IOException (checked)
    public static void readFile(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line = reader.readLine();
        System.out.println(line);
        reader.close();
    }
}
```

If you do **not** catch or declare the exception, the compiler gives an error.

---

## 2. ❌ Unchecked Exception (Runtime)

### 🔹 Common Examples:

* `NullPointerException`
* `ArithmeticException`
* `ArrayIndexOutOfBoundsException`
* `IllegalArgumentException`

### 📌 Code Example

```java
public class UncheckedExample {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        printElement(arr, 5); // Index out of bounds
    }

    public static void printElement(int[] arr, int index) {
        // No need to declare or catch the exception
        System.out.println(arr[index]);
    }
}
```

Even though an `ArrayIndexOutOfBoundsException` might occur, it **does not need** to be declared or caught.

---

## ✅ Summary Table

| Feature                | Checked Exception             | Unchecked Exception                                |
| ---------------------- | ----------------------------- | -------------------------------------------------- |
| Compile-time check     | ✅ Yes                         | ❌ No                                               |
| Subclass of            | `Exception` (not Runtime)     | `RuntimeException`                                 |
| Must declare or catch? | ✅ Yes                         | ❌ No (optional)                                    |
| Examples               | `IOException`, `SQLException` | `NullPointerException`, `IllegalArgumentException` |
| Best Use Case          | Expected external failures    | Programming bugs, logical errors                   |

---

Would you like a custom diagram or mnemonic to help remember this better?
