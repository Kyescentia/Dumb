
### Midterm Study Guide: Core Programming Concepts


---

#### 1. The Fundamentals: How a Program Works

This is the foundation. Every single program you write will use these ideas.

*   **Variables & Data Types:**
    *   **What they are:** Variables are containers for storing data. Each piece of data has a *type*.
    *   **What to know:**
        *   **String (`str`):** Text, always in quotes (e.g., `"Hello"`, `'A'`).
        *   **Integer (`int`):** Whole numbers (e.g., `10`, `-5`, `0`).
        *   **Float (`float`):** Numbers with decimals (e.g., `98.5`, `0.05`).
        *   **Boolean (`bool`):** Represents truth, can only be `True` or `False`.

*   **User Input & Output:**
    *   **What they are:** How your program communicates with the user.
    *   **What to know:**
        *   `print()`: Displays information to the user.
        *   `input()`: Gets information **from** the user. **Important:** `input()` always returns a string, even if the user types a number.
        *   **Type Casting:** You must convert the input string to a number using `int()` or `float()` if you want to do math with it (e.g., `score = int(input("Enter score: "))`).

*   **Basic Operators:**
    *   **Arithmetic:** `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `**` (exponent), `%` (modulo/remainder), `//` (integer division).
    *   **Comparison:** `==` (is equal to), `!=` (is not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to). These always result in a `True` or `False` boolean value.

---

#### 2. Making Decisions: Control Flow

This is how your program becomes "smart" and can do different things in different situations.

*   **`if / elif / else` Statements:**
    *   **What they are:** The primary way to execute code blocks conditionally.
    *   **When to use:**
        *   `if`: Checks the first condition.
        *   `elif`: Checks a new condition if the previous `if` or `elif` was false. You can have many of these.
        *   `else`: Runs if **none** of the preceding conditions were true.
    *   **Logical Operators:** You will need to combine conditions with `and` (both must be true) and `or` (at least one must be true).

*   **`match / case` Statements:**
    *   **What it is:** A cleaner, alternative way to handle multiple checks against a single variable's value.
    *   **When to use:** It's perfect when you have a variable and want to do something different for each of its possible, specific values (e.g., if a variable is 1, do this; if it's 2, do that...).

---

#### 3. Repeating Actions: Loops

Loops allow you to run code multiple times without copying and pasting it.

*   **`for` Loops (Definite Iteration):**
    *   **What it is:** A loop that runs a specific number of times.
    *   **When to use:** When you know how many times you need to loop, or when you want to do something "for each item" in a collection (like a list or dictionary).
    *   **Key Syntax:** `for i in range(5):` (loops 5 times, `i` will be 0, 1, 2, 3, 4) and `for item in my_list:`.

*   **`while` Loops (Indefinite Iteration):**
    *   **What it is:** A loop that continues as long as its condition is `True`.
    *   **When to use:** When you don't know how many times you'll need to loop. A classic use is asking for user input until they type "quit".
    *   **Key Syntax:** `while score != -1:`. You must ensure the condition eventually becomes false, or you'll have an infinite loop!
    *   **`break` statement:** Used to exit a loop immediately, even if the loop's condition is still true. This is often used inside an `if` statement within a loop.

*   **Nested Loops:**
    *   **What it is:** A loop inside another loop.
    *   **What to know:** The inner loop completes all its iterations for *each single iteration* of the outer loop. This is essential for creating patterns (like triangles of stars or numbers) and working with grids.

---

#### 4. Organizing Data: Data Structures

These are specialized containers for storing and managing collections of related data.

*   **Lists `[ ]`:**
    *   **What it is:** An ordered, changeable collection of items.
    *   **What to know:**
        *   Create with `my_list = [1, 2, 3]`.
        *   Add items with `.append()`.
        *   Access items by index: `my_list[0]` (the first item).
        *   Useful functions: `len()` (to get the length), `sorted()` (to get a sorted copy).

*   **Dictionaries `{ }`:**
    *   **What it is:** An unordered collection of `key: value` pairs.
    *   **What to know:**
        *   Create with `my_dict = {'state': 'California', 'capital': 'Sacramento'}`.
        *   Extremely fast for looking up a value if you know the key: `my_dict['state']`.
        *   Great for things like quizzes (question number is key, question/answer is value) or storing related properties of an object.

---

#### 5. Writing Robust Code

These skills make your programs more professional and less likely to crash.

*   **Error Handling with `try / except`:**
    *   **What it is:** A way to "catch" errors that would normally crash your program.
    *   **When to use:** The most common use is when converting user input to a number. If the user types "abc", `int("abc")` will cause a `ValueError`.
    *   **How it works:** Put the risky code in the `try` block. If an error occurs, the code in the `except` block runs instead of the program crashing.

*   **Using Modules (like `random`):**
    *   **What it is:** Modules are files of pre-written code you can bring into your program.
    *   **What to know:**
        *   Use `import random` at the top of your file.
        *   `random.randint(a, b)`: Gets a random integer.
        *   `random.sample(list, k)`: Gets `k` unique random items from a list.
        *   `random.shuffle(list)`: Randomly shuffles the items in a list.

### How to Prepare

*   **Flowcharts are Key:** Your lecturer included many flowcharts. This is a big hint. Be prepared to **read a flowchart and write the Python code for it**, or vice-versa. Practice translating the diamond shapes (`if/else`) and loops into code.
*   **Practice by Hand:** Don't just read the code. Open a blank editor or take a piece of paper and try to write the programs from scratch. Try to build a simple grading program or a number-guessing game.
*   **Explain the Concepts:** Try to explain what a `for` loop is and when you'd use it to a friend or family member. If you can teach it, you understand it.
