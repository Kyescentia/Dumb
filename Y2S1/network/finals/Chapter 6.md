---

### **Chapter 6: Network Time Protocol (NTP)**

This chapter explains the importance of time synchronization on a network and how to configure NTP.

#### **6.1-6.2 Time Service and NTP Operations**

*   **Importance**: Synchronized time across all network devices is critical for accurate timestamping of log files, which is essential for troubleshooting and security event correlation.
*   **NTP Overview**: NTP is a protocol that allows devices to synchronize their clocks with a central time source. It operates on UDP port 123.
*   **NTP Hierarchy (Stratum)**: NTP uses a hierarchical system to define the accuracy of a time source.
    *   **Stratum 0**: Authoritative, high-precision time sources like GPS clocks or atomic clocks.
    *   **Stratum 1**: Servers directly connected to Stratum 0 devices. They are considered the most accurate time servers on the network.
    *   **Stratum 2**: Servers that receive their time from Stratum 1 servers.
    *   **Stratum 3 and lower**: Continue the hierarchy, with each level adding a small amount of delay.
    *   **Stratum 16**: Indicates a device is unsynchronized.
*   **NTP Roles**:
    *   **Server**: Provides time to clients.
    *   **Client**: Receives time from a server.
    *   **Client/Server**: Receives time from a higher-stratum server and provides it to lower-stratum clients.

#### **6.3 Configure and Verify NTP**

*   **Configuration**:
    *   The command `ntp server <ip-address>` is used in global configuration mode to point a device to an NTP server.
*   **Verification**:
    *   `show clock detail`: Shows the current time and whether the time source is "user configuration" (manual) or "NTP".
    *   `show ntp status`: Displays if the clock is synchronized, the device's own stratum level, and the IP address of the reference server.
    *   `show ntp associations`: Provides detailed information about the connection to the NTP server, including its stratum, delay, and offset.

---
