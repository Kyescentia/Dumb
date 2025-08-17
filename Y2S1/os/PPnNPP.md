### **Priority Scheduling / 优先级调度**

*   **EN:** This algorithm assigns a priority to each process. The CPU is allocated to the process with the highest priority. We need to specify if it's preemptive or non-preemptive.
*   **中文:** 该算法为每个进程分配一个优先级。CPU会分配给优先级最高的进程。我们需要明确它是抢占式还是非抢占式的。

### **Example Data Set / 示例数据集**

We will use the same data set for both examples.
两个示例将使用相同的数据集。

**Rule: A lower number means a higher priority.**
**规则：数字越小，优先级越高。**

| Job (作业) | Arrival Time (到达时间) | CPU Cycle (CPU周期) | Priority (优先级) |
| :--------- | :---------------------- | :------------------ | :---------------- |
| A          | 0                       | 6                   | 3                 |
| B          | 2                       | 4                   | 1 (Highest)       |
| C          | 3                       | 2                   | 4 (Lowest)        |
| D          | 5                       | 5                   | 2                 |

---

### **1. Non-Preemptive Priority (NPP) / 非抢占式优先级调度**

#### **Definition / 定义**

*   **EN:** In Non-Preemptive Priority scheduling, once a process is given the CPU, it runs to completion without being interrupted by any other process, even if a higher-priority process arrives. The scheduler only chooses a new process when the current one finishes.
*   **中文:** 在非抢占式优先级调度中，一旦一个进程获得了CPU，它就会一直运行直到完成，不会被任何其他进程中断，即使有更高优先级的进程到达也是如此。调度器只在当前进程完成时才选择新进程。

#### **Gantt Chart Visualization / 甘特图可视化**
```
0        6         10        15      17
|--------|---------|---------|------|
|   A    |    B    |    D    |  C   |
|--------|---------|---------|------|
```

#### **Step-by-Step Walkthrough / 分步解析**

1.  **Time 0:** Only Job A (Priority 3) is in the ready queue. It starts executing. Because this is **non-preemptive**, it will run for its entire 6 cycles, finishing at time 6.
    **时间 0:** 就绪队列中只有作业 A (优先级 3)。它开始执行。因为这是**非抢占式**的，它将完整运行其6个周期的时长，并在时间 6 完成。
2.  **Time 6:** Job A is finished. The CPU is now available. We look at all the jobs that have arrived by now: B (Prio 1), C (Prio 4), and D (Prio 2).
    **时间 6:** 作业 A 完成，CPU空闲。我们查看此时已到达的所有作业：B (优先级 1)、C (优先级 4) 和 D (优先级 2)。
3.  We compare their priorities. Job B has the highest priority (1). So, Job B starts running. It runs for 4 cycles.
    我们比较它们的优先级。作业 B 的优先级最高 (1)。因此，作业 B 开始运行，运行时长为4个周期。
4.  **Time 10:** Job B finishes (6 + 4 = 10). The remaining jobs in the queue are C (Prio 4) and D (Prio 2).
    **时间 10:** 作业 B 完成 (6 + 4 = 10)。队列中剩余的作业是 C (优先级 4) 和 D (优先级 2)。
5.  Comparing them, Job D has the higher priority (2). Job D starts running. It runs for 5 cycles.
    比较两者，作业 D 的优先级更高 (2)。作业 D 开始运行，运行时长为5个周期。
6.  **Time 15:** Job D finishes (10 + 5 = 15). The only job left is C.
    **时间 15:** 作业 D 完成 (10 + 5 = 15)。唯一剩下的作业是 C。
7.  **Time 17:** Job C runs for its 2 cycles and finishes (15 + 2 = 17).
    **时间 17:** 作业 C 运行其2个周期并完成 (15 + 2 = 17)。

#### **Calculation Table / 计算表**

| Job | Arrival | CPU | **Finish Time** | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :-------------- | :--------------------------------- | :------------------------------ |
| A   | 0       | 6   | 6               | 6 - 0 = **6**                      | 6 - 6 = **0**                   |
| B   | 2       | 4   | 10              | 10 - 2 = **8**                     | 8 - 4 = **4**                   |
| C   | 3       | 2   | 17              | 17 - 3 = **14**                    | 14 - 2 = **12**                 |
| D   | 5       | 5   | 15              | 15 - 5 = **10**                    | 10 - 5 = **5**                  |
|     |         |     |                 | **Average: 9.5**                   | **Average: 5.25**               |

---

### **2. Preemptive Priority (PP) / 抢占式优先级调度**

#### **Definition / 定义**

*   **EN:** In Preemptive Priority scheduling, the currently running process can be interrupted (preempted) if a new process with a *higher priority* arrives. The scheduler constantly checks if a better process is available.
*   **中文:** 在抢占式优先级调度中，如果一个具有更高优先级的新进程到达，当前正在运行的进程可能会被中断（抢占）。调度器会持续检查是否有更优的进程可用。

#### **Gantt Chart Visualization / 甘特图可视化**
```
0    2         6         11         15     17
|----|---------|---------|----------|------|
| A  |    B    |    D    |     A    |   C  |
|----|---------|---------|----------|------|
```

#### **Step-by-Step Walkthrough / 分步解析**

1.  **Time 0:** Job A (Prio 3) arrives and starts running.
    **时间 0:** 作业 A (优先级 3) 到达并开始运行。
2.  **Time 2:** Job B arrives. Its priority (1) is **higher** than the currently running Job A's priority (3). **PREEMPTION occurs!** Job A is paused and sent back to the ready queue. Job A has (6 - 2) = 4 cycles remaining. Job B starts running.
    **时间 2:** 作业 B 到达。它的优先级 (1) **高于**当前运行的作业 A 的优先级 (3)。**发生抢占！** 作业 A 被暂停并送回就绪队列。作业 A 剩余 (6 - 2) = 4 个周期。作业 B 开始运行。
3.  **Time 2 to 6:** Job B runs. During this time, C (at time 3) and D (at time 5) arrive, but their priorities (4 and 2) are lower than B's (1), so B is not interrupted. Job B runs for its full 4 cycles and finishes at time 6.
    **时间 2 到 6:** 作业 B 运行。在此期间，C (在时间 3) 和 D (在时间 5) 到达，但它们的优先级 (4 和 2) 都低于 B 的 (1)，所以 B 不会被中断。作业 B 完整运行4个周期，并在时间 6 完成。
4.  **Time 6:** Job B is finished. The CPU is available. The ready queue now contains: A (Prio 3, rem 4), C (Prio 4, rem 2), and D (Prio 2, rem 5).
    **时间 6:** 作业 B 完成，CPU空闲。就绪队列中现在有：A (优先级 3, 剩余 4)、C (优先级 4, 剩余 2) 和 D (优先级 2, 剩余 5)。
5.  Comparing priorities, Job D has the highest priority (2). Job D starts running. It runs for 5 cycles.
    比较优先级，作业 D 的优先级最高 (2)。作业 D 开始运行，运行时长为5个周期。
6.  **Time 11:** Job D finishes (6 + 5 = 11). The ready queue contains: A (Prio 3, rem 4) and C (Prio 4, rem 2).
    **时间 11:** 作业 D 完成 (6 + 5 = 11)。就绪队列中有：A (优先级 3, 剩余 4) 和 C (优先级 4, 剩余 2)。
7.  Job A has the higher priority (3). Job A resumes and runs for its remaining 4 cycles.
    作业 A 的优先级更高 (3)。作业 A 恢复运行，完成其剩余的4个周期。
8.  **Time 15:** Job A finishes (11 + 4 = 15). The only job left is C.
    **时间 15:** 作业 A 完成 (11 + 4 = 15)。唯一剩下的作业是 C。
9.  **Time 17:** Job C runs for its 2 cycles and finishes (15 + 2 = 17).
    **时间 17:** 作业 C 运行其2个周期并完成 (15 + 2 = 17)。

#### **Calculation Table / 计算表**

| Job | Arrival | CPU | **Finish Time** | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :-------------- | :--------------------------------- | :------------------------------ |
| A   | 0       | 6   | 15              | 15 - 0 = **15**                    | 15 - 6 = **9**                  |
| B   | 2       | 4   | 6               | 6 - 2 = **4**                      | 4 - 4 = **0**                   |
| C   | 3       | 2   | 17              | 17 - 3 = **14**                    | 14 - 2 = **12**                 |
| D   | 5       | 5   | 11              | 11 - 5 = **6**                     | 6 - 5 = **1**                   |
|     |         |     |                 | **Average: 9.75**                  | **Average: 5.5**                |
