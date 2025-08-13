
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
         ```python
        # Input (gets a string)
        user_name = input("Enter your name: ")
        
        # Output
        print("Hello,", user_name)

        # Type Casting for math
        age_str = input("Enter your age: ")
        age_num = int(age_str) # Convert to integer
        print("Next year you will be", age_num + 1)
        ```
    *   **中文:** `print()` 用于显示信息。`input()` 用于从用户那里获取信息。**重要提示:** `input()` 函数返回的永远是**字符串**。你必须使用 `int()` 或 `float()` 将其转换为数字才能进行数学计算。这个过程叫做**类型转换**。
         ```python
        # 输入 (获取字符串)
        user_name = input("请输入你的名字: ")
        
        # 输出
        print("你好,", user_name)

        # 用于计算的类型转换
        age_str = input("请输入你的年龄: ")
        age_num = int(age_str) # 转换为整数
        print("明年你就", age_num + 1, "岁了")
        ```

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
         ```python
        score = 85
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B") # This will run
        else:
            print("Grade: C or below")
        ```
    *   **中文:** 这是程序做出选择的主要方式。它会检查一个条件 (`if`)，如果该条件为假，则检查下一个条件 (`elif`)，如果所有条件都不满足，则执行最后的部分 (`else`)。使用 `and` 和 `or` 可以组合多个条件。
         ```python
        score = 85
        if score >= 90:
            print("等级: A")
        elif score >= 80:
            print("等级: B") # 这段代码将会运行
        else:
            print("等级: C或以下")
        ```

*   **`match / case` Statements (match / case 语句)**
   ### **When to Use `match/case`**

   *   **BEST for:** Checking a single variable against multiple **specific, exact values**.
   *   **NOT for:** Checking ranges (e.g., `score > 90`). For ranges, a standard `if/elif/else` is still the best tool.

   ### **何时使用 `match/case`**

   *   **最适合用于：** 将 **单个变量** 与多个 **特定的、精确的值** 进行比较。
   *   **不适合用于：** 检查范围 (例如 `score > 90`)。对于范围检查，标准的 `if/elif/else` 仍然是最好的工具。
   
   *   **English:** A cleaner way to check one variable against many possible specific values. It's like a "switch" statement.
         **The `if/elif/else` Way:**
         ```python
            choice = "2"
            
            if choice == "1":
                print("Viewing Profile.")
            elif choice == "2":
                print("Editing Settings.")
            elif choice == "3":
                print("Logging Out`.")
            else:
                print("Invalid choice!")
            # Output: Editing Settings.
         ```
         
         **The `match/case` Way (Cleaner):**
         ```python
         choice = "2"
         
         match choice:
             case "1":
                 print("Viewing Profile.")
             case "2":
                 print("Editing Settings.")
             case "3":
                 print("Logging Out.")
             case _:  # The underscore `_` is a wildcard, acting like 'else'
                 print("Invalid choice!")
         # Output: Editing Settings.
         ```
   *   **中文:** 一种更清晰的方式，用于检查单个变量是否等于多个可能的值。类似于其他语言中的 "switch" 语句。
       **使用 `if/elif/else` 的方法:**
       ```python
         choice = "2"
         
         if choice == "1":
             print("查看个人资料 (Viewing Profile)。")
         elif choice == "2":
             print("编辑设置 (Editing Settings)。")
         elif choice == "3":
             print("登出 (Logging Out)。")
         else:
             print("无效选择 (Invalid choice)!")
         # 输出: 编辑设置 (Editing Settings)。
       ```
   
       **使用 `match/case` 的方法 (更简洁):**
       ```python
         choice = "2"
         
         match choice:
             case "1":
                 print("查看个人资料 (Viewing Profile)。")
             case "2":
                 print("编辑设置 (Editing Settings)。")
             case "3":
                 print("登出 (Logging Out)。")
             case _:  # 这个下划线 `_` 是一个通配符 (wildcard)，作用类似于 'else'
                 print("无效选择 (Invalid choice)!")
         # 输出: 编辑设置 (Editing Settings)。
       ```
   
   #### **Advanced Features: Combining Cases with `|`**
   
   A powerful feature is using the `|` (OR) symbol to combine multiple cases that should do the same thing. This is taken from the grading example in your notes.
   
   **The `if/elif/else` Way:**
   ```python
   grade = 'B'
   
   if grade == 'A' or grade == 'F':
       print("You got an", grade, "for the test!")
   elif grade == 'B' or grade == 'C' or grade == 'D':
       print("You got a", grade, "for the test!")
   ```
   
   **The `match/case` Way:**
   ```python
   grade = 'B'
   
   match grade:
       case 'A' | 'F':  # Matches if grade is 'A' OR 'F'
           print("You got an", grade, "for the test!")
           
       case 'B' | 'C' | 'D': # Matches if grade is 'B' OR 'C' OR 'D'
           print("You got a", grade, "for the test!")
   ```

   #### **高级功能：使用 `|` 合并条件**

   一个强大的功能是使用 `|` (或) 符号来合并多个应该执行相同操作的 `case`。这个例子来自你笔记中的成绩评定。
   
   **使用 `if/elif/else` 的方法:**
   ```python
   grade = 'B'
   
   if grade == 'A' or grade == 'F':
       print("你在这次考试中得到了一个 (an)", grade)
   elif grade == 'B' or grade == 'C' or grade == 'D':
       print("你在这次考试中得到了一个 (a)", grade)
   ```
   
   **使用 `match/case` 的方法:**
   ```python
   grade = 'B'
   
   match grade:
       case 'A' | 'F':  # 如果 grade 是 'A' 或 (OR) 'F'，则匹配
           print("你在这次考试中得到了一个 (an)", grade)
           
       case 'B' | 'C' | 'D': # 如果 grade 是 'B' 或 'C' 或 'D'，则匹配
           print("你在这次考试中得到了一个 (a)", grade)
   ```

---

#### **3. Repeating Actions: Loops (重复操作：循环)**

*   **`for` Loops (for 循环)**
    *   **English:** Use this when you know how many times you want to loop (e.g., `for i in range(5):`) or when you want to process every item in a collection (e.g., `for question in my_quiz:`).
         ```python
        # Loop 3 times (prints 0, 1, 2)
        for i in range(3):
            print("Loop number", i)

        # Loop through a list
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print("I like", fruit)
        ```
    *   **中文:** 当你知道要循环多少次时使用 (例如 `for i in range(5):`)，或者当你想处理一个集合中的每一项时使用 (例如 `for question in my_quiz:`)。
         ```python
        # 循环3次 (打印 0, 1, 2)
        for i in range(3):
            print("循环次数", i)

        # 遍历列表
        fruits = ["苹果", "香蕉", "樱桃"]
        for fruit in fruits:
            print("我喜欢", fruit)
        ```

*   **`while` Loops (while 循环)**
    *   **English:** Use this when you want to loop as long as a condition is true. It's perfect for waiting for user input, like "keep asking for a number until the user enters 0". The `break` statement is used to exit a loop early.
         ```python
        command = ""
        while command != "quit":
            command = input("Enter 'quit' to exit: ")
            print("You typed:", command)
        print("Goodbye!")
        ```
    *   **中文:** 当你想在某个条件为真的情况下一直循环时使用。它非常适合等待用户输入，比如“一直要求用户输入数字，直到用户输入0为止”。`break` 语句用于提前退出循环。
         ```python
        command = ""
        while command != "quit":
            command = input("输入 'quit' 退出: ")
            print("你输入了:", command)
        print("再见!")
        ```

*   **Nested Loops (嵌套循环)**
    *   **English:** A loop inside another loop. This is essential for creating patterns (like triangles of numbers) and working with grids.
         ```python
        # Prints a 3x3 grid of coordinates
        for i in range(3):      # Outer loop (rows)
            for j in range(3):  # Inner loop (columns)
                print(f"({i},{j})", end=" ")
            print() # New line after each row
        ```
    *   **中文:** 一个循环内部包含另一个循环。这对于创建图形（如数字三角形）和处理网格结构至关重要。
         ```python
        # 打印一个3x3的坐标网格
        for i in range(3):      # 外层循环 (行)
            for j in range(3):  # 内层循环 (列)
                print(f"({i},{j})", end=" ")
            print() # 每行结束后换行
        ```
---

#### **4. Organizing Data: Data Structures (组织数据：数据结构)**

*   **Lists `[ ]` (列表)**
    *   **English:** An ordered collection of items. You can add items (`.append()`) and access them by their position (index), starting from 0 (e.g., `my_list[0]`).
         ```python
        scores = [88, 92, 75]
        scores.append(100) # Add an item
        print("First score:", scores[0]) # Prints 88
        print("All scores:", scores) # [88, 92, 75, 100]
        ```
    *   **中文:** 一个有序的、可更改的项目集合。你可以添加项目 (`.append()`) 并通过它们的位置（索引）来访问它们，索引从0开始 (例如 `my_list[0]`)。
         ```python
        scores = [88, 92, 75]
        scores.append(100) # 添加一个项目
        print("第一个分数:", scores[0]) # 打印 88
        print("所有分数:", scores) # [88, 92, 75, 100]
        ```

*   **Dictionaries `{ }` (字典)**
    *   **English:** A collection of `key: value` pairs. Very fast for looking up a value when you know its key (e.g., `quizzes[1]`). Perfect for storing related data, like a state and its capital.
         ```python
        # Key: Value
        student = {
            "name": "David",
            "id": 12345,
            "major": "Computer Science"
        }
        print(student["name"]) # Looks up the key "name" and prints "David"
        ```
    *   **中文:** 一个由`键: 值`对组成的集合。当你-知道键时，查找对应的值非常快 (例如 `quizzes[1]`)。非常适合存储关联数据，例如一个州和它的首府。
         ```python
        # 键: 值
        student = {
            "name": "大卫",
            "id": 12345,
            "major": "计算机科学"
        }
        print(student["name"]) # 查找键"name"并打印"大卫"
        ```

---

#### **5. Writing Robust Code (编写健壮的代码)**

*   **Error Handling: `try / except` (错误处理)**
    *   **English:** This prevents your program from crashing. Put risky code (like `int(input())`) in the `try` block. If an error occurs, the code in the `except` block will run instead.
         ```python
        try:
            age = int(input("Enter your age: "))
            print("You are", age, "years old.")
        except ValueError:
            # This runs if the user types text instead of a number
            print("Invalid input! Please enter a number.")
        ```
    *   **中文:** 这可以防止你的程序崩溃。将有风险的代码（如 `int(input())`）放在 `try` 代码块中。如果发生错误，程序会执行 `except` 代码块中的代码，而不是直接崩溃。
         ```python
        try:
            age = int(input("请输入你的年龄: "))
            print("你今年", age, "岁。")
        except ValueError:
            # 如果用户输入了文本而不是数字，这部分代码会运行
            print("无效输入！请输入一个数字。")
        ```

*   **Using Modules (e.g., `random`) (使用模块)**
    *   **English:** Modules give you extra functions. You must `import` them first. The `random` module is used for games and simulations.
        *   `random.randint(a, b)`: Get a random integer.
        *   `random.sample(list, k)`: Get `k` unique random items.
         ```python
        import random

        # Get a random integer between 1 and 6 (like a dice)
        dice_roll = random.randint(1, 6)
        print("You rolled a", dice_roll)
        ```
    *   **中文:** 模块为你提供额外的功能。你必须先 `import` 它们。`random` 模块用于游戏和模拟。
        *   `random.randint(a, b)`: 获取一个随机整数。
        *   `random.sample(list, k)`: 获取 `k` 个不重复的随机项。
         ```python
        import random

        # 获取一个1到6之间的随机整数 (像掷骰子)
        dice_roll = random.randint(1, 6)
        print("你掷出了", dice_roll)
        ```

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
