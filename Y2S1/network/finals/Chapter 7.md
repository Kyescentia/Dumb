### **Chapter 7: Simple Network Management Protocol (SNMP)**

This chapter details how SNMP is used for network monitoring and management.

#### **7.1-7.2 SNMP Introduction and Operation**

*   **SNMP Architecture**: Consists of four main components:
    1.  **Network Management System (NMS)**: A central application that monitors and manages network devices.
    2.  **Managed Device**: A network device (e.g., router, switch) that is monitored by the NMS.
    3.  **Agent**: Software running on a managed device that collects information and sends it to the NMS.
    4.  **Management Information Base (MIB)**: A hierarchical database on the agent that stores variables and statistics about the device. Each variable is identified by an Object Identifier (OID).

*   **SNMP Communication**:
    *   The NMS **polls** the agent using `get` requests on **UDP port 161**.
    *   The agent can send unsolicited alerts, called **traps**, to the NMS on **UDP port 162** to report significant events (e.g., an interface failure).

*   **SNMP Operations**:
    *   `get-request`: NMS requests a specific value from the MIB.
    *   `set-request`: NMS changes a value in the MIB to configure the device.
    *   `trap`: Agent sends an alert to the NMS.

#### **7.3 SNMP Versions**

*   **SNMPv1**: The original version. Simple but insecure, as it uses plaintext community strings for authentication.
*   **SNMPv2c**: An enhanced version with bulk-retrieval capabilities, but still uses insecure community strings ("c" stands for community).
*   **SNMPv3**: The most secure version. It provides:
    *   **Authentication**: Verifies the source of the message.
    *   **Encryption**: Encrypts the message content.
    *   **Integrity**: Ensures the message has not been tampered with.

*   **Community Strings**: In v1 and v2c, these act as passwords.
    *   **Read-only (ro)**: Allows the NMS to read MIB data.
    *   **Read-write (rw)**: Allows the NMS to read and modify MIB data.

#### **7.4 MIB Object ID (OID)**

*   The MIB is a tree-like structure, and an OID is the unique path to a specific variable in that tree. For example, Cisco's private MIB branch begins with the OID `1.3.6.1.4.1.9`.
*   The **Cisco SNMP Object Navigator** is an online tool for looking up the meaning of specific OIDs.

---
