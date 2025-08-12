
### **Midterm Study Guide (期中考试复习指南)**

This guide covers the core concepts from your notes. Focus on understanding these topics, and you will be well-prepared.
本指南涵盖了你笔记中的核心概念。专注于理解这些主题，你就能为考试做好充分准备。

---

#### **1. The Fundamentals: How a Program Works (基础知识：程序如何工作)**

*   **Variables & Data Types (变量 & 数据类型)**
    *   **English:** Variables are containers for storing data. The main data types you need to know are:
        *   **String (`str`):** Text, in quotes (e.g., `"Hello"`, `'A'`).
        *   **Integer (`int`):** Whole numbers (e.g., `10`, `-5`).
        *   **Float (`float`):** Numbers with decimals (e.g., `98.5`, `0.05`).
        *   **Boolean (`bool`):** `True` or `False`.
    *   **中文:** 变量是用来存储数据的容器。你需要知道的主要数据类型有：
        *   **字符串 (`str`):** 文本，用引号括起来 (例如: `"你好"`, `'A'`)。
        *   **整数 (`int`):** 没有小数点的数字 (例如: `10`, `-5`)。
        *   **浮点数 (`float`):** 带小数点的数字 (例如: `98.5`, `0.05`)。
        *   **布尔值 (`bool`):** `True` (真) 或 `False` (假)。

*   **User Input & Output (用户输入 & 输出)**
    *   **English:** `print()` displays information. `input()` gets information from the user. **Important:** `input()` always gives you a **string**. You must use `int()` or `float()` to convert it to a number for calculations. This is called **Type Casting**.
    *   **中文:** `print()` 用于显示信息。`input()` 用于从用户那里获取信息。**重要提示:** `input()` 函数返回的永远是**字符串**。你必须使用 `int()` 或 `float()` 将其转换为数字才能进行数学计算。这个过程叫做**类型转换**。

*   **Basic Operators (基本运算符)**
    *   **English:**
        *   **Arithmetic:** `+`, `-`, `*`, `/`, `%` (remainder/模), `//` (integer division/整除).
        *   **Comparison:** `==` (equals), `!=` (not equals), `>`, `<`, `>=`, `<=`. These always give a `True` or `False` result.
    *   **中文:**
        *   **算术运算符:** `+`, `-`, `*`, `/`, `%` (取余), `//` (整除)。
        *   **比较运算符:** `==` (等于), `!=` (不等于), `>`, `<`, `>=`, `<=`。这些运算符的结果永远是 `True` 或 `False`。

---

#### **2. Making Decisions: Control Flow (做出决策：控制流)**

*   **`if / elif / else` Statements (if / elif / else 语句)**
    *   **English:** This is the main way for your program to make choices. It checks a condition (`if`), if that's false, it checks the next (`elif`), and if all else fails, it does the final part (`else`). Use `and` and `or` to combine conditions.
    *   **中文:** 这是程序做出选择的主要方式。它会检查一个条件 (`if`)，如果该条件为假，则检查下一个条件 (`elif`)，如果所有条件都不满足，则执行最后的部分 (`else`)。使用 `and` 和 `or` 可以组合多个条件。

*   **`match / case` Statements (match / case 语句)**
    *   **English:** A cleaner way to check one variable against many possible specific values. It's like a "switch" statement.
    *   **中文:** 一种更清晰的方式，用于检查单个变量是否等于多个可能的值。类似于其他语言中的 "switch" 语句。

---

#### **3. Repeating Actions: Loops (重复操作：循环)**

*   **`for` Loops (for 循环)**
    *   **English:** Use this when you know how many times you want to loop (e.g., `for i in range(5):`) or when you want to process every item in a collection (e.g., `for question in my_quiz:`).
    *   **中文:** 当你知道要循环多少次时使用 (例如 `for i in range(5):`)，或者当你想处理一个集合中的每一项时使用 (例如 `for question in my_quiz:`)。

*   **`while` Loops (while 循环)**
    *   **English:** Use this when you want to loop as long as a condition is true. It's perfect for waiting for user input, like "keep asking for a number until the user enters 0". The `break` statement is used to exit a loop early.
    *   **中文:** 当你想在某个条件为真的情况下一直循环时使用。它非常适合等待用户输入，比如“一直要求用户输入数字，直到用户输入0为止”。`break` 语句用于提前退出循环。

*   **Nested Loops (嵌套循环)**
    *   **English:** A loop inside another loop. This is essential for creating patterns (like triangles of numbers) and working with grids.
    *   **中文:** 一个循环内部包含另一个循环。这对于创建图形（如数字三角形）和处理网格结构至关重要。

---

#### **4. Organizing Data: Data Structures (组织数据：数据结构)**

*   **Lists `[ ]` (列表)**
    *   **English:** An ordered collection of items. You can add items (`.append()`) and access them by their position (index), starting from 0 (e.g., `my_list[0]`).
    *   **中文:** 一个有序的、可更改的项目集合。你可以添加项目 (`.append()`) 并通过它们的位置（索引）来访问它们，索引从0开始 (例如 `my_list[0]`)。

*   **Dictionaries `{ }` (字典)**
    *   **English:** A collection of `key: value` pairs. Very fast for looking up a value when you know its key (e.g., `quizzes[1]`). Perfect for storing related data, like a state and its capital.
    *   **中文:** 一个由`键: 值`对组成的集合。当你-知道键时，查找对应的值非常快 (例如 `quizzes[1]`)。非常适合存储关联数据，例如一个州和它的首府。

---

#### **5. Writing Robust Code (编写健壮的代码)**

*   **Error Handling: `try / except` (错误处理)**
    *   **English:** This prevents your program from crashing. Put risky code (like `int(input())`) in the `try` block. If an error occurs, the code in the `except` block will run instead.
    *   **中文:** 这可以防止你的程序崩溃。将有风险的代码（如 `int(input())`）放在 `try` 代码块中。如果发生错误，程序会执行 `except` 代码块中的代码，而不是直接崩溃。

*   **Using Modules (e.g., `random`) (使用模块)**
    *   **English:** Modules give you extra functions. You must `import` them first. The `random` module is used for games and simulations.
        *   `random.randint(a, b)`: Get a random integer.
        *   `random.sample(list, k)`: Get `k` unique random items.
    *   **中文:** 模块为你提供额外的功能。你必须先 `import` 它们。`random` 模块用于游戏和模拟。
        *   `random.randint(a, b)`: 获取一个随机整数。
        *   `random.sample(list, k)`: 获取 `k` 个不重复的随机项。

---

### **How to Prepare (如何备考)**

*   **Flowcharts are Key (流程图是关键)**
    *   **English:** Your lecturer provided many flowcharts. This is a big hint. Practice translating a flowchart into Python code, and vice-versa.
    *   **中文:** 你的讲师提供了很多流程图，这是一个重要的提示。练习将流程图翻译成Python代码，反之亦然。

*   **Practice by Hand (动手练习)**
    *   **English:** Don't just read the code. Try to write the programs yourself without looking at the answers. This is the best way to learn.
    *   **中文:** 不要只是阅读代码。尝试自己从头开始编写程序，不要看答案。这是最好的学习方法。

*   **Explain the Concepts (解释概念)**
    *   **English:** Try to explain what a `for` loop is or why you need `try/except` to someone else. If you can teach it, you truly understand it.
    *   **中文:** 尝试向别人解释什么是 `for` 循环，或者为什么需要 `try/except`。如果你能教会别人，说明你真正理解了。
