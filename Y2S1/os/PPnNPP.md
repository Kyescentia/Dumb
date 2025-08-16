### **Priority Scheduling / 优先级调度**

*   **EN:** This algorithm assigns a priority to each process. The CPU is allocated to the process with the highest priority. We need to specify if it's preemptive or non-preemptive.
*   **中文:** 该算法为每个进程分配一个优先级。CPU会分配给优先级最高的进程。我们需要明确它是抢占式还是非抢占式的。

#### **Example Data Set / 示例数据集**

Let's use a new data set with a priority column.
我们使用一个带有优先级列的新数据集。

**Rule: A lower number means a higher priority.**
**规则：数字越小，优先级越高。**

| Job (作业) | Arrival Time (到达时间) | CPU Cycle (CPU周期) | Priority (优先级) |
| :--------- | :---------------------- | :------------------ | :---------------- |
| A          | 0                       | 6                   | 3                 |
| B          | 2                       | 4                   | 1 (Highest)       |
| C          | 3                       | 2                   | 4 (Lowest)        |
| D          | 5                       | 5                   | 2                 |

---

### **1. Non-Preemptive Priority / 非抢占式优先级调度**

*   **EN:** Once a process starts running, it will not be interrupted. It runs to completion. The scheduler only makes a decision when the CPU is free.
*   **中文:** 一旦一个进程开始运行，它就不会被中断，会一直运行直到完成。调度器只在CPU空闲时才做决策。

#### **Gantt Chart Visualization / 甘特图可视化**
```
0        6         10        15      17
|--------|---------|---------|------|
|   A    |    B    |    D    |  C   |
|--------|---------|---------|------|
```

#### **Step-by-Step Walkthrough / 分步解析**

1.  **At time 0:** Only Job A (Priority 3) has arrived. It must run. Since it's non-preemptive, it will run for its full 6 cycles.
    **时间 0:** 只有作业 A (优先级 3) 到达，必须运行它。由于是非抢占式的，它将完整运行6个周期。
2.  **At time 6:** Job A finishes. The CPU is free. By now, jobs B (Prio 1), C (Prio 4), and D (Prio 2) have all arrived. We check their priorities:
    **时间 6:** 作业 A 完成，CPU空闲。此时，作业 B (优先级 1), C (优先级 4), 和 D (优先级 2) 都已到达。我们检查它们的优先级：
    *   B has the highest priority (1). So, B runs next.
    *   B 的优先级最高 (1)。所以，B 接下来运行。
3.  Job B runs from **time 6 to 10** (4 cycles).
    作业 B 从 **时间 6 运行到 10** (4个周期)。
4.  **At time 10:** Job B finishes. The remaining available jobs are C (Prio 4) and D (Prio 2). Job D has the higher priority (2). So, D runs next.
    **时间 10:** 作业 B 完成。剩余的可用作业是 C (优先级 4) 和 D (优先级 2)。作业 D 的优先级更高 (2)。所以，D 接下来运行。
5.  Job D runs from **time 10 to 15** (5 cycles).
    作业 D 从 **时间 10 运行到 15** (5个周期)。
6.  **At time 15:** Only Job C is left. It runs from **time 15 to 17**.
    **时间 15:** 只剩下作业 C。它从 **时间 15 运行到 17**。

---

### **2. Preemptive Priority / 抢占式优先级调度**

*   **EN:** A running process can be interrupted (preempted) if a new process with a higher priority arrives.
*   **中文:** 如果一个具有更高优先级的新进程到达，正在运行的进程可能会被中断 (抢占)。

#### **Gantt Chart Visualization / 甘特图可视化**
```
0    2         6         11      13   17
|----|---------|---------|------|----|
| A  |    B    |    D    |  C   | A  |
|----|---------|---------|------|----|
```

#### **Step-by-Step Walkthrough / 分步解析**

1.  **Time 0:** A arrives (Prio 3) and starts running.
    **时间 0:** A 到达 (优先级 3) 并开始运行。
2.  **Time 2:** B arrives. Its priority (1) is higher than A's priority (3). **PREEMPTION!** B interrupts A. B starts running. (A has 4 cycles remaining).
    **时间 2:** B 到达。它的优先级 (1) 高于 A 的优先级 (3)。**发生抢占！** B 中断 A 并开始运行。(A 剩余4个周期)。
3.  **Time 3:** C arrives. Its priority (4) is lower than B's (1), so B continues to run.
    **时间 3:** C 到达。它的优先级 (4) 低于 B 的 (1)，所以 B 继续运行。
4.  **Time 5:** D arrives. Its priority (2) is lower than B's (1), so B continues to run.
    **时间 5:** D 到达。它的优先级 (2) 低于 B 的 (1)，所以 B 继续运行。
5.  **Time 6:** B finishes its 4 cycles. The CPU is free. The Ready Queue contains: A (Prio 3, rem 4), C (Prio 4, rem 2), and D (Prio 2, rem 5).
    **时间 6:** B 完成其4个周期，CPU空闲。就绪队列中有：A (优先级 3, 剩余 4), C (优先级 4, 剩余 2), 和 D (优先级 2, 剩余 5)。
6.  Job D has the highest priority among them (2). So, D runs next.
    作业 D 在其中优先级最高 (2)。所以，D 接下来运行。
7.  **Time 11:** D finishes its 5 cycles. The CPU is free. The Ready Queue contains: A (Prio 3, rem 4) and C (Prio 4, rem 2).
    **时间 11:** D 完成其5个周期，CPU空闲。就绪队列中有：A (优先级 3, 剩余 4) 和 C (优先级 4, 剩余 2)。
8.  Job A has the higher priority (3). So, A runs next. But wait, C has lower priority, shouldn't it run last? No, we check priority first. A is higher. Let's recheck. D finishes at 11. Ready queue is A (prio 3) and C (prio 4). D (prio 2) is higher than A.  Ah, let's retrace from step 6.
    
    *Correction:*
    6. **Time 6:** B finishes. Ready queue: A (Prio 3, rem 4), C (Prio 4, rem 2), D (Prio 2, rem 5). D has the highest priority (2). D runs from **time 6 to 11**.
    7. **Time 11:** D finishes. Ready queue: A (Prio 3, rem 4), C (Prio 4, rem 2). A has the higher priority (3). A runs from **time 11 to 15**. (It runs for its remaining 4 cycles).
    8. **Time 15:** A finishes. Only C is left. C runs from **time 15 to 17**.

    Let's fix the Gantt chart and walkthrough. This is a common mistake and good to catch! The previous chart was wrong.
    
    **Corrected Walkthrough:**
    1.  **Time 0-2:** A runs (rem 4).
    2.  **Time 2-6:** B (Prio 1) arrives and preempts A. B runs for 4 cycles and finishes.
    3.  **Time 6-11:** B is done. Ready Queue: A (Prio 3, rem 4), C (Prio 4, rem 2), D (Prio 2, rem 5). D is highest priority. D runs for 5 cycles and finishes.
    4.  **Time 11-15:** D is done. Ready Queue: A (Prio 3, rem 4), C (Prio 4, rem 2). A is higher priority. A runs for its remaining 4 cycles and finishes.
    5.  **Time 15-17:** A is done. Only C is left. C runs for 2 cycles and finishes.

#### **Corrected Gantt Chart Visualization / 修正后的甘特图可视化**
```
0    2         6         11         15     17
|----|---------|---------|----------|------|
| A  |    B    |    D    |     A    |   C  |
|----|---------|---------|----------|------|
```

---
