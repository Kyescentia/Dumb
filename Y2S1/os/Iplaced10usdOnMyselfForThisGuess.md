## **Module 3: Managing Linux Permissions and Ownership / 模块三：管理 Linux 权限和所有权**

EN: This module is about controlling who can access files and what they can do with them. It covers the three core components of file security: ownership, permissions, and user/group management.
中: 本模块关于控制谁可以访问文件以及他们能对文件做什么。它涵盖了文件安全的三个核心组成部分：所有权、权限以及用户/组管理。

### **1. Users, Groups, and Ownership / 用户、组和所有权**

*   **Users / 用户**: EN: Individual accounts on the system. Every user has a unique User ID (UID). The superuser is named `root` and has UID `0`.
    中: 系统上的个人账户。每个用户都有一个唯一的用户ID (UID)。超级用户名为 `root`，其 UID 为 `0`。
*   **Groups / 组**: EN: A collection of users. Every user must belong to at least one primary group. Groups have a unique Group ID (GID).
    中: 用户的集合。每个用户必须至少属于一个主组。组有唯一的组ID (GID)。
*   **Ownership / 所有权**: EN: Every file and directory is owned by exactly one **user** and one **group**.

#### **Important User/Group Information Commands / 重要的用户/组信息命令**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| `id <username>` | EN: Displays a user's UID, primary GID, and all groups they belong to.<br>中: 显示用户的 UID、主 GID 以及他们所属的所有组。 |
| `groups <username>` | EN: Lists only the groups a user is a member of.<br>中: 只列出用户所属的组。 |
| `whoami` | EN: Shows your current effective username.<br>中: 显示你当前的有效用户名。 |

#### **Important Configuration Files / 重要的配置文件**

*   `/etc/passwd`: EN: Stores user account information like username, UID, GID, home directory, and shell. **Does not store the password.**
    中: 存储用户账户信息，如用户名、UID、GID、主目录和 shell。**不存储密码。**
*   `/etc/shadow`: EN: Securely stores encrypted user passwords and password expiration policies. Only readable by `root`.
    中: 安全地存储加密的用户密码和密码过期策略。只有 `root` 可读。
*   `/etc/group`: EN: Defines groups and lists their members.
    中: 定义组并列出其成员。

### **2. File Permissions / 文件权限**

EN: Permissions are checked using the `ls -l` command. The first 10 characters (`-rwxr-xr--`) represent the file type and permissions.
中: 使用 `ls -l` 命令检查权限。前10个字符 (`-rwxr-xr--`) 代表文件类型和权限。

*   **File Type / 文件类型**: The first character. `-` for a file, `d` for a directory, `l` for a symbolic link.
    中: 第一个字符。`-` 代表文件，`d` 代表目录，`l` 代表符号链接。
*   **Permission Groups / 权限组**: The next nine characters are three sets of three.
    1.  **User (Owner) / 用户 (所有者)**: `rwx` (Characters 2-4)
    2.  **Group / 组**: `r-x` (Characters 5-7)
    3.  **Other (Everyone else) / 其他人**: `r--` (Characters 8-10)
*   **Permission Meanings / 权限含义**:
    *   `r` (Read / 读): EN: View file contents or list directory contents.
        中: 查看文件内容或列出目录内容。
    *   `w` (Write / 写): EN: Modify a file or create/delete files within a directory.
        中: 修改文件或在目录内创建/删除文件。
    *   `x` (Execute / 执行): EN: Run a file (if it's a script/program) or enter (`cd` into) a directory.
        中: 运行文件（如果是脚本/程序）或进入 (`cd`) 目录。

### **3. Managing Permissions and Ownership Commands / 管理权限和所有权的命令**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`chmod`** | EN: **Ch**ange **mod**e. Changes permissions. **This is the most important command in this module.**<br>中: **更**改**模**式。更改权限。**这是本模块中最重要的命令。**<br>**Octal (Number) Method / 八进制（数字）方法 (Most likely to be tested / 最可能考):**<br> `r=4`, `w=2`, `x=1`. Add them up for each group (User, Group, Other).<br>_Example / 示例: `chmod 755 script.sh` -> `rwx` for User (4+2+1=7), `r-x` for Group (4+1=5), `r-x` for Other (4+1=5)._<br>**Symbolic (Letter) Method / 符号（字母）方法:**<br> `u` (user), `g` (group), `o` (other), `a` (all). `+` (add), `-` (remove), `=` (set exactly).<br>_Example / 示例: `chmod u+x,g-w script.sh`_ |
| **`chown`** | EN: **Ch**ange **own**er. Changes the user and/or group that owns a file. Requires `root` privileges.<br>中: **更**改**所**有者。更改拥有文件的用户和/或组。需要 `root` 权限。<br>_Example / 示例: `chown jane:staff report.txt` (Changes user to `jane`, group to `staff`)._<br>_Example / 示例: `chown bob report.txt` (Changes only the user to `bob`)._ |
| `chgrp` | EN: **Ch**ange **gr**ou**p**. Changes only the group ownership of a file.<br>中: **更**改**组**。只更改文件的组所有权。 |
| `umask` | EN: Sets the default permissions that are *removed* when creating new files/directories. A `umask` of `022` is common, meaning new directories are `755` and files are `644`.<br>中: 设置创建新文件/目录时被*移除*的默认权限。`022` 的 `umask` 很常见，意味着新目录权限为 `755`，文件为 `644`。 |

### **4. User and Group Management Commands / 用户和组管理命令**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`useradd <user>`** | EN: Adds a new user account.<br>中: 添加一个新用户账户。<br>_Common Option / 常用选项: `-m` (create home directory)._ |
| **`passwd <user>`** | EN: Sets or changes a user's password.<br>中: 设置或更改用户的密码。 |
| `usermod <options> <user>` | EN: Modifies an existing user account. Very useful for adding a user to a group.<br>中: 修改一个已存在的用户账户。常用于将用户添加到一个组。<br>_Example / 示例: `usermod -aG developers john` (Adds user `john` to the `developers` group)._ |
| **`userdel <user>`** | EN: Deletes a user account.<br>中: 删除一个用户账户。<br>_Common Option / 常用选项: `-r` (remove home directory)._ |
| `groupadd <group>` | EN: Adds a new group.<br>中: 添加一个新组。 |
| `groupdel <group>` | EN: Deletes a group.<br>中: 删除一个组。 |

---

## **Module 4: Working with the BASH Shell and Shell Scripts / 模块四：使用 BASH Shell 和 Shell 脚本**

EN: This module covers how to automate tasks by writing scripts, which are simply text files containing a sequence of Linux commands.
中: 本模块涵盖如何通过编写脚本来自动化任务，脚本就是包含一系列 Linux 命令的文本文件。

### **1. Shell Variables / Shell 变量**

*   **Concept / 概念**: EN: A named piece of storage in memory. You assign a value to it and can retrieve it later.
    中: 内存中一个有名字的存储空间。你可以给它赋一个值，之后可以检索它。
*   **Creating Variables / 创建变量**: EN: Use the format `NAME="Value"`. **There must be no spaces around the `=` sign.**
    中: 使用 `NAME="Value"` 的格式。**`=` 号两边绝对不能有空格。**
    *   `MYVAR="Hello World"`
*   **Using Variables / 使用变量**: EN: Precede the name with a dollar sign `$`.
    中: 在变量名前加上美元符号 `$`。
    *   `echo $MYVAR`
*   **Quotes / 引号**:
    *   **Double Quotes `"`**: EN: Allows the shell to interpret variables inside. (`echo "My shell is $SHELL"` -> `My shell is /bin/bash`)
        中: 允许 shell 解析其中的变量。（`echo "My shell is $SHELL"` -> `My shell is /bin/bash`）
    *   **Single Quotes `'`**: EN: Treats every character literally. Disables variable interpretation. (`echo 'My shell is $SHELL'` -> `My shell is $SHELL`)
        中: 将每个字符都视为字面值。禁用变量解析。（`echo 'My shell is $SHELL'` -> `My shell is $SHELL`）

### **2. Creating and Running a Shell Script / 创建并运行 Shell 脚本**

1.  **Create the File / 创建文件**: EN: Use a text editor like `nano` or `vi`.
    中: 使用文本编辑器如 `nano` 或 `vi`。
    *   `nano myscript.sh`
2.  **Add the Shebang / 添加 Shebang**: EN: The **very first line** must be `#!/bin/bash`. This tells the system which interpreter to use.
    中: **第一行**必须是 `#!/bin/bash`。这告诉系统使用哪个解释器。
3.  **Write Commands / 编写命令**: EN: Add commands just as you would type them in the terminal.
    中: 像在终端中输入一样添加命令。
4.  **Make it Executable / 设为可执行**: EN: Use the `chmod` command. This is a critical step.
    中: 使用 `chmod` 命令。这是关键的一步。
    *   **`chmod 755 myscript.sh`** or **`chmod +x myscript.sh`**
5.  **Run the Script / 运行脚本**: EN: Execute it by specifying its path.
    中: 通过指定其路径来执行。
    *   `./myscript.sh` (The `./` means "in the current directory").

### **3. Scripting Constructs and Commands / 脚本结构和命令**

| Concept / 概念 | Description / 描述 |
| :--- | :--- |
| **`echo`** | EN: The most important command for printing text or variable values to the screen.<br>中: 用于在屏幕上打印文本或变量值的最重要命令。 |
| **Positional Parameters / 位置参数** | EN: How a script receives arguments from the command line.<br>中: 脚本从命令行接收参数的方式。<br>`$0`: The script's name / 脚本名<br>`$1`: First argument / 第一个参数<br>`$2`: Second argument / 第二个参数<br>`$#`: The total number of arguments / 参数总数<br>`$@`: All arguments as a list / 所有参数（列表形式） |
| **`if` statement / `if` 语句** | EN: For making decisions. **The spaces around `[` and `]` are mandatory.**<br>中: 用于做判断。**`[` 和 `]` 两边的空格是强制性的。**<br>_Syntax / 语法:_<br>`if [ condition ]; then`<br>  `... commands ...`<br>`elif [ another_condition ]; then`<br>  `... other commands ...`<br>`else`<br>  `... commands ...`<br>`fi` |
| **Test Conditions / 测试条件** | EN: Used inside the `[ ... ]` of an `if` statement.<br>中: 用于 `if` 语句的 `[ ... ]` 内部。<br>**String Comparison / 字符串比较:** `"$VAR1" = "$VAR2"` (equal), `"$VAR1" != "$VAR2"` (not equal)<br>**Number Comparison / 数字比较:** `-eq` (equal), `-ne` (not equal), `-gt` (greater than), `-lt` (less than)<br>**File Checks / 文件检查:** `-f` (is a file), `-d` (is a directory), `-e` (exists) |
| **`for` loop / `for` 循环** | EN: Repeats a block of code for each item in a list.<br>中: 对列表中的每个项目重复执行一段代码块。<br>_Syntax / 语法:_<br>`for VAR in item1 item2 item3; do`<br>  `echo $VAR`<br>`done` |
| `case` statement / `case` 语句 | EN: A cleaner way to handle multiple `if/elif` conditions for a single variable.<br>中: 一种更清晰的方式来处理针对单个变量的多个 `if/elif` 条件。<br>_Syntax / 语法:_<br>`case "$VAR" in`<br>  `pattern1) commands;;`<br>  `pattern2) commands;;`<br>  `*) default_commands;;`<br>`esac` |
| `read` | EN: Prompts the user for input and stores it in a variable.<br>中: 提示用户输入并将其存储在一个变量中。<br>_Example / 示例: `echo "Enter your name:"; read USER_NAME`_ |
