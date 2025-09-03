### **Linux Lifesaver Commands: Getting Help / Linux "救命"命令：获取帮助**

EN: These are the most important commands in Linux. Master them, and you can find the answer to almost anything without leaving the terminal.
中: 这些是 Linux 中最重要的命令。掌握它们，你几乎可以在不离开终端的情况下找到任何问题的答案。

#### **1. The Ultimate Lifesaver: When You Don't Know the Command Name / 终极救星：当你不知道命令名称时**

*   **`apropos <keyword>`** (or `man -k <keyword>`)
    *   EN: **This is your most important discovery tool.** Use it when you know *what you want to do* but don't know the command. It searches the one-line descriptions of all commands for your keyword.
    *   中: **这是你最重要的发现工具。** 当你知道*你想做什么*但不知道具体命令时，就用它。它会搜索所有命令的单行描述来查找你的关键字。
    *   Example / 示例: `apropos "copy file"`

#### **2. When You Know the Command Name / 当你知道命令名称时**

*   **`man <command>`**
    *   EN: The **man**ual. Once `apropos` helps you find a command, use `man` to learn how to use it. It provides the full, official documentation.
    *   中: **man**ual (手册)。一旦 `apropos` 帮你找到了命令，就用 `man` 来学习如何使用它。它提供完整、官方的文档。
    *   **Navigation / 导航**: Use arrow keys to scroll, `/` to search, and `q` to quit. / 使用箭头键滚动，用 `/` 搜索，按 `q` 退出。

*   **`<command> --help`**
    *   EN: A faster alternative to `man`. It prints a quick summary of a command's most common options.
    *   中: `man` 的一个更快替代方案。它打印出命令最常用选项的快速摘要。

#### **3. Other Essential Help Commands / 其他核心帮助命令**

*   `whatis <command>`
    *   EN: Gives a very brief, one-line description of what a command does.
    *   中: 提供一个关于命令作用的非常简短的单行描述。
*   `whereis <command>`
    *   EN: Tells you where the command's program file is located on the system.
    *   中: 告诉你命令的程序文件在系统中的位置。
*   `info <command>`
    *   EN: Displays detailed command information, often more narrative than `man`.
    *   中: 显示详细的命令信息，通常比 `man` 更具叙述性。

---

## **Module 1: Performing Basic Linux Tasks / 模块一：执行基本 Linux 任务**

### **1. UNIX vs. Linux / UNIX 与 Linux**
*   **UNIX**: EN: Closed-source, proprietary OS. / 中: 闭源、专有操作系统。
*   **Linux**: EN: Open-source, "copyleft" OS based on UNIX. / 中: 基于 UNIX 的开源、“写反”操作系统。

### **2. Key Concepts: Kernel and Shell / 关键概念：内核与 Shell**
*   **Kernel / 内核**: EN: The core of the OS, manages hardware. / 中: 操作系统的核心，管理硬件。
*   **Shell / 外壳 (Shell)**: EN: The command-line interface between you and the kernel. / 中: 你与内核之间的命令行界面。

### **3. Essential System & Navigation Commands / 核心系统与导航命令**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`pwd`** | EN: **P**rint **W**orking **D**irectory (shows your current location).<br>中: **打**印**工**作**目**录（显示您当前的位置）。 |
| **`ls`** | EN: **L**i**s**t files and directories. Common options: `-l` (long format), `-a` (all files).<br>中: **列**出文件和目录。常用选项: `-l` (长格式), `-a` (所有文件)。 |
| **`cd <dir>`** | EN: **C**hange **D**irectory. Special args: `..` (up one level), `~` (home), `/` (root).<br>中: **切**换**目**录。特殊参数: `..` (上一级), `~` (主目录), `/` (根目录)。 |
| **`whoami`** | EN: Displays your current username.<br>中: 显示您当前的用户名。 |
| `who` | EN: Displays who is currently logged into the system.<br>中: 显示当前登录到系统的用户。 |
| `w` | EN: A more detailed version of `who`, showing what users are doing.<br>中: `who` 命令的更详细版本，显示用户正在做什么。 |
| `id` | EN: Displays user and group ID information.<br>中: 显示用户和组的 ID 信息。 |
| `date` | EN: Displays the current date and time.<br>中: 显示当前日期和时间。 |
| `cal` | EN: Displays a calendar for the current month.<br>中: 显示当前月份的日历。 |
| `uname` | EN: Prints system information (kernel name, version, etc.).<br>中: 打印系统信息（内核名称、版本等）。 |
| **`clear`** | EN: Clears the terminal screen.<br>中: 清除终端屏幕。 |
| `reset` | EN: Resets the terminal to its default settings.<br>中: 将终端重置为默认设置。 |
| **`exit`** | EN: Logs out of the current shell session.<br>中: 退出当前的 shell 会话。 |
| `shutdown` | EN: A versatile command to shut down or reboot, allowing for timed shutdowns.<br>中: 一个灵活的关机或重启命令，允许定时关机。 |
| `reboot` | EN: Reboots the system (requires admin privileges).<br>中: 重启系统（需要管理员权限）。 |
| `poweroff` | EN: Shuts down the system (requires admin privileges).<br>中: 关闭系统（需要管理员权限）。 |
| `halt` | EN: Halts the system without powering it off.<br>中: 停止系统但不关闭电源。 |

---

## **Module 2: Managing Files in Linux / 模块二：管理 Linux 文件**

### **1. Wildcards for File Matching / 用于文件匹配的通配符**

EN: Wildcards are special characters that help you select multiple files at once.
中: 通配符是帮助您一次选择多个文件的特殊字符。

| Wildcard / 通配符 | Name / 名称 | Description / 描述 |
| :--- | :--- | :--- |
| **`*`** | EN: Asterisk<br>中: 星号 | EN: **Matches zero or more characters within a single directory level.**<br>中: **匹配单个目录层级内的零个或多个字符。**<br>Example / 示例: `ls *.txt` (lists all `.txt` files in the current directory). |
| **`**`** | EN: Globstar<br>中: 全局星号 | EN: **A modern lifesaver. Recursively matches files and directories across all subdirectory levels.**<br>中: **现代救星。递归匹配所有子目录层级中的文件和目录。**<br>Example / 示例: `ls **/*.txt` (lists all `.txt` files in the current directory and every directory below it). |
| `?` | EN: Question Mark<br>中: 问号 | EN: Matches exactly one character.<br>中: 匹配任意一个字符。<br>Example / 示例: `ls report?.log` (matches `report1.log`, `reportA.log`, but not `report10.log`). |
| `[...]` | EN: Brackets<br>中: 方括号 | EN: Matches any single character within the brackets.<br>中: 匹配括号内的任意一个字符。<br>Example / 示例: `ls [abc]*.log` (matches files starting with `a`, `b`, or `c`). |

### **2. File & Directory Management / 文件和目录管理**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`touch <file>`** | EN: Creates a new, empty file or updates the timestamp.<br>中: 创建一个新的空文件或更新时间戳。 |
| **`mkdir <dir>`** | EN: **M**a**k**e a new **dir**ectory.<br>中: **创**建一个新**目**录。 |
| **`cp <src> <dest>`** | EN: **C**o**p**y a file or directory. Use `-r` for directories.<br>中: **复**制文件或目录。对目录使用 `-r` 选项。 |
| **`mv <src> <dest>`** | EN: **M**o**v**e or **rename** a file or directory.<br>中: **移**动或**重命名**文件或目录。 |
| **`rm <file>`** | EN: **R**e**m**ove (delete) a file. **Use with caution!**<br>中: **删**除文件。**请谨慎使用！** |
| **`rm -r <dir>`** | EN: **R**ecursively remove a directory. **Use with extreme caution!**<br>中: **递**归删除目录。**请极其谨慎使用！** |
| `rmdir <dir>` | EN: **R**e**m**ove an **empty** **dir**ectory.<br>中: **删**除一个**空**的**目**录。 |
| **`ln [-s] <target> <link>`** | EN: Creates a hard link or **s**ymbolic link (`-s`).<br>中: 创建一个硬链接或**符**号链接 (`-s`)。 |

### **3. Viewing Files / 查看文件**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`cat <file>`** | EN: Display the entire content of a file.<br>中: 显示文件的全部内容。 |
| **`less <file>`** | EN: View file content page by page. More powerful than `more`.<br>中: 分页查看文件内容。比 `more` 功能更强大。 |
| `more <file>` | EN: An older, less powerful version of `less`.<br>中: 一个比 `less` 更老、功能更少的版本。 |
| **`head <file>`** | EN: View the first 10 lines of a file. Use `-n` to specify a number.<br>中: 查看文件的前 10 行。使用 `-n` 指定行数。 |
| **`tail <file>`** | EN: View the last 10 lines of a file. Use `-f` to **f**ollow a file in real-time.<br>中: 查看文件的最后 10 行。使用 `-f` 实时**跟**踪文件。 |

### **4. Searching for Files and Text / 搜索文件和文本**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`find <path> [options]`** | EN: Searches for files based on criteria like name, size, type, etc.<br>中: 根据名称、大小、类型等条件搜索文件。 |
| `locate <pattern>` | EN: A faster but less flexible alternative to `find` that uses a pre-built database.<br>中: `find` 命令的一个更快但灵活性较低的替代品，它使用一个预先构建的数据库。 |
| **`grep <pattern> <file>`** | EN: Searches for a pattern of text *inside* one or more files.<br>中: 在一个或多个文件*内部*搜索文本模式。 |

### **5. Other File Utilities / 其他文件工具**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| `file <filename>` | EN: Determines a file's type (e.g., text, image, executable).<br>中: 判断文件的类型（例如，文本、图像、可执行文件）。 |
| `wc <file>` | EN: **W**ord **C**ount. Counts lines, words, and characters in a file.<br>中: **字**数**统**计。统计文件中的行数、单词数和字符数。 |
| `diff <file1> <file2>` | EN: Compares two files and shows the **diff**erences.<br>中: 比较两个文件并显示它们的**差**异。 |
| `sort <file>` | EN: Sorts the lines of a text file.<br>中: 对文本文件的行进行排序。 |
| `vi`, `nano`, `gedit` | EN: Different text editors available on Linux.<br>中: Linux 上可用的不同文本编辑器。 |

### **6. Archiving and Compression / 归档和压缩**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`tar`** | EN: The **T**ape **Ar**chiver. Combines multiple files into one. Common options: `-c` (create), `-x` (extract), `-v` (verbose), `-f` (file), `-z` (gzip).<br>中: **磁**带**归**档器。将多个文件合并成一个。常用选项: `-c` (创建), `-x` (提取), `-v` (详细), `-f` (文件), `-z` (gzip)。 |
| `gzip`, `gunzip` | EN: Compresses or decompresses files using the gzip algorithm (`.gz`).<br>中: 使用 gzip 算法压缩或解压文件 (`.gz`)。 |
| `bzip2`, `bunzip2` | EN: Compresses or decompresses files using the bzip2 algorithm (`.bz2`).<br>中: 使用 bzip2 算法压缩或解压文件 (`.bz2`)。 |

---

## **Module 3: Managing Permissions and Ownership / 模块三：管理权限和所有权**

### **1. Permissions and Ownership Commands / 权限和所有权命令**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`chmod`** | EN: **Ch**ange **mod**e. Changes the permissions of a file or directory.<br>中: **更**改**模**式。更改文件或目录的权限。 |
| **`chown`** | EN: **Ch**ange **own**er. Changes the user and/or group ownership of a file.<br>中: **更**改**所**有者。更改文件的用户和/或组所有权。 |
| `chgrp` | EN: **Ch**ange **gr**ou**p**. Changes only the group ownership of a file.<br>中: **更**改**组**。只更改文件的组所有权。 |
| `umask` | EN: Sets the default permissions for newly created files and directories.<br>中: 为新创建的文件和目录设置默认权限。 |

### **2. User and Group Management / 用户和组管理**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| `useradd` | EN: Adds a new user account.<br>中: 添加一个新用户账户。 |
| `usermod` | EN: Modifies an existing user account.<br>中: 修改一个已存在的用户账户。 |
| `userdel` | EN: Deletes a user account.<br>中: 删除一个用户账户。 |
| **`passwd`** | EN: Changes a user's password.<br>中: 更改用户的密码。 |
| `groupadd` | EN: Adds a new group.<br>中: 添加一个新组。 |
| `groupmod` | EN: Modifies an existing group.<br>中: 修改一个已存在的组。 |
| `groupdel` | EN: Deletes a group.<br>中: 删除一个组。 |
| `gpasswd` | EN: Administers group passwords.<br>中: 管理组密码。 |
| `newgrp` | EN: Logs into a new group.<br>中: 登录到一个新组。 |

---

## **Module 4: BASH Shell and Scripting / 模块四：BASH Shell 和脚本编程**

### **1. Shell Environment and Variables / Shell 环境和变量**

| Command / 命令 | Description / 描述 |
| :--- | :--- |
| **`echo`** | EN: Displays text or the value of a variable.<br>中: 显示文本或变量的值。 |
| `env` | EN: Displays all environment variables.<br>中: 显示所有环境变量。 |
| `set` | EN: Displays all shell variables (environment and local).<br>中: 显示所有 shell 变量（环境和本地）。 |
| `export` | EN: Makes a local variable available to sub-processes (turns it into an environment variable).<br>中: 使本地变量对子进程可用（将其转变为环境变量）。 |
| `unset` | EN: Deletes a shell variable.<br>中: 删除一个 shell 变量。 |
| `read` | EN: Reads a line of input from the user into a variable.<br>中: 从用户那里读取一行输入并存入一个变量。 |
| `let` / `expr` | EN: Commands to perform arithmetic in shell scripts.<br>中: 在 shell 脚本中执行算术运算的命令。 |

### **2. Redirection and Pipes / 重定向和管道**

| Symbol / 符号 | Name / 名称 | Description / 描述 |
| :--- | :--- | :--- |
| **`>`** | EN: Redirect Output<br>中: 重定向输出 | EN: Sends command output to a file, **overwriting** it.<br>中: 将命令输出发送到文件，并**覆盖**其内容。 |
| **`>>`** | EN: Append Output<br>中: 追加输出 | EN: Sends output to a file, **adding** it to the end.<br>中: 将输出发送到文件，并**添加**到末尾。 |
| **`<`** | EN: Redirect Input<br>中: 重定向输入 | EN: Takes input for a command from a file instead of the keyboard.<br>中: 从文件而不是键盘为命令获取输入。 |
| `**`| `**` | EN: Pipe<br>中: 管道 | EN: **This is extremely important.** Sends the output of one command to be the input of another.<br>中: **这个极其重要。** 将一个命令的输出作为另一个命令的输入。 |
