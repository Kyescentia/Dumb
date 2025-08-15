### **Example Data Set / 示例数据集**

Let's use the following 5 processes for all examples:
我们在所有示例中使用以下5个进程：

| Job (作业) | Arrival Time (到达时间) | CPU Cycle (CPU周期) |
| :--------- | :---------------------- | :------------------ |
| A          | 0                       | 8                   |
| B          | 1                       | 4                   |
| C          | 2                       | 2                   |
| D          | 3                       | 1                   |
| E          | 4                       | 5                   |

---

### **1. FCFS (First-Come, First-Served) / 先到先得**

*   **EN:** This is a **non-preemptive** algorithm. Processes are executed in the exact order they arrive.
*   **中文:** 这是一个**非抢占式**算法。进程完全按照它们的到达顺序执行。

#### **Execution Timeline (Gantt Chart) / 执行时间轴 (甘特图)**
```
0        8         12    14   15        20
|--------|---------|-----|----|---------|
|   A    |    B    |  C  | D  |    E    |
|--------|---------|-----|----|---------|
```


#### **Step-by-Step Walkthrough / 分步解析**

1.  **At time 0:** Job A arrives and starts running immediately.
    **时间 0:** 作业 A 到达并立即开始运行。
2.  **At time 8:** Job A finishes. All other jobs (B, C, D, E) have arrived. We serve them in their arrival order: B, then C, then D, then E.
    **时间 8:** 作业 A 完成。所有其他作业 (B, C, D, E) 均已到达。我们按它们的到达顺序服务：先是 B，然后是 C，接着是 D，最后是 E。
3.  Job B runs from **time 8 to 12** (4 cycles).
    作业 B 从 **时间 8 运行到 12** (4个周期)。
4.  Job C runs from **time 12 to 14** (2 cycles).
    作业 C 从 **时间 12 运行到 14** (2个周期)。
5.  Job D runs from **time 14 to 15** (1 cycle).
    作业 D 从 **时间 14 运行到 15** (1个周期)。
6.  Job E runs from **time 15 to 20** (5 cycles).
    作业 E 从 **时间 15 运行到 20** (5个周期)。

#### **Calculations / 计算**

| Job | Arrival | CPU | Finish | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :----- | :--------------------------------- | :------------------------------ |
| A   | 0       | 8   | 8      | 8 - 0 = **8**                      | 8 - 8 = **0**                   |
| B   | 1       | 4   | 12     | 12 - 1 = **11**                    | 11 - 4 = **7**                  |
| C   | 2       | 2   | 14     | 14 - 2 = **12**                    | 12 - 2 = **10**                 |
| D   | 3       | 1   | 15     | 15 - 3 = **12**                    | 12 - 1 = **11**                 |
| E   | 4       | 5   | 20     | 20 - 4 = **16**                    | 16 - 5 = **11**                 |
|     |         |     |        | **Average: 11.8**                  | **Average: 7.8**                |

---

### **2. SJN (Shortest Job Next) / 最短作业优先**

*   **EN:** This is a **non-preemptive** algorithm. When the CPU becomes free, it selects the available process with the shortest CPU cycle to run next.
*   **中文:** 这是一个**非抢占式**算法。当CPU空闲时，它会从已到达的进程中选择CPU周期最短的那个来运行。

#### **Execution Timeline (Gantt Chart) / 执行时间轴 (甘特图)**
```
0        8  9    11         15        20
|--------|--|----|----------|---------|
|   A    |D | C  |     B    |    E    |
|--------|--|----|----------|---------|
```


#### **Step-by-Step Walkthrough / 分步解析**

1.  **At time 0:** Only Job A is available. It must run. It runs until it finishes.
    **时间 0:** 只有作业 A 可用，必须运行它。它会一直运行直到完成。
2.  **At time 8:** Job A finishes. The CPU is now free. By this time, all other jobs (B, C, D, E) have arrived. We check their CPU cycles:
    **时间 8:** 作业 A 完成，CPU空闲。此时，所有其他作业 (B, C, D, E) 都已到达。我们检查它们的CPU周期：
    *   B: 4, C: 2, D: 1, E: 5
3.  Job D has the shortest cycle (1), so it runs next from **time 8 to 9**.
    作业 D 的周期最短 (1)，所以它接下来运行，从 **时间 8 到 9**。
4.  **At time 9:** The CPU is free. The remaining jobs are B(4), C(2), E(5). Job C is the shortest, so it runs next from **time 9 to 11**.
    **时间 9:** CPU空闲。剩余作业为 B(4), C(2), E(5)。作业 C 最短，所以它接下来运行，从 **时间 9 到 11**。
5.  **At time 11:** The CPU is free. Remaining jobs are B(4), E(5). Job B is shorter, so it runs from **time 11 to 15**.
    **时间 11:** CPU空闲。剩余作业为 B(4), E(5)。作业 B 更短，所以它运行，从 **时间 11 到 15**。
6.  **At time 15:** Only Job E is left. It runs from **time 15 to 20**.
    **时间 15:** 只剩下作业 E。它运行，从 **时间 15 到 20**。

#### **Calculations / 计算**

| Job | Arrival | CPU | Finish | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :----- | :--------------------------------- | :------------------------------ |
| A   | 0       | 8   | 8      | 8 - 0 = **8**                      | 8 - 8 = **0**                   |
| B   | 1       | 4   | 15     | 15 - 1 = **14**                    | 14 - 4 = **10**                 |
| C   | 2       | 2   | 11     | 11 - 2 = **9**                     | 9 - 2 = **7**                   |
| D   | 3       | 1   | 9      | 9 - 3 = **6**                      | 6 - 1 = **5**                   |
| E   | 4       | 5   | 20     | 20 - 4 = **16**                    | 16 - 5 = **11**                 |
|     |         |     |        | **Average: 10.6**                  | **Average: 6.6**                |

---

### **3. SRT (Shortest Remaining Time) / 最短剩余时间**

*   **EN:** This is the **preemptive** version of SJN. The scheduler always chooses the process with the shortest remaining time. It can interrupt (preempt) a running process if a new process arrives with a shorter remaining time.
*   **中文:** 这是SJN的**抢占式**版本。调度器总是选择剩余时间最短的进程。如果一个新到达的进程比当前运行进程的剩余时间更短，它可以中断 (抢占) 当前进程。

#### **Execution Timeline (Gantt Chart) / 执行时间轴 (甘特图)**
```
0  1  2    4  5      8           13                  20
|--|--|----|--|------|-----------|-------------------|
| A|B | C  |D |   B  |      E    |         A         |
|--|--|----|--|------|-----------|-------------------|
```

#### **Step-by-Step Walkthrough / 分步解析**

1.  **Time 0:** A arrives (CPU=8). A starts running.
    **时间 0:** A 到达 (CPU=8)。A 开始运行。
2.  **Time 1:** B arrives (CPU=4). A has 7 time left. Since 4 < 7, B **preempts** A. B starts running. (A returns to Ready Queue with 7 time left).
    **时间 1:** B 到达 (CPU=4)。A 剩余7。因为 4 < 7，B **抢占** A。B 开始运行。(A 返回就绪队列，剩余7)。
3.  **Time 2:** C arrives (CPU=2). B has 3 time left. Since 2 < 3, C **preempts** B. C starts running. (B returns to Ready Queue with 3 time left).
    **时间 2:** C 到达 (CPU=2)。B 剩余3。因为 2 < 3，C **抢占** B。C 开始运行。(B 返回就绪队列，剩余3)。
4.  **Time 3:** D arrives (CPU=1). C has 1 time left. Since 1 < 1 is false (they are equal), C continues. *(Note: Common rule is the running process continues on a tie).*
    **时间 3:** D 到达 (CPU=1)。C 剩余1。因为 1 < 1 是错误的 (它们相等)，所以C继续运行。*(注：通常规则是在相等时，当前运行的进程继续)*。
5.  **Time 4:** C finishes. E arrives (CPU=5). The Ready Queue contains: A(7), B(3), D(1), E(5). D has the shortest remaining time (1), so D runs.
    **时间 4:** C 完成。E 到达 (CPU=5)。就绪队列中有：A(7), B(3), D(1), E(5)。D 的剩余时间最短 (1)，所以 D 运行。
6.  **Time 5:** D finishes. Ready Queue: A(7), B(3), E(5). B is the shortest (3), so B runs.
    **时间 5:** D 完成。就绪队列：A(7), B(3), E(5)。B 最短 (3)，所以 B 运行。
7.  **Time 8:** B finishes. Ready Queue: A(7), E(5). E is the shortest (5), so E runs.
    **时间 8:** B 完成。就绪队列：A(7), E(5)。E 最短 (5)，所以 E 运行。
8.  **Time 13:** E finishes. Only A is left. A runs for its remaining 7 units.
    **时间 13:** E 完成。只剩下 A。A 运行其剩余的7个单位。
9.  **Time 20:** A finishes.
    **时间 20:** A 完成。

#### **Calculations / 计算**

| Job | Arrival | CPU | Finish | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :----- | :--------------------------------- | :------------------------------ |
| A   | 0       | 8   | 20     | 20 - 0 = **20**                    | 20 - 8 = **12**                 |
| B   | 1       | 4   | 8      | 8 - 1 = **7**                      | 7 - 4 = **3**                   |
| C   | 2       | 2   | 4      | 4 - 2 = **2**                      | 2 - 2 = **0**                   |
| D   | 3       | 1   | 5      | 5 - 3 = **2**                      | 2 - 1 = **1**                   |
| E   | 4       | 5   | 13     | 13 - 4 = **9**                     | 9 - 5 = **4**                   |
|     |         |     |        | **Average: 8.0**                   | **Average: 4.0**                |

---

### **4. RR (Round Robin) / 轮询调度**

*   **EN:** This is a **preemptive** algorithm. Each process gets a fixed time slice called a **Time Quantum**. We will use a **Time Quantum of 3**. If a process is not finished after its quantum, it is preempted and moved to the back of the Ready Queue.
*   **中文:** 这是一个**抢占式**算法。每个进程获得一个固定的时间片，称为**时间量**。我们使用 **时间量 = 3**。如果一个进程在时间片结束后仍未完成，它将被抢占并移至就绪队列的末尾。

#### **Execution Timeline (Gantt Chart) / 执行时间轴 (甘特图)**
```
0    3    6   8  9      12     15   16   18   20
|----|----|---|--|------|------|----|----|----|
| A  | B  | C |D |   A  |   E  | B  | A  | E  |
|----|----|---|--|------|------|----|----|----|
```


#### **Step-by-Step Walkthrough / 分步解析**
(Ready Queue state is shown at the beginning of each time slice / 每个时间片开始时显示就绪队列状态)

1.  **Time 0:** Queue: [A]. A runs for 3 units.
    **时间 0:** 队列: [A]。A 运行3个单位。
2.  **Time 3:** A's quantum ends (5 left). B, C, D have arrived. Queue becomes [B, C, D, A]. B runs for 3 units.
    **时间 3:** A 的时间片结束 (剩余5)。B, C, D 已到达。队列变为 [B, C, D, A]。B 运行3个单位。
3.  **Time 6:** B's quantum ends (1 left). E has arrived. Queue becomes [C, D, A, E, B]. C runs for 2 units and finishes.
    **时间 6:** B 的时间片结束 (剩余1)。E 已到达。队列变为 [C, D, A, E, B]。C 运行2个单位并完成。
4.  **Time 8:** C finishes early. The next in queue is D. D runs for 1 unit and finishes.
    **时间 8:** C 提前完成。队列中的下一个是 D。D 运行1个单位并完成。
5.  **Time 9:** D finishes early. The next in queue is A. A runs for another 3 units.
    **时间 9:** D 提前完成。队列中的下一个是 A。A 再运行3个单位。
6.  **Time 12:** A's quantum ends (2 left). Queue becomes [E, B, A]. E runs for 3 units.
    **时间 12:** A 的时间片结束 (剩余2)。队列变为 [E, B, A]。E 运行3个单位。
7.  **Time 15:** E's quantum ends (2 left). Queue becomes [B, A, E]. B runs for 1 unit and finishes.
    **时间 15:** E 的时间片结束 (剩余2)。队列变为 [B, A, E]。B 运行1个单位并完成。
8.  **Time 16:** B finishes early. The next in queue is A. A runs for 2 units and finishes.
    **时间 16:** B 提前完成。队列中的下一个是 A。A 运行2个单位并完成。
9.  **Time 18:** A finishes early. The next in queue is E. E runs for its final 2 units.
    **时间 18:** A 提前完成。队列中的下一个是 E。E 运行其最后的2个单位。
10. **Time 20:** E finishes. All jobs are done.
    **时间 20:** E 完成。所有作业完成。

#### **Calculations / 计算**

| Job | Arrival | CPU | Finish | Turnaround Time (Finish - Arrival) | Waiting Time (Turnaround - CPU) |
| :-- | :------ | :-- | :----- | :--------------------------------- | :------------------------------ |
| A   | 0       | 8   | 18     | 18 - 0 = **18**                    | 18 - 8 = **10**                 |
| B   | 1       | 4   | 16     | 16 - 1 = **15**                    | 15 - 4 = **11**                 |
| C   | 2       | 2   | 8      | 8 - 2 = **6**                      | 6 - 2 = **4**                   |
| D   | 3       | 1   | 9      | 9 - 3 = **6**                      | 6 - 1 = **5**                   |
| E   | 4       | 5   | 20     | 20 - 4 = **16**                    | 16 - 5 = **11**                 |
|     |         |     |        | **Average: 12.2**                  | **Average: 8.2**                |
