
---

### **Networking Essentials Midterm (Bilingual)**
### **网络基础期中 (中英双语)**

---

### **Chapter 1: Quality of Service (QoS) Concepts**
### **第1章：服务质量 (QoS) 概念**

**1. Factors Affecting QoS / 影响QoS的因素**
*   **Bandwidth / 带宽**
    *   **EN:** The capacity of a network link, measured in bits per second (bps). Congestion occurs when traffic exceeds available bandwidth.
    *   **中文:** 网络链路的容量，以比特每秒 (bps) 为单位。当流量超过可用带宽时会发生拥塞。
*   **Delay (Latency) / 延迟**
    *   **EN:** The time it takes for a packet to travel from source to destination. High delay can ruin real-time applications.
    *   **中文:** 数据包从源头传输到目的地所需的时间。高延迟会破坏实时应用的体验。
*   **Jitter / 抖动**
    *   **EN:** The variation in the delay of received packets. Causes choppy voice and video.
    *   **中文:** 接收到的数据包延迟的变化。这会导致语音和视频通话卡顿。
*   **Packet Loss / 丢包**
    *   **EN:** Packets that are dropped and fail to reach their destination, usually due to network congestion.
    *   **中文:** 因网络拥塞等原因被丢弃，未能到达目的地的数据包。

**2. Queuing Algorithms / 队列算法**
*   **FIFO (First-In, First-Out) / 先进先出**
    *   **EN:** Processes packets in the exact order they arrive. No prioritization.
    *   **中文:** 完全按照数据包到达的顺序处理，没有优先级之分。
*   **WFQ (Weighted Fair Queuing) / 加权公平队列**
    *   **EN:** Prioritizes low-volume traffic and gives each flow a fair share of the bandwidth.
    *   **中文:** 优先处理低流量的通信，并为每个“流”公平地分配带宽。
*   **CBWFQ (Class-Based Weighted Fair Queuing) / 基于类的加权公平队列**
    *   **EN:** Guarantees a minimum amount of bandwidth to user-defined traffic classes during congestion.
    *   **中文:** 在拥塞期间，为用户自定义的流量类别保证一个最低的带宽。
*   **LLQ (Low Latency Queuing) / 低延迟队列**
    *   **EN:** Adds a strict priority queue to CBWFQ, essential for delay-sensitive traffic like voice.
    *   **中文:** 在CBWFQ的基础上增加一个严格的优先队列，对语音等延迟敏感的流量至关重要。

**3. QoS Models / QoS模型**
*   **Best-Effort / 尽力而为**
    *   **EN:** The default model with no QoS. All packets are treated equally. Use when you have more than enough bandwidth.
    *   **中文:** 默认模型，无QoS。所有数据包被平等对待。适用于网络带宽非常充足的情况。
*   **Integrated Services (IntServ) / 集成服务**
    *   **EN:** Guarantees QoS by having applications reserve resources along the path. Not scalable.
    *   **中文:** 通过应用在路径上预留资源来保证QoS。可扩展性差。
*   **Differentiated Services (DiffServ) / 区分服务**
    *   **EN:** A scalable model that classifies and marks packets (using DSCP). Routers then give service based on the marking. Most common model.
    *   **中文:** 一种可扩展的模型，对数据包进行分类和标记 (使用DSCP)。路由器根据标记提供不同级别的服务。是最常见的模型。

---

### **Chapter 2: Application Layer Protocols**
### **第2章：应用层协议**

**1. Remote Networking Protocols / 远程网络协议**
*   **Telnet**
    *   **EN:** Insecure protocol that sends all data, including passwords, in **plaintext**. Uses TCP Port 23.
    *   **中文:** 不安全的协议，所有数据（包括密码）都以**明文**传输。使用TCP端口23。
*   **SSH (Secure Shell) / 安全外壳**
    *   **EN:** Secure standard that **encrypts** the entire session. Always use this instead of Telnet. Uses TCP Port 22.
    *   **中文:** 安全的标准，对整个会话进行**加密**。应始终使用SSH代替Telnet。使用TCP端口22。

**2. File Transfer Protocols / 文件传输协议**
*   **FTP (File Transfer Protocol) / 文件传输协议**
    *   **EN:** Insecure. Uses two connections: control (TCP 21) and data (TCP 20).
    *   **中文:** 不安全。使用两个连接：控制连接 (TCP 21) 和数据连接 (TCP 20)。
*   **SFTP (SSH File Transfer Protocol) / SSH文件传输协议**
    *   **EN:** Secure file transfer that runs over an encrypted SSH session (TCP 22).
    *   **中文:** 安全的文件传输，运行在加密的SSH会话之上 (TCP 22)。
*   **TFTP (Trivial File Transfer Protocol) / 简单文件传输协议**
    *   **EN:** Very simple, but has no security or authentication. Uses UDP 69. Used in trusted LANs for backing up IOS images and configs.
    *   **中文:** 非常简单，但没有安全或认证机制。使用UDP 69。常用于受信任的局域网中备份IOS镜像和配置文件。

---

### **Chapter 3: DHCP (Dynamic Host Configuration Protocol)**
### **第3章：DHCP (动态主机配置协议)**

**1. DORA Procedure / DORA流程**
The four steps a client uses to get an IP address. / 客户端获取IP地址的四个步骤。
1.  **Discover / 发现:** Client broadcasts to find DHCP servers. / 客户端广播以寻找DHCP服务器。
2.  **Offer / 提供:** Servers offer an IP address lease. / 服务器提供IP地址租约。
3.  **Request / 请求:** Client requests a specific lease from a server. / 客户端向特定服务器请求租约。
4.  **Acknowledge / 确认:** Server confirms the lease and provides other network info. / 服务器确认租约并提供其他网络信息。

**2. Configuration Commands / 配置命令 [IMPORTANT / 重要]**
*   **Exclude Addresses / 排除地址:**
    *   `ip dhcp excluded-address [start-ip] [end-ip]`
*   **Create Pool / 创建地址池:**
    *   `ip dhcp pool [pool-name]`
*   **Configure Pool / 配置地址池:**
    *   `network [network-id] [subnet-mask]` (Defines the subnet / 定义子网)
    *   `default-router [gateway-ip]` (Sets the gateway / 设置网关)
    *   `dns-server [dns-ip]` (Sets the DNS / 设置DNS)
*   **Configure DHCP Relay / 配置DHCP中继:**
    *   (On the interface facing clients / 在面向客户端的接口上)
    *   `ip helper-address [dhcp-server-ip]`

---

### **Chapter 4: WLAN Concepts**
### **第4章：WLAN 概念**

**1. Access Point (AP) Types / AP类型**
*   **Autonomous AP / 自治型AP ("胖AP")**
    *   **EN:** A standalone AP that is managed individually. Best for small networks.
    *   **中文:** 独立工作的AP，每个都需要单独配置和管理。适用于小型网络。
*   **Controller-Based AP (Lightweight AP) / 基于控制器的AP ("瘦AP")**
    *   **EN:** A "thin" AP that gets its configuration from a central Wireless LAN Controller (WLC). Essential for large enterprise networks.
    *   **中文:** "瘦"AP，其配置由一个中央的无线局域网控制器(WLC)提供。对于大型企业网络至关重要。

**2. CAPWAP (Control and Provisioning of Wireless Access Points)**
*   **EN:** The standard protocol that creates a secure tunnel between a WLC and a lightweight AP for management and control.
*   **中文:** WLC和瘦AP之间创建安全隧道的标准协议，用于管理和控制。

**3. WLAN Threats and Risks / WLAN威胁与风险**
*   **Rogue AP / 流氓AP**
    *   **EN:** An unauthorized AP connected to the corporate network, creating a major security hole.
    *   **中文:** 未经授权连接到公司网络的AP，会造成严重的安全漏洞。
*   **Man-in-the-Middle (MITM) Attack / 中间人攻击**
    *   **EN:** An attacker intercepts communication between two parties. The "Evil Twin" attack is a common example, where a fake AP mimics a real one.
    *   **中文:** 攻击者拦截双方通信。常见的例子是“邪恶双胞胎”攻击，即攻击者设置一个假的AP来模仿合法的AP。
*   **Denial of Service (DoS) Attack / 拒绝服务攻击**
    *   **EN:** An attempt to make a network unavailable, for example, by jamming the radio frequency or sending deauthentication frames.
    *   **中文:** 试图使网络资源不可用。例如，通过干扰无线电频率或发送伪造的“取消认证”帧。

---
