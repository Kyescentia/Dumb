---

### **Chapter 8: Syslog**

This chapter focuses on the Syslog protocol for network device logging.

#### **8.1-8.3 Syslog Operation and Message Format**

*   **Purpose**: Syslog is a standard protocol for sending event notification messages to a logging server. It uses UDP port 514.
*   **Message Destinations**: Messages can be sent to:
    *   Internal logging buffer (RAM).
    *   Console line.
    *   VTY lines (Telnet/SSH sessions).
    *   An external syslog server.
*   **Message Format**: `%FACILITY-SEVERITY-MNEMONIC: description`
    *   **Facility**: The part of the system that generated the message (e.g., LINK, SYS).
    *   **Severity**: A number from 0 (Emergency) to 7 (Debugging) indicating the message's importance.
    *   **Mnemonic**: A short code describing the message.

#### **8.4-8.6 Configuration and File Maintenance**

*   **Timestamps**: By default, logs are not timestamped. Use the `service timestamps log datetime` command to add the date and time to messages, which is vital for troubleshooting.
*   **File Systems**: Cisco IOS has a file system (IFS) for managing files on flash, NVRAM, and other storage. Key commands include `dir`, `cd`, `pwd`, and `show file systems`.
*   **Backing Up and Restoring Configurations**:
    *   Configurations can be backed up to a text file, a TFTP server (`copy running-config tftp`), or a USB drive (`copy running-config usbflash0:`).
*   **Password Recovery**: A procedure to bypass a lost password by booting into ROMMON mode, changing the configuration register to `0x2142` to bypass the startup config, copying the startup config to the running config, resetting the password, and then restoring the configuration register to `0x2102`.
*   **IOS Image Management**:
    *   Cisco IOS images can be backed up to and restored from a TFTP server using the `copy flash: tftp:` and `copy tftp: flash:` commands.
    *   The `boot system` command is used to specify which IOS image file the router should load on startup.

---
