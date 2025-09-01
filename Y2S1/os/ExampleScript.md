

### **Scripting Examples for Module 4 / 模块四脚本示例**

#### **1. Variables and `echo` / 变量和 `echo`**
EN: The most basic script: defining variables and printing them.
中: 最基础的脚本：定义变量并打印它们。

**Script Name / 脚本名:** `user_info.sh`

```bash
#!/bin/bash

# 1. Define a variable with a string value.
#    定义一个值为字符串的变量。
USERNAME="Alice"

# 2. Define a variable with a number value.
#    定义一个值为数字的变量。
USER_ID=1001

# 3. Use 'echo' to print static text and variables.
#    使用 'echo' 打印静态文本和变量。
#    Double quotes "" are used so the shell can read the variable's value.
#    使用双引号 "" 以便 shell 可以读取变量的值。
echo "User Information:"
echo "-----------------"
echo "Username is: $USERNAME"
echo "User ID is: $USER_ID"

# 4. Single quotes '' treat everything literally. The variable will not be read.
#    单引号 '' 将所有内容视为字面值。变量不会被读取。
echo 'This will print the literal text: $USERNAME'
```

**How to Run and Expected Output / 如何运行及预期输出:**

```bash
$ chmod +x user_info.sh
$ ./user_info.sh

User Information:
-----------------
Username is: Alice
User ID is: 1001
This will print the literal text: $USERNAME
```

---

#### **2. Positional Parameters (`$1`, `$#`, `$@`) / 位置参数**
EN: A script that processes arguments given to it on the command line.
中: 一个处理从命令行传递给它的参数的脚本。

**Script Name / 脚本名:** `arg_checker.sh`

```bash
#!/bin/bash

# This script demonstrates how to use command-line arguments.
# 本脚本演示如何使用命令行参数。

# $0 is the name of the script itself.
# $0 是脚本本身的名字。
echo "The script being run is: $0"

# $1 is the first argument, $2 is the second, etc.
# $1 是第一个参数，$2 是第二个，以此类推。
echo "The first argument is: $1"
echo "The second argument is: $2"

# $# is the total number of arguments passed to the script.
# $# 是传递给脚本的参数总数。
echo "You provided $# arguments in total."

# $@ represents all arguments as a list.
# $@ 代表所有参数，形式为一个列表。
echo "All the arguments are: $@"
```

**How to Run and Expected Output / 如何运行及预期输出:**

```bash
$ chmod +x arg_checker.sh
$ ./arg_checker.sh hello world 123

The script being run is: ./arg_checker.sh
The first argument is: hello
The second argument is: world
You provided 3 arguments in total.
All the arguments are: hello world 123
```

---

#### **3. `if` Statement (Decision Making) / `if` 语句 (做判断)**
EN: A script that checks if a file exists. This is a very common test scenario.
中: 一个检查文件是否存在的脚本。这是一个非常常见的考试场景。

**Script Name / 脚本名:** `file_exists.sh`

```bash
#!/bin/bash

# This script checks if the file provided as the first argument ($1) exists.
# 本脚本检查作为第一个参数 ($1) 提供的文件是否存在。

# Check if an argument was provided. -z checks for a null/empty string.
# 检查是否提供了参数。-z 检查是否为空字符串。
if [ -z "$1" ]; then
  echo "Error: Please provide a filename as an argument."
  exit 1 # Exit with an error code
fi

# The main condition: -f checks if the path exists and is a regular file.
# 主要条件：-f 检查路径是否存在且为普通文件。
# The spaces around [ and ] are MANDATORY!
# [ 和 ] 两边的空格是强制性的！
if [ -f "$1" ]; then
  # This block runs if the condition is true.
  # 如果条件为真，则运行此代码块。
  echo "Success: The file '$1' exists."
else
  # This block runs if the condition is false.
  # 如果条件为假，则运行此代码块。
  echo "Failure: The file '$1' does not exist."
fi
```

**How to Run and Expected Output / 如何运行及预期输出:**

```bash
$ touch testfile.txt  # Create a file to test with
$ chmod +x file_exists.sh

# First run (Success case)
$ ./file_exists.sh testfile.txt
Success: The file 'testfile.txt' exists.

# Second run (Failure case)
$ ./file_exists.sh non_existent_file.txt
Failure: The file 'non_existent_file.txt' does not exist.

# Third run (Error case)
$ ./file_exists.sh
Error: Please provide a filename as an argument.
```

---

#### **4. `for` Loop (Repetition) / `for` 循环 (重复)**
EN: A script that loops through all its arguments and performs an action.
中: 一个遍历其所有参数并执行操作的脚本。

**Script Name / 脚本名:** `backup_files.sh`

```bash
#!/bin/bash

# This script takes a list of filenames as arguments and "backs them up"
# by copying them with a .bak extension.
# 本脚本接收一个文件名列表作为参数，并通过复制它们并添加 .bak 扩展名来“备份”它们。

# "$@" is special. It expands to a list of all positional parameters.
# "$@" 是特殊的。它会展开为所有位置参数的列表。
for FILENAME in "$@"
do
  # The 'do...done' block is executed for each item in the list.
  # 'do...done' 代码块会对列表中的每个项目执行一次。
  echo "Backing up '$FILENAME' to '$FILENAME.bak'..."
  cp "$FILENAME" "$FILENAME.bak"
done

echo "------------------"
echo "Backup complete!"
```

**How to Run and Expected Output / 如何运行及预期输出:**

```bash
$ touch file1.txt file2.log  # Create some files
$ chmod +x backup_files.sh
$ ./backup_files.sh file1.txt file2.log

Backing up 'file1.txt' to 'file1.txt.bak'...
Backing up 'file2.log' to 'file2.log.bak'...
------------------
Backup complete!

$ ls
backup_files.sh  file1.txt  file1.txt.bak  file2.log  file2.log.bak
```

---

#### **5. `read` (Interactive Input) / `read` (交互式输入)**
EN: A script that asks the user a question and uses their answer.
中: 一个向用户提问并使用其答案的脚本。

**Script Name / 脚本名:** `greeter.sh`

```bash
#!/bin/bash

# This script asks for the user's name and greets them.
# 本脚本询问用户的名字并向他们问好。

# Use 'echo -n' to print text without a newline at the end.
# 使用 'echo -n' 打印文本，末尾不带换行符。
echo -n "Please enter your name: "

# 'read' waits for the user to type something and press Enter.
# 'read' 会等待用户输入内容并按 Enter 键。
# The input is stored in the variable specified (USER_NAME).
# 输入的内容被存储在指定的变量 (USER_NAME) 中。
read USER_NAME

# Now we can use the variable that contains the user's input.
# 现在我们可以使用包含用户输入的变量了。
echo "Hello, $USER_NAME! Welcome to the system."
```

**How to Run and Expected Output / 如何运行及预期输出:**

```bash
$ chmod +x greeter.sh
$ ./greeter.sh

Please enter your name: Bob  <-- (You type "Bob" and press Enter)
Hello, Bob! Welcome to the system.
```
