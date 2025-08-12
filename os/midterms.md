
### Chapter 1: Practical 1 – Performing Basic Linux Tasks

This chapter focuses on getting information from the system and managing your terminal session.

#### **1. System Information & Date Commands**

*   **Command:** `date`
    *   **Purpose:** To display or format the current system date and time.
    *   **How to Use:** `date +"[format specifiers]"`
    *   **Examples from the Practical:**
        *   (Q3a) Display a literal string:
            ```bash
            $ date "+This is the date"
            Output: This is the date
            ```
        *   (Q3b) Display the full month name (`%B`):
            ```bash
            $ date "+This is the date: %B"
            Output: This is the date: October 
            ```
        *   (Q4a) Format as `Date: 30 October 2025`:
            ```bash
            $ date +"Date: %d %B %Y"
            ```
        *   (Q4b) Format as `Today is Friday (30/10/2025)`:
            ```bash
            $ date +"Today is %A (%d/%m/%Y)"
            ```
        *   (Q4c) Format as `Date Today: 30-10-2025 & Time Now: 12:30 PM`:
            ```bash
            $ date +"Date Today: %d-%m-%Y & Time Now: %I:%M %p"
            ```

*   **Command:** `uname`
    *   **Purpose:** (Q5c) To display basic system information. By default, it prints the kernel name.
    *   **How to Use:** `uname`
    *   **Example:**
        ```bash
        $ uname
        Output: Linux
        ```

*   **Command:** `last`
    *   **Purpose:** (Q5d) To show a list of the last logged-in users.
    *   **How to Use:** `last`

#### **2. Getting Help & Documentation**

*   **Command:** `man`
    *   **Purpose:** (Q6a, Q7) To display the **manual** page for a command, providing in-depth information.
    *   **How to Use:** `man [command_name]`
    *   **Example:** To get the manual for the `sed` command:
        ```bash
        $ man sed
        ```

*   **Command:** `apropos`
    *   **Purpose:** (Q7) To search for commands related to a keyword.
    *   **How to Use:** `apropos [keyword]`
    *   **Example:** To find commands related to "search":
        ```bash
        $ apropos search
        ```

*   **Command:** `[command] --help`
    *   **Purpose:** (Q6e, Q7) To display a short, summarized help message for a command.
    *   **How to Use:** `[command_name] --help`
    *   **Example:** To get a summary for the `gzip` command:
        ```bash
        $ gzip --help
        ```

#### **3. Terminal Control & Communication**

*   **Command:** `wall`
    *   **Purpose:** (Q5a) To write a message to all currently logged-in users' terminals.
    *   **How to Use:** `wall "Your message here"`

*   **Command:** `echo`
    *   **Purpose:** (Q5b) To display text on the terminal.
    *   **How to Use:** `echo "Your text here"`

*   **Command:** `clear`
    *   **Purpose:** (Q6c, Q7) To clear all text from the terminal screen.
    *   **How to Use:** `clear`

*   **Command:** `exit`
    *   **Purpose:** (Q6c, Q7) To close the current terminal session.
    *   **How to Use:** `exit`

*   **Command:** `pwd`
    *   **Purpose:** (Q7) To **p**rint the **w**orking **d**irectory (show your current location).
    *   **How to Use:** `pwd`

*   **Command:** `sudo`
    *   **Purpose:** (Q7) To execute a command with superuser (administrator) privileges.
    *   **How to Use:** `sudo [command_to_run_as_admin]`

---

### Chapter 2: Practical 2 – Managing Files in Linux System

This chapter is about creating, deleting, moving, and organizing files and directories.

#### **1. Navigation & Listing**

*   **Command:** `pwd`
    *   **Purpose:** (Q1) To show your current path.
    *   **How to Use:** `pwd`

*   **Command:** `cd`
    *   **Purpose:** To **c**hange **d**irectory.
    *   **How to Use:** `cd [path_to_directory]`
    *   **Examples:**
        *   Go to your home directory: `cd ~`
        *   (Q7) Go to the root directory: `cd /`
        *   Go up one level: `cd ..`

*   **Command:** `ls`
    *   **Purpose:** (Q3) To **l**i**s**t the contents of a directory.
    *   **How to Use:** `ls [options] [path]`
    *   **Examples:**
        *   List contents of current directory: `ls`
        *   List contents in a detailed, long format: `ls -l`

#### **2. Creating Files & Directories**

*   **Command:** `mkdir`
    *   **Purpose:** (Q2, Q4) To **m**a**k**e a new **dir**ectory.
    *   **How to Use:** `mkdir [directory_name]`
    *   **Example:**
        ```bash
        $ mkdir D2
        $ mkdir D2/super
        ```

*   **Command:** `touch`
    *   **Purpose:** (Q5) To create a new, empty file or update the timestamp of an existing file.
    *   **How to Use:** `touch [filename1] [filename2] ...`
    *   **Example:**
        ```bash
        $ touch apple.doc april.doc box.txt ultra.txt
        ```

#### **3. Copying, Moving, & Deleting**

*   **Command:** `cp`
    *   **Purpose:** To **c**o**p**y files or directories.
    *   **How to Use (Files):** `cp [source_file] [destination_file_or_directory]`
    *   **How to Use (Directories):** `cp -r [source_directory] [destination_directory]` (The `-r` means recursive).
    *   **Examples:**
        *   (Q11) Copy directory `super` to home (`~`) and rename it `super2`: `cp -r super ~/super2`
        *   (Q26) Backup files to the "backup" directory: `cp sampleA.txt sampleC.txt backup/`

*   **Command:** `mv`
    *   **Purpose:** To **m**o**v**e or rename files and directories.
    *   **How to Use:** `mv [source] [destination]`
    *   **Examples:**
        *   (Q10) Rename `ultra.txt` to `mega.txt`: `mv ultra.txt mega.txt`
        *   (Extra Q6) Move and rename in one step: `mv /tmp/file2 ~/my_file2`

*   **Command:** `rm`
    *   **Purpose:** To **r**e**m**ove (delete) files or directories. **Use with caution!**
    *   **How to Use (Files):** `rm [filename]`
    *   **How to Use (Directories):** `rm -r [directory_name]` (The `-r` means recursive).
    *   **Examples:**
        *   (Q24) Delete a file: `rm sampleB.txt`
        *   (Q13) Delete a directory and everything inside it: `rm -r super`

#### **4. Viewing & Editing Files**

*   **Command:** `cat`
    *   **Purpose:** To display file contents, combine files, or create a new file.
    *   **How to Use:**
        *   View a file: `cat [filename]` (Q21)
        *   Create a file: `cat > [filename]` (Q16)
        *   Combine files: `cat [file1] [file2] > [new_combined_file]` (Q20)
    *   **Example (Combine):**
        ```bash
        $ cat sampleA.txt sampleB.txt > sampleC.txt
        ```

*   **Command:** `vi`
    *   **Purpose:** (Q14, Q18) A powerful command-line text editor.
    *   **How to Use:** `vi [filename]`
    *   **Basic Controls:**
        1.  Press `i` to enter **Insert Mode** to start typing.
        2.  Press `Esc` to return to **Command Mode**.
        3.  In Command Mode, type `:wq` and press Enter to **w**rite (save) and **q**uit.

*   **Command:** `wc`
    *   **Purpose:** (Q19) To get the **w**ord **c**ount (and line/character count) of a file.
    *   **How to Use:** `wc [filename]`

*   **Command:** `less`
    *   **Purpose:** (Extra Q4) To view the contents of a long file page-by-page.
    *   **How to Use:** `less [filename]`

#### **5. Searching & Archiving**

*   **Command:** `ls` with Wildcards
    *   **Purpose:** (Q6) To list files matching a specific pattern.
    *   **How to Use:**
        *   `*` matches any number of characters.
        *   `?` matches exactly one character.
    *   **Examples:**
        *   (Q6a) Files starting with "ap": `ls ap*`
        *   (Q6b) Filenames with exactly 7 characters: `ls ???????`
        *   (Q6c) Files ending with ".txt": `ls *.txt`
        *   (Q6d) Files where the third letter is "p": `ls ??p*`

*   **Command:** `find`
    *   **Purpose:** (Q8, Q9) To search the file system for files and directories.
    *   **How to Use:** `find [starting_path] -type [d_or_f] -name "[search_pattern]"`
    *   **Examples:**
        *   (Q8) Find a directory named "super" starting from root: `find / -type d -name "super"`
        *   (Q9) Find a file named "ultra.txt" starting from root: `find / -type f -name "ultra.txt"`

*   **Command:** `tar`
    *   **Purpose:** (Q22) To bundle multiple files into a single archive file (a "tarball"). It does not compress.
    *   **How to Use:** `tar -cvf [archive_name.tar] [file1] [file2] ...`
        *   `-c`: create
        *   `-v`: verbose (show progress)
        *   `-f`: file (specify archive name)
    *   **Example:**
        ```bash
        $ tar -cvf sampleC.tar sampleA.txt sampleB.txt
        ```

*   **Command:** `gzip`
    *   **Purpose:** (Extra Q7) To compress a file. Often used on a `.tar` file.
    *   **How to Use:** `gzip [filename]`
    *   **Example:**
        ```bash
        # First, create the tar archive
        $ tar -cvf MyArchive.tar file1 file2
        # Then, compress it
        $ gzip MyArchive.tar 
        # This creates a new file: MyArchive.tar.gz
        ```
