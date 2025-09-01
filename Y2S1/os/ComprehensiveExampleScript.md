
---

### **Combined Script Example: A Safe Deletion Utility / 组合脚本示例：一个安全删除工具**

EN: This script is a "safe delete" tool. Instead of permanently deleting files with `rm`, it moves them to a pre-defined trash directory. It checks its arguments, loops through them, and asks for confirmation before acting.
<br>中: 这个脚本是一个“安全删除”工具。它不会用 `rm` 永久删除文件，而是将它们移动到一个预定义的回收站目录。它会检查参数，遍历它们，并在操作前请求确认。

**Script Name / 脚本名:** `safe_delete.sh`

```bash
#!/bin/bash

################################################################################
# A script to safely "delete" files by moving them to a trash directory.
# It combines variables, positional parameters, if, for, and read.
#
# 一个通过将文件移动到回收站目录来安全“删除”文件的脚本。
# 它结合了变量、位置参数、if、for 和 read。
################################################################################

# --- 1. VARIABLES ---
# Define a constant variable for our trash directory.
# 为我们的回收站目录定义一个常量。
TRASH_DIR="$HOME/.trash"


# --- 2. IF STATEMENT (Initial Checks) ---
# Check if the trash directory exists. If not, create it.
# 检查回收站目录是否存在。如果不存在，则创建它。
if [ ! -d "$TRASH_DIR" ]; then
  echo "Trash directory not found. Creating it now at $TRASH_DIR"
  mkdir "$TRASH_DIR"
fi

# Check if the user provided any arguments ($#).
# 检查用户是否提供了任何参数 ($#)。
if [ "$#" -eq 0 ]; then
  echo "Usage: $0 <file1> [file2] ..."
  echo "Error: You must specify at least one file to delete."
  exit 1 # Exit because there's nothing to do.
fi


# --- 3. POSITIONAL PARAMETERS & FOR LOOP ---
# Announce what we are about to do.
# 声明我们将要做什么。
echo "The following files will be moved to the trash: $@"

# Ask for confirmation using 'read'.
# 使用 'read' 请求确认。
echo -n "Are you sure you want to continue? (y/n): "
read CONFIRMATION

# --- 4. IF STATEMENT (Processing Confirmation) ---
# Check the user's answer.
# 检查用户的回答。
if [ "$CONFIRMATION" != "y" ]; then
  echo "Operation cancelled by user."
  exit 0 # Exit cleanly.
fi


# If we get here, the user confirmed 'y'.
# 如果程序执行到这里，说明用户确认了 'y'。
echo "Proceeding with deletion..."

# Loop through every argument the user provided ("$@").
# 遍历用户提供的每一个参数 ("$@")。
for FILE_TO_DELETE in "$@"
do
  # --- NESTED IF STATEMENT (Check each file) ---
  # Check if the current item actually exists before trying to move it.
  # 在尝试移动之前，检查当前项目是否真实存在。
  if [ -e "$FILE_TO_DELETE" ]; then
    echo "  -> Moving '$FILE_TO_DELETE' to trash..."
    mv "$FILE_TO_DELETE" "$TRASH_DIR/"
  else
    echo "  -> Warning: File '$FILE_TO_DELETE' not found. Skipping."
  fi
done

echo "---------------------------------"
echo "Safe delete operation complete!"
```

### **How to Use and Understand It / 如何使用和理解它**

1.  **Save the code** as `safe_delete.sh`.
    <br>中: 将代码保存为 `safe_delete.sh`。

2.  **Make it executable:**
    <br>中: **设为可执行:**
    ```bash
    chmod +x safe_delete.sh
    ```

3.  **Create some test files:**
    <br>中: **创建一些测试文件:**
    ```bash
    touch report.txt notes.md image.jpg non_existent_file
    ```

4.  **Run the script with arguments:**
    <br>中: **带参数运行脚本:**
    ```bash
    ./safe_delete.sh report.txt notes.md non_existent_file
    ```

**Expected Interaction and Output / 预期的交互和输出:**

```
The following files will be moved to the trash: report.txt notes.md non_existent_file
Are you sure you want to continue? (y/n): y  <-- You type 'y' and press Enter
Proceeding with deletion...
  -> Moving 'report.txt' to trash...
  -> Moving 'notes.md' to trash...
  -> Warning: File 'non_existent_file' not found. Skipping.
---------------------------------
Safe delete operation complete!
```

**Verification / 验证:**

*   `ls`: You will see that `report.txt` and `notes.md` are gone from the current directory.
    <br>中: `ls`: 你会看到 `report.txt` 和 `notes.md` 已经从当前目录消失了。
*   `ls ~/.trash`: You will see `report.txt` and `notes.md` are now inside your trash directory.
    <br>中: `ls ~/.trash`: 你会看到 `report.txt` 和 `notes.md` 现在位于你的回收站目录中。

This single script effectively demonstrates all the key programming concepts from Module 4 working together to create a robust and safe tool.
