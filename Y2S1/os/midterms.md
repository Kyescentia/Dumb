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
        *   🔗 [Example of NPP](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/PPnNPP.md#1-non-preemptive-priority--%E9%9D%9E%E6%8A%A2%E5%8D%A0%E5%BC%8F%E4%BC%98%E5%85%88%E7%BA%A7%E8%B0%83%E5%BA%A6)
    *   **Preemptive / 抢占式**
        *   **EN:** The OS can interrupt a running process and force it to give up the CPU.
        *   **中文:** 操作系统可以中断一个正在运行的进程，强制其放弃CPU。
       *   🔗 [Example of PP](https://github.com/Kyescentia/Dumb/blob/main/Y2S1/os/PPnNPP.md#2-preemptive-priority--%E6%8A%A2%E5%8D%A0%E5%BC%8F%E4%BC%98%E5%85%88%E7%BA%A7%E8%B0%83%E5%BA%A6)

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

### **Chapter 3: Deadlock / 第三章：死锁**

#### **1. What is Deadlock? / 什么是死锁？**

*   **Definition / 定义**
    *   **EN:** A situation where a set of two or more processes are permanently blocked because each process is holding a resource and waiting for another resource that is held by another process in the same set. It is also called a "deadly embrace."
    *   **中文:** 一种状态，其中两个或多个进程被永久阻塞，因为每个进程都持有一个资源，同时又在等待该集合中另一个进程所持有的另一个资源。它也被称为“死锁拥抱”。
*   **Key Characteristics / 关键特征**
    *   **EN:** Deadlock is more serious than starvation because it affects multiple processes and will never resolve on its own. It requires external intervention (e.g., terminating a process) to be broken.
    *   **中文:** 死锁比饥饿更严重，因为它影响多个进程，并且永远无法自行解决。它需要外部干预（例如，终止一个进程）才能被打破。

---

#### **2. The Four Necessary Conditions for Deadlock / 死锁的四个必要条件**

*   **EN:** For a deadlock to occur, all four of these conditions must be met simultaneously.
*   **中文:** 死锁的发生必须**同时满足**以下所有四个条件。

1.  **Mutual Exclusion / 互斥条件**
    *   **EN:** At least one resource must be non-sharable, meaning only one process can use it at a time.
    *   **中文:** 至少有一个资源必须是非共享的，意味着一次只有一个进程可以使用它。（例如：打印机）。
2.  **Hold and Wait / 占有并等待**
    *   **EN:** A process is holding at least one resource while waiting to acquire additional resources that are currently being held by other processes.
    *   **中文:** 一个进程至少持有一个资源，同时又在等待获取当前被其他进程持有的额外资源。
3.  **No Preemption / 不可抢占**
    *   **EN:** A resource cannot be forcibly taken away from the process holding it. It can only be released voluntarily by the process.
    *   **中文:** 资源不能被强制性地从持有它的进程中夺走。它只能由该进程自愿释放。
4.  **Circular Wait / 循环等待**
    *   **EN:** A set of waiting processes {P0, P1, ..., Pn} exists such that P0 is waiting for a resource held by P1, P1 is waiting for a resource held by P2, ..., and Pn is waiting for a resource held by P0.
    *   **中文:** 存在一个等待进程的循环链 {P0, P1, ..., Pn}，其中P0在等待P1持有的资源，P1在等待P2持有的资源，...，而Pn在等待P0持有的资源。

---

#### **3. Modeling Deadlocks: Resource-Allocation Graphs / 死锁建模：资源分配图**

*   **EN:** We can visualize the state of the system using a directed graph.
*   **中文:** 我们可以使用有向图来可视化系统的状态。
    *   **Process (进程):** Represented by a circle / 用圆形表示。
    *   **Resource (资源):** Represented by a square / 用方形表示。
    *   **Request Edge (请求边):** An arrow from a process to a resource (`P → R`) means the process is requesting that resource. / 从进程指向资源的箭头 (`P → R`) 表示该进程正在请求该资源。
    *   **Assignment Edge (分配边):** An arrow from a resource to a process (`R → P`) means the resource has been allocated to that process. / 从资源指向进程的箭头 (`R → P`) 表示该资源已被分配给该进程。

*   **Key Rule / 关键规则**
    *   **EN:** If the graph contains a **cycle**, a deadlock exists. If there is no cycle, the system is not deadlocked.
    *   **中文:** 如果图中包含一个**环路（cycle）**，则存在死锁。如果没有环路，系统就没有死锁。

*   **Example / 示例:**
    *   **EN:** P1 holds R1 and wants R2. P2 holds R2 and wants R1.
    *   **中文:** P1持有R1并想要R2。P2持有R2并想要R1。

    **Text-based Visualization / 文本可视化:**
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
    *   **EN:** The cycle `P1 → R2 → P2 → R1 → P1` clearly indicates a deadlock.
    *   **中文:** 环路 `P1 → R2 → P2 → R1 → P1` 清晰地表明了死锁的存在。

---

#### **4. Strategies for Handling Deadlocks / 处理死锁的策略**

##### **a) Deadlock Prevention / 死锁预防**

*   **EN:** Design the system to break one of the four necessary conditions, making deadlock impossible.
*   **中文:** 通过破坏四个必要条件之一来设计系统，使死锁不可能发生。
    1.  **Break Mutual Exclusion:** Make resources sharable (not always possible, e.g., for a printer). / 打破互斥：使资源可共享（但并非所有资源都可行，如打印机）。
    2.  **Break Hold and Wait:** Require a process to request all its resources at once, or to release all held resources before requesting new ones. / 打破占有并等待：要求进程一次性请求所有资源，或在请求新资源前释放所有已持有的资源。
    3.  **Break No Preemption:** If a process requests a resource that is unavailable, it must release all resources it currently holds. / 打破不可抢占：如果一个进程请求的资源不可用，它必须释放当前持有的所有资源。
    4.  **Break Circular Wait:** Impose a total ordering of all resource types and require that each process requests resources in an increasing order of enumeration (Havender's solution). / 打破循环等待：对所有资源类型进行全局排序，并要求每个进程按递增的顺序请求资源（Havender解决方案）。

##### **b) Deadlock Avoidance / 死锁避免**

*   **EN:** The OS uses prior information about the maximum resources a process might need to decide whether granting a request is "safe." The goal is to never enter an unsafe state.
*   **中文:** 操作系统使用关于进程可能需要的最大资源的先验信息，来决定批准一个请求是否“安全”。目标是永远不进入不安全状态。
    *   **Main Tool / 主要工具:** **Banker's Algorithm**. / **银行家算法**。
    *   **EN:** It checks if granting a request will leave the system in a **safe state** (a state where there is at least one sequence for all processes to finish). If not, the request is denied.
    *   **中文:** 它检查批准一个请求后系统是否会处于**安全状态**（即存在至少一个能让所有进程都完成的序列）。如果不是，则请求被拒绝。

##### **c) Deadlock Detection and Recovery / 死锁检测与恢复**

*   **EN:** Allow the system to enter a deadlock, then detect it and recover.
*   **中文:** 允许系统进入死锁状态，然后检测到它并进行恢复。
    *   **Detection / 检测:** Periodically check for cycles in the resource-allocation graph. / 定期检查资源分配图中是否存在环路。
    *   **Recovery / 恢复:**
        1.  **Process Termination / 终止进程:** Abort one or more processes in the deadlock cycle. / 中止死锁环路中的一个或多个进程。
        2.  **Resource Preemption / 资源抢占:** Forcibly take away resources from some processes and give them to others until the deadlock cycle is broken. / 从某些进程中强制性地收回资源，并将其分配给其他进程，直到死锁环路被打破。

---

#### **5. Deadlock vs. Starvation / 死锁 vs. 饥饿**

*   **Deadlock / 死锁**
    *   **EN:** A process is blocked and can **never** run again because it is waiting for a resource held by another waiting process in a circular chain.
    *   **中文:** 一个进程被阻塞，并且**永远**无法再次运行，因为它正在等待一个循环链中另一个等待进程所持有的资源。
*   **Starvation / 饥饿**
    *   **EN:** A process is overlooked or repeatedly postponed by the scheduler but is **not technically blocked**. It *could* run, but high-priority processes keep arriving and taking its place. It's a problem of indefinite postponement.
    *   **中文:** 一个进程被调度器忽略或反复推迟，但**技术上并未被阻塞**。它*本可以*运行，但高优先级的进程不断到达并抢占了它的位置。这是一个无限期延迟的问题。
    *   **Solution / 解决方案:** **Aging (老化)** - gradually increasing the priority of processes that wait for a long time. / **老化** - 逐渐提高等待时间长的进程的优先级。

---

### **Banker's Algorithm Example / 银行家算法示例**

#### **Definition and Goal / 定义与目标**

*   **EN:** The Banker's Algorithm is a **deadlock avoidance** algorithm. It ensures the system is always in a **"safe state"**. A safe state is one where there exists at least one sequence of execution that allows all processes to complete without deadlocking. If a resource request leads to an unsafe state, the request is denied.
*   **中文:** 银行家算法是一种**死锁避免**算法。它通过检查每一个资源请求来确保系统始终处于**“安全状态”**。安全状态是指存在至少一个能让所有进程都顺利完成而不会发生死锁的执行序列。如果一个资源请求会导致不安全状态，该请求将被拒绝。

#### **Example Data Set / 示例数据集**

*   **Processes / 进程:** P0, P1, P2
*   **Resource Types / 资源类型:** A, B, C
*   **Total System Resources / 系统总资源:** **A=9, B=3, C=6**

---

### **Part 1: Is the initial system state safe? / 第一部分：初始系统状态是否安全？**

#### **Step 1: Initial State and Need Calculation / 步骤1：初始状态与需求计算**

*   **EN:** This is the current snapshot of the system.
*   **中文:** 这是系统当前的快照。

| Process | Allocation (A B C) | Max (A B C) |
| :------ | :----------------- | :---------- |
| P0      | 1 0 0              | 4 3 3       |
| P1      | 3 1 2              | 5 2 2       |
| P2      | 2 1 1              | 3 3 2       |

*   **EN:** First, we calculate the `Available` resources and the `Need` matrix (`Need = Max - Allocation`).
*   **中文:** 首先，我们计算 `Available` (可用资源) 和 `Need` (需求) 矩阵 (`Need = Max - Allocation`)。

*   **Total Allocated (已分配总量):**
    *   A: 1 + 3 + 2 = 6
    *   B: 0 + 1 + 1 = 2
    *   C: 0 + 2 + 1 = 3
*   **Available = Total - Allocated:**
    *   A: 9 - 6 = 3
    *   B: 3 - 2 = 1
    *   C: 6 - 3 = 3
    *   **Available = [3, 1, 3]**

*   **Need Matrix (需求矩阵):**

| Process | Need (A B C) |
| :------ | :----------- |
| P0      | 3 3 3        |
| P1      | 2 1 0        |
| P2      | 1 2 1        |

#### **Step 2: Apply the Safety Algorithm / 步骤2：应用安全算法**

*   **EN:** We check for a process `Pi` where `Need[i] <= Work`. We start with `Work = Available`.
*   **中文:** 我们寻找是否存在一个进程 `Pi` 满足 `Need[i] <= Work`。我们从 `Work = Available` 开始。

**Let Work = Available = [3, 1, 3]**

1.  **Check P0:** `Need(3,3,3)` is **not <=** `Work(3,1,3)`. (Needs 3 of B, only 1 available). **P0 must wait.**
    **检查 P0:** `Need(3,3,3)` **不满足 <=** `Work(3,1,3)`。（需要3个B，但只有1个可用）。**P0必须等待。**
2.  **Check P1:** `Need(2,1,0)` **is <=** `Work(3,1,3)`. **Success!** P1 can run.
    **检查 P1:** `Need(2,1,0)` **满足 <=** `Work(3,1,3)`。**成功！** P1可以运行。
    *   **EN:** We simulate P1 finishing and releasing its resources.
    *   **中文:** 我们模拟P1完成并释放其资源。
    *   `Work = Work + Allocation[P1] = [3,1,3] + [3,1,2] = [6,2,5]`
    *   **Safe Sequence so far: <P1>**
3.  **Check P2** (with new Work): `Need(1,2,1)` **is <=** `Work(6,2,5)`. **Success!** P2 can run.
    **检查 P2** (使用新的 Work): `Need(1,2,1)` **满足 <=** `Work(6,2,5)`。**成功！** P2可以运行。
    *   **EN:** Simulate P2 finishing.
    *   **中文:** 模拟P2完成。
    *   `Work = Work + Allocation[P2] = [6,2,5] + [2,1,1] = [8,3,6]`
    *   **Safe Sequence so far: <P1, P2>**
4.  **Check P0 again** (with new Work): `Need(3,3,3)` **is <=** `Work(8,3,6)`. **Success!** P0 can run.
    **再次检查 P0** (使用新的 Work): `Need(3,3,3)` **满足 <=** `Work(8,3,6)`。**成功！** P0可以运行。
    *   **Final Safe Sequence: <P1, P2, P0>**

#### **Conclusion for Part 1 / 第一部分结论**

*   **EN:** Yes, the system is in a **safe state**. A safe sequence is **<P1, P2, P0>**.
*   **中文:** 是的，系统处于**安全状态**。一个安全序列是 **<P1, P2, P0>**。

---

### **Part 2: What if P2 requests (1,1,0)? / 第二部分：如果 P2 请求 (1,1,0) 会怎样？**

#### **Step 1: Check if the request is valid / 步骤1：检查请求是否有效**

1.  **EN:** Is `Request(1,1,0)` <= `Need[P2](1,2,1)`? **Yes.** (The process is not asking for more than it said it would need).
    **中文:** `Request(1,1,0)` 是否 <= `Need[P2](1,2,1)`？**是。** (进程请求的没有超过它声明的最大需求)。
2.  **EN:** Is `Request(1,1,0)` <= `Available(3,1,3)`? **Yes.** (The system has enough resources to fulfill the request right now).
    **中文:** `Request(1,1,0)` 是否 <= `Available(3,1,3)`？**是。** (系统当前有足够的资源来满足该请求)。

Since both checks pass, we must proceed to the safety check.
由于两个检查都通过了，我们必须继续进行安全检查。

#### **Step 2: Create the Hypothetical State / 步骤2：创建假设状态**

*   **EN:** We pretend to grant the request and update the system state.
*   **中文:** 我们假设批准该请求并更新系统状态。
*   `Available` becomes `[3,1,3] - [1,1,0] = [2,0,3]`
*   `Allocation[P2]` becomes `[2,1,1] + [1,1,0] = [3,2,1]`
*   `Need[P2]` becomes `[1,2,1] - [1,1,0] = [0,1,1]`

#### **Step 3: Run the Safety Algorithm on the NEW state / 步骤3：对新状态运行安全算法**

**Let Work = New Available = [2, 0, 3]**

1.  **Check P0:** `Need(3,3,3)` is **not <=** `Work(2,0,3)`. **P0 must wait.**
    **检查 P0:** `Need(3,3,3)` **不满足 <=** `Work(2,0,3)`。**P0必须等待。**
2.  **Check P1:** `Need(2,1,0)` is **not <=** `Work(2,0,3)`. (Needs 1 of B, 0 available). **P1 must wait.**
    **检查 P1:** `Need(2,1,0)` **不满足 <=** `Work(2,0,3)`。(需要1个B，但0个可用)。**P1必须等待。**
3.  **Check P2:** `Need(0,1,1)` is **not <=** `Work(2,0,3)`. (Needs 1 of B, 0 available). **P2 must wait.**
    **检查 P2:** `Need(0,1,1)` **不满足 <=** `Work(2,0,3)`。(需要1个B，但0个可用)。**P2必须等待。**

*   **EN:** We have gone through all processes, and **not a single one can run**. The system is stuck.
*   **中文:** 我们已经检查了所有进程，**没有一个可以运行**。系统卡住了。

#### **Conclusion for Part 2 / 第二部分结论**

*   **EN:** The resulting hypothetical state is **UNSAFE**. Therefore, the Banker's Algorithm dictates that the OS **must deny the request** from P2. P2 is placed in a waiting state, and the system is not changed.
*   **中文:** 最终的假设状态是**不安全的**。因此，银行家算法规定操作系统**必须拒绝 P2 的请求**。P2被置于等待状态，系统状态保持不变。
