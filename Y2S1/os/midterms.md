### **Midterm Test Details / 期中考试重点摘要** 

*   **Test (考试):** Mid-term Test (Chapters 1 to 3) / 期中考试 (第1至3章)
*   **Weightage (分数占比):** 50% of your final grade / 占总成绩的 50%
*   **Marks (分数):** 50
*   **Date (日期):** Monday, 18/8/2025 (Week 9) / 2025年8月18日，星期一 (第九周)
*   **Time (时间):** 3:15 PM - 4:45 PM
*   **Duration (时长):** 1 hour 30 minutes / 1小时30分钟
*   **Venue (地点):** M003 & M004

---

## **Chapter 1: System Software & OS Introduction / 系统软件与操作系统简介**

### **1. Core Concepts / 核心概念**

*   **Computer System Components / 计算机系统组件**
    *   **EN:** The system is composed of hardware, software, and users.
    *   **中文:** 系统由硬件、软件和用户组成。
*   **System Software vs. Application Software / 系统软件 vs. 应用软件**
    *   **System Software / 系统软件**
        *   **EN:** Operates the computer hardware and provides a platform for applications (e.g., OS, BIOS). It is the foundation.
        *   **中文:** 操作计算机硬件并为应用程序提供平台的软件 (例如：操作系统、BIOS)。它是系统的基础。
    *   **Application Software / 应用软件**
        *   **EN:** Programs designed for specific user tasks (e.g., Word, Chrome, games). They run on top of the system software.
        *   **中文:** 为用户执行特定任务而设计的程序 (例如：Word, Chrome, 游戏)。它们运行在系统软件之上。
*   **Operating System (OS) / 操作系统**
    *   **EN:** The most important system software that acts as an intermediary between the user/applications and the hardware. It manages all resources.
    *   **中文:** 最重要的系统软件，作为用户/应用程序和硬件之间的中介。它管理所有资源。

### **2. OS Managers (Subsystems) / 操作系统管理器 (子系统)**

*   **Processor Manager / 处理器管理器**
    *   **EN:** Manages the CPU, deciding which process gets CPU time and for how long.
    *   **中文:** 管理中央处理器 (CPU)，决定哪个进程以及何时获得CPU时间。
*   **Memory Manager / 内存管理器**
    *   **EN:** Manages RAM by allocating memory to processes and ensuring protection.
    *   **中文:** 通过为进程分配内存并确保内存保护来管理RAM (内存)。
*   **Device Manager / 设备管理器**
    *   **EN:** Manages all I/O devices like keyboards, printers, and disk drives.
    *   **中文:** 管理所有输入/输出设备，如键盘、打印机和磁盘驱动器。
*   **File Manager / 文件管理器**
    *   **EN:** Manages files and directories, controlling access and permissions.
    *   **中文:** 管理文件和目录，控制访问权限。

### **3. Types of Operating Systems / 操作系统的类型**

*   **Batch Systems / 批处理系统**
    *   **EN:** Processes a batch of similar jobs serially without user interaction. Focuses on throughput.
    *   **中文:** 无需用户交互，按批次顺序处理相似的作业。注重吞吐量。
*   **Time-Sharing (Interactive) Systems / 分时 (交互式) 系统**
    *   **EN:** Allows multiple users to interact with the system at the same time by quickly switching between jobs.
    *   **中文:** 通过在作业之间快速切换，允许多个用户同时与系统进行交互。
*   **Real-Time Systems / 实时系统**
    *   **EN:** Used in time-critical environments where data must be processed within a strict time limit (e.g., airport traffic control).
    *   **中文:** 用于时间关键型环境，数据必须在严格的时间限制内处理 (例如：机场交通管制)。

### **4. Key OS Operations / 关键的操作系统操作**

*   **Dual-Mode Operation / 双模式操作**
    *   **EN:** The OS switches between user mode (for applications) and kernel mode (for OS tasks) to protect system resources.
    *   **中文:** 操作系统在用户模式 (用于应用程序) 和内核模式 (用于操作系统任务) 之间切换，以保护系统资源。
*   **Interrupts / 中断**
    *   **EN:** A signal from hardware or software that diverts the CPU to handle an important event.
    *   **中文:** 来自硬件或软件的信号，使CPU转去处理一个重要事件。

---

## **Chapter 2: Processor Management / 处理器管理**

### **1. Processes & Schedulers / 进程与调度器**

*   **Program vs. Process / 程序 vs. 进程**
    *   **EN:** A program is inactive code on a disk. A process is a program in execution.
    *   **中文:** 程序是磁盘上的静态代码。进程是正在执行中的程序。
*   **Schedulers / 调度器**
    *   **Job Scheduler (Long-Term) / 作业调度器 (长期)**
        *   **EN:** Selects which jobs from the disk are loaded into memory's READY queue.
        *   **中文:** 从磁盘中选择作业加载到内存的就绪队列中。
    *   **Process Scheduler (Short-Term) / 进程调度器 (短期)**
        *   **EN:** Selects the next process from the READY queue to be executed by the CPU.
        *   **中文:** 从就绪队列中选择下一个将由CPU执行的进程。
*   **Process Control Block (PCB) / 进程控制块**
    *   **EN:** A data structure that stores all information about a process, such as its state, ID, and registers.
    *   **中文:** 一种数据结构，用于存储关于一个进程的所有信息，如状态、ID和寄存器内容。
*   **Context Switching / 上下文切换**
    *   **EN:** The mechanism of saving the state of the current process (into its PCB) and loading the state of the next process.
    *   **中文:** 保存当前进程的状态 (到其PCB中) 并加载下一个进程的状态的机制。

### **2. Scheduling Policies & Algorithms / 调度策略与算法 🧠**

*   **Scheduling Policies / 调度策略**
    *   **Non-Preemptive / 非抢占式**
        *   **EN:** Once a process starts, it keeps the CPU until it finishes or voluntarily gives it up.
        *   **中文:** 一旦进程开始运行，它将一直占用CPU，直到完成或自愿放弃。
    *   **Preemptive / 抢占式**
        *   **EN:** The OS can interrupt a running process and force it to give up the CPU.
        *   **中文:** 操作系统可以中断一个正在运行的进程，强制其放弃CPU。
*   **Scheduling Algorithms / 调度算法**
    *   **First-Come, First-Served (FCFS) / 先到先得**
        *   **EN:** A non-preemptive algorithm where processes are executed in the order they arrive.
        *   **中文:** 一种非抢占式算法，进程按其到达的顺序执行。
        *   🔗 [Example of FCFS](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/schedulingalgorithms.md#1-fcfs-first-come-first-served--%E5%85%88%E5%88%B0%E5%85%88%E5%BE%97)
    *   **Shortest Job Next (SJN) / 最短作业优先**
        *   **EN:** A non-preemptive algorithm that selects the waiting process with the smallest estimated execution time.
        *   **中文:** 一种非抢占式算法，选择等待队列中预计执行时间最短的进程。
        *   🔗 [Example of SJN](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/schedulingalgorithms.md#2-sjn-shortest-job-next--%E6%9C%80%E7%9F%AD%E4%BD%9C%E4%B8%9A%E4%BC%98%E5%85%88)
    *   **Shortest Remaining Time (SRT) / 最短剩余时间**
        *   **EN:** The preemptive version of SJN. It switches to a new process if it has a shorter remaining time than the current one.
        *   **中文:** SJN的抢占式版本。如果新到达的进程比当前进程的剩余时间更短，则切换到新进程。
        *   🔗 [Example of SRT](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/schedulingalgorithms.md#3-srt-shortest-remaining-time--%E6%9C%80%E7%9F%AD%E5%89%A9%E4%BD%99%E6%97%B6%E9%97%B4)
    *   **Round Robin (RR) / 轮询调度**
        *   **EN:** A preemptive algorithm where each process gets a small unit of CPU time (time quantum).
        *   **中文:** 一种抢占式算法，每个进程被分配一个小的CPU时间单位 (时间片)。
        *   🔗 [Example of RR](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/schedulingalgorithms.md#4-rr-round-robin--%E8%BD%AE%E8%AF%A2%E8%B0%83%E5%BA%A6)

### **3. Important Formulas / 重要计算公式**

*   **Turnaround Time / 周转时间**
    *   **EN:** Calculated as: `Finish Time` – `Arrival Time`.
    *   **中文:** 计算公式为: `完成时间` – `到达时间`。
*   **Waiting Time / 等待时间**
    *   **EN:** Calculated as: `Finish Time` – `CPU Cycle` – `Arrival Time`.
    *   **中文:** 计算公式为: `完成时间` – `CPU周期` – `到达时间`。

---

## **Chapter 3: Deadlock / 死锁**

### **1. What is Deadlock? / 什么是死锁?**

*   **Deadlock / 死锁**
    *   **EN:** A situation where two or more processes are blocked forever, each waiting for a resource held by another process in the set.
    *   **中文:** 指两个或多个进程因互相等待对方持有的资源而陷入永久阻塞的一种状态。

### **2. The Four Necessary Conditions for Deadlock / 死锁的四个必要条件**

*   **Mutual Exclusion / 互斥条件**
    *   **EN:** At least one resource must be held in a non-sharable mode; only one process can use it at a time.
    *   **中文:** 至少有一个资源必须处于非共享模式；一次只有一个进程可以使用它。
*   **Hold and Wait / 占有并等待**
    *   **EN:** A process must be holding at least one resource and waiting to acquire additional resources held by other processes.
    *   **中文:** 一个进程必须至少持有一个资源，并且正在等待获取由其他进程持有的额外资源。
*   **No Preemption / 不可抢占**
    *   **EN:** Resources cannot be forcibly taken from a process. They must be explicitly released by the process holding them.
    *   **中文:** 资源不能被强制性地从一个进程中夺走，必须由持有它的进程显式释放。
*   **Circular Wait / 循环等待**
    *   **EN:** A set of waiting processes {P0, P1, ..., Pn} must exist such that P0 is waiting for a resource held by P1, P1 is waiting for P2, ..., and Pn is waiting for P0.
    *   **中文:** 必须存在一个等待进程集合 {P0, P1, ..., Pn}，其中P0在等待P1持有的资源，P1在等待P2的资源，...，而Pn在等待P0的资源。

### **3. Strategies for Handling Deadlocks / 处理死锁的策略**

*   **Deadlock Prevention / 死锁预防**
    *   **EN:** Ensure that the system can never enter a deadlock state by breaking one of the four necessary conditions.
    *   **中文:** 通过破坏四个必要条件之一，确保系统永远不会进入死锁状态。
*   **Deadlock Avoidance / 死锁避免**
    *   **EN:** The system dynamically checks if granting a resource request is "safe" and will not lead to a deadlock. Uses Banker's Algorithm.
    *   **中文:** 系统动态地检查分配一个资源请求是否“安全”，即不会导致死锁。使用银行家算法。
*   **Deadlock Detection and Recovery / 死锁检测与恢复**
    *   **EN:** Allow the system to enter a deadlock state, detect it, and then recover by terminating processes or preempting resources.
    *   **中文:** 允许系统进入死锁状态，然后检测它，并通过终止进程或抢占资源来进行恢复。

### **4. Deadlock vs. Starvation / 死锁 vs. 饥饿**

*   **Deadlock / 死锁**
    *   **EN:** A group of processes are all stuck in a circular wait. The state is permanent and requires external intervention.
    *   **中文:** 一组进程陷入循环等待。这种状态是永久性的，需要外部干预才能解决。
*   **Starvation / 饥饿**
    *   **EN:** A process is indefinitely postponed because it is repeatedly denied access to resources (e.g., a low-priority process).
    *   **中文:** 一个进程被无限期地延迟，因为它反复被拒绝访问资源 (例如，一个低优先级的进程)。
   
   ### **Deadlock Example / 死锁示例**
   
   *   **EN:** A situation where two or more processes are blocked forever, waiting for each other. This happens when all four necessary conditions (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) are met.
   *   **中文:** 两个或多个进程因相互等待而永久阻塞的情况。当四个必要条件 (互斥、占有并等待、不可抢占、循环等待) 同时满足时会发生。
   
   #### **The Scenario / 场景**
   
   *   **Processes / 进程:**
       *   **Process 1 (P1):** Needs to use the Scanner first, then the Printer.
       *   **Process 2 (P2):** Needs to use the Printer first, then the Scanner.
   *   **Resources / 资源:**
       *   **Resource 1 (R1):** A Scanner (扫描仪)
       *   **Resource 2 (R2):** A Printer (打印机)
   
   Both resources have **Mutual Exclusion** (only one process can use them at a time).
   两种资源都是**互斥**的 (一次只能由一个进程使用)。
   
   #### **Sequence of Events Leading to Deadlock / 导致死锁的事件顺序**
   
   1.  **Step 1:** Process 1 requests and gets the Scanner (R1).
       **第一步:** 进程1 请求并获得了扫描仪 (R1)。
       *   *State:* P1 holds R1. (P1 占有 R1).
   2.  **Step 2:** Process 2 requests and gets the Printer (R2).
       **第二步:** 进程2 请求并获得了打印机 (R2)。
       *   *State:* P1 holds R1; P2 holds R2. (P1 占有 R1; P2 占有 R2).
   3.  **Step 3:** Process 1 tries to request the Printer (R2), but it's held by P2. So, **P1 waits**.
       **第三步:** 进程1 试图请求打印机 (R2)，但它被 P2 占有。因此，**P1 开始等待**。
       *   *State:* P1 holds R1 and is waiting for R2. (P1 占有 R1 并等待 R2).
   4.  **Step 4:** Process 2 tries to request the Scanner (R1), but it's held by P1. So, **P2 waits**.
       **第四步:** 进程2 试图请求扫描仪 (R1)，但它被 P1 占有。因此，**P2 开始等待**。
       *   *State:* P2 holds R2 and is waiting for R1. (P2 占有 R2 并等待 R1).
   
   #### **Result: DEADLOCK!**
   **结果：死锁！**
   
   *   **EN:** P1 is waiting for P2 to release the Printer. P2 is waiting for P1 to release the Scanner. Neither can proceed. This is a **Circular Wait**.
   *   **中文:** P1 在等待 P2 释放打印机。P2 在等待 P1 释放扫描仪。两者都无法继续执行。这是一个**循环等待**。
   
   #### **Resource Allocation Graph Visualization / 资源分配图可视化**
   This graph shows the deadlock state clearly:
   这个图清晰地展示了死锁状态：
   
   ```
          waits for / 等待
      P1 ----------> [ R2 ]
      ^              |
      |              |
    holds / 占有     holds / 占有
      |              |
      |              v
    [ R1 ] <---------- P2
          waits for / 等待
   ```
   
   *   **EN:** The cycle in the graph (P1 → R2 → P2 → R1 → P1) confirms the deadlock.
   *   **中文:** 图中的循环 (P1 → R2 → P2 → R1 → P1) 证实了死锁的存在。
