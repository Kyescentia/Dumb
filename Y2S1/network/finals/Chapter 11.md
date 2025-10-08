# **Chapter 11: Network Troubleshooting**

This chapter covers the methodologies, tools, and documentation necessary for effective network troubleshooting.

#### **11.1 Network Documentation**

*   **Overview**: Accurate and complete network documentation is crucial for effectively monitoring and troubleshooting networks. All documentation should be stored in a centralized location with backups kept separately.

*   **Types of Documentation**:
    *   **Network Topology Diagrams**:
        *   **Physical Topology**: Shows the physical location of devices, wiring closets, and cabling. It answers the question "Where is the device located?"
        *   **Logical Topology**: Illustrates how data flows across the network, including IP addresses, VLANs, subnets, and device names. It answers the question "How are devices connected logically?"
    *   **Network Device Documentation**: Contains up-to-date records of all network hardware and software. This should include:
        *   **Router Documentation**: Model, IOS version, hostname, location, and detailed interface information (IP addresses, MAC addresses, descriptions).
        *   **Switch Documentation**: Similar details as routers, with additional information on port configurations, VLAN assignments, and VTP settings.
        *   **End-System Documentation**: Device OS, IP address, MAC address, default gateway, DNS server, and any network applications running.

*   **Establishing a Network Baseline**:
    *   A baseline is a snapshot of normal network performance, used as a reference point to identify problems.
    *   It helps verify if the network design meets business needs and identifies areas of congestion or underutilization.
    *   **Steps to Create a Baseline**:
        1.  **Determine Data to Collect**: Start with simple but critical variables like interface utilization and CPU utilization.
        2.  **Identify Devices and Ports of Interest**: Use the logical topology to pinpoint key devices (servers, routers) and critical interfaces to monitor.
        3.  **Determine Baseline Duration**: Capture data for a minimum of seven days to observe typical usage patterns. A two-to-four-week period is generally adequate.

*   **Data Measurement Commands (Cisco IOS)**: A set of `show` commands is used to collect data for documentation and baselining.
    *   `show version`: Displays device software and hardware details.
    *   `show ip interface brief`: Provides a summary of interface status and IP addresses.
    *   `show interfaces`: Offers detailed statistics for all interfaces, including errors and drops.
    *   `show ip route`: Shows the IPv4 routing table.
    *   `show running-config`: Displays the active configuration.

---

#### **11.2 Troubleshooting Process**

*   **General Procedures**: Using a structured, systematic method reduces troubleshooting time and prevents unnecessary changes. A simple three-stage flowchart is:
    1.  **Gather Symptoms**: Collect information about the problem.
    2.  **Isolate the Problem**: Narrow down the possible causes.
    3.  **Implement Corrective Action**: Apply a fix. If it works, document it. If not, undo the change and repeat the process.

*   **Seven-Step Troubleshooting Process**: A more detailed and formal methodology.
    1.  **Define the Problem**: Clearly state what is not working.
    2.  **Gather Information**: Collect data from devices, users, and NMS tools.
    3.  **Analyze Information**: Review the collected data to form a hypothesis.
    4.  **Eliminate Possible Causes**: Rule out potential causes one by one.
    5.  **Propose Hypothesis**: State the most likely cause of the problem.
    6.  **Test Hypothesis**: Implement a potential solution and have a rollback plan.
    7.  **Solve the Problem**: Document the final solution for future reference.

*   **Structured Troubleshooting Methods**:
    *   **Top-Down**: Starts at the Application layer and works down. Best for simple or application-related issues.
    *   **Bottom-Up**: Starts at the Physical layer and works up. Ideal for suspected hardware or cabling problems.
    *   **Divide-and-Conquer**: Starts at a middle layer (e.g., Network layer) and tests both up and down. A common approach is to start with a `ping`.
    *   **Follow-the-Path**: Traces the path of traffic from source to destination to find the point of failure.
    *   **Substitution**: Replaces a suspected faulty component with a known good one.
    *   **Comparison**: Compares configurations or performance between working and non-working elements.

---

#### **11.3 Troubleshooting Tools**

*   **Software Tools**:
    *   **Network Management System (NMS)**: Provides centralized monitoring, configuration, and fault management.
    *   **Knowledge Bases**: Vendor documentation and online resources are invaluable.
    *   **Baselining Tools**: Automate the process of collecting performance data.
    *   **Protocol Analyzers (e.g., Wireshark)**: Capture and decode network traffic to inspect packets at every layer.

*   **Hardware Tools**:
    *   **Digital Multimeters and Cable Testers**: Check for physical layer issues like cable faults, power problems, and incorrect pinouts.
    *   **Cisco Prime Network Analysis Module (NAM)**: A tool for in-depth performance analysis in switched and routed environments.

*   **Syslog Server**: A centralized server that collects and stores log messages from network devices, allowing for easier analysis and correlation of events. Cisco IOS uses 8 severity levels (0-7), where 0 is the most severe (Emergencies).

---

#### **11.4 Symptoms and Causes of Network Problems**

This section breaks down common problems by OSI layer.

*   **Physical Layer**:
    *   **Symptoms**: Loss of connectivity, poor performance, high CPU utilization, console errors.
    *   **Causes**: Power issues, hardware faults, cabling errors, attenuation (signal loss), noise (EMI), interface misconfigurations.
*   **Data Link Layer**:
    *   **Symptoms**: No Layer 3 connectivity, excessive broadcasts, "line protocol down" messages.
    *   **Causes**: Encapsulation errors, MAC address mapping issues, framing errors (duplex mismatch), and Spanning Tree Protocol (STP) failures or loops.
*   **Network Layer**:
    *   **Symptoms**: Complete network failure or suboptimal performance affecting a subset of users.
    *   **Causes**: Routing table errors (missing routes), neighbor adjacency problems, or issues with the routing protocol's topology database.
*   **Transport Layer**:
    *   **Causes**: Incorrectly configured Access Control Lists (ACLs) blocking traffic or Network Address Translation (NAT) interoperability issues with certain protocols (like DHCP or DNS).
*   **Application Layer**: Problems with specific services like HTTP, DNS, or email, often related to configuration on the end device or server.

---

#### **11.5 Troubleshooting IP Connectivity**

A step-by-step, bottom-up approach to resolving end-to-end connectivity issues.

1.  **Verify the Physical Layer**: Use `show interfaces` to check if the interface is "up, line protocol is up" and look for input/output errors.
2.  **Check for Duplex Mismatches**: Ensure both sides of a link are configured for the same duplex setting (auto is preferred). Mismatches can cause severe performance degradation.
3.  **Verify Addressing on the Local Network**: Check the ARP cache (`arp -a`) on hosts and the MAC address table (`show mac address-table`) on switches to ensure correct Layer 2 and 3 mappings and VLAN assignments.
4.  **Verify Default Gateway**: Ensure clients have the correct default gateway configured. Use `show ip route` on routers and `ipconfig` or `route print` on PCs.
5.  **Verify Correct Path**: Use `traceroute` to see the path traffic is taking and `show ip route` to analyze the routing table to ensure the best path (longest prefix match) is being used.
6.  **Verify the Transport Layer**: Use `telnet` to a specific port to test connectivity for a service (e.g., `telnet <server_ip> 80`).
7.  **Verify ACLs**: Use `show ip interface` to see if any ACLs are applied that might be blocking traffic.
8.  **Verify DNS**: Use `nslookup` to confirm that domain names are resolving to the correct IP addresses.

---
