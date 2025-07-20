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
