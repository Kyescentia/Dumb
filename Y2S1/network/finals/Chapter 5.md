---

### **Chapter 5: WLAN Configuration**

This chapter details the configuration of Wireless Local Area Networks (WLANs) on both small home routers and enterprise-level Wireless LAN Controllers (WLCs).

#### **5.1 Remote Site WLAN Configuration (SOHO Router)**

*   **Basic Setup**: Small office/home office (SOHO) routers are configured via a web GUI.
    *   **Initial Steps**: Log in, change the default admin password, and configure basic IP settings.
    *   **Wireless Settings**: Configure the SSID, security mode (WPA2 Personal is standard), passphrase, and channel.
*   **Key Features**:
    *   **NAT**: Translates private LAN IPs to a single public IP.
    *   **QoS**: Prioritizes traffic like voice and video.
    *   **Port Forwarding**: Opens specific ports to allow external access to internal services.

#### **5.2-5.3 Configure a WLAN on a WLC**

*   **WLC Architecture**: A WLC is a centralized device that manages multiple Lightweight Access Points (LAPs).
*   **WLC Interfaces**:
    *   **Management Interface**: Used for in-band management of the WLC.
    *   **Virtual Interface**: A non-configurable IP address used in mobility management.
    *   **Dynamic Interfaces (VLAN Interfaces)**: User-created interfaces that map WLAN SSIDs to specific VLANs.
*   **Configuring a Basic WLAN (WPA2 Personal)**:
    1.  Navigate to the WLANs menu and create a new WLAN.
    2.  Define the Profile Name and SSID.
    3.  Enable the WLAN.
    4.  Under the Security tab, select WPA2 Policy and enter a Pre-Shared Key (PSK).
    5.  Assign the WLAN to an interface (e.g., the management interface).
*   **Configuring a WPA2 Enterprise WLAN**:
    1.  **Configure Servers**:
        *   Add a RADIUS server for authentication under the Security > RADIUS menu. This requires the server's IP and a shared secret.
        *   Optionally, configure an SNMP server for monitoring under the Management menu.
    2.  **Create a New Interface**: Create a new dynamic interface and map it to the appropriate VLAN ID. Configure its IP address, gateway, and DHCP server.
    3.  **Create the WLAN**: Create a new WLAN and assign it to the new interface.
    4.  **Configure Security**: On the Security tab, the default is 802.1X. On the AAA Servers tab, select the configured RADIUS server.

#### **5.4 Troubleshoot WLAN Issues**

*   **Client Not Connecting**:
    *   Verify client IP configuration (`ipconfig`).
    *   Check for physical connectivity.
    *   Ensure security settings (passphrase, encryption type) match the AP.
    *   Check for interference or being out of the coverage area.
*   **Slow Network**:
    *   Upgrade clients to a newer 802.11 standard.
    *   Split traffic between the 2.4 GHz and 5 GHz bands by using different SSIDs. The 5 GHz band is faster and less crowded.
*   **Updating Firmware**: Periodically update the firmware on routers and APs to get the latest features and security patches. On a WLC, firmware can be pushed to all managed APs simultaneously.
