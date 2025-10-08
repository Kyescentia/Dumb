---

### **Chapter 3: DHCPv4**

This chapter covers the operation and configuration of DHCP for IPv4.

#### **3.1 DHCPv4 Concepts**

*   **Purpose**: DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, default gateways, and DNS servers to clients.
*   **Lease Process (DORA)**: A four-step process for a client to obtain an IP address.
    1.  **Discover**: Client broadcasts a DHCPDISCOVER message to find servers.
    2.  **Offer**: DHCP server(s) unicast a DHCPOFFER with lease details.
    3.  **Request**: Client broadcasts a DHCPREQUEST to accept an offer.
    4.  **Acknowledge**: The selected server unicasts a DHCPACK to confirm the lease.
*   **Lease Renewal**: Before a lease expires, the client sends a unicast DHCPREQUEST to the original server to renew it. The server responds with a DHCPACK.

#### **3.2 Configure a Cisco IOS DHCPv4 Server**

*   **Configuration Steps**:
    1.  **Exclude Addresses**: `ip dhcp excluded-address <start-ip> [end-ip]` to reserve addresses for static assignment.
    2.  **Create Pool**: `ip dhcp pool <pool-name>` to create a new address pool.
    3.  **Configure Pool Options**:
        *   `network <network-id> <subnet-mask>`: Defines the pool of available addresses.
        *   `default-router <ip-address>`: Sets the default gateway for clients.
        *   `dns-server <ip-address>`: Sets the DNS server for clients.
*   **Verification**:
    *   `show running-config | section dhcp`: View DHCP configuration.
    *   `show ip dhcp binding`: See active leases.
    *   `show ip dhcp server statistics`: View message counts.
*   **DHCP Relay**:
    *   If clients are on a different subnet from the DHCP server, a router must be configured as a relay agent.
    *   The command `ip helper-address <dhcp-server-ip>` is applied to the interface that receives client broadcasts. The router then forwards these requests as unicasts to the specified server.

#### **3.3 Configure a DHCPv4 Client**

*   A Cisco router can be configured as a DHCP client, typically for a WAN interface connecting to an ISP.
*   The command `ip address dhcp` is used on the interface to enable it to receive its IP address automatically.

---
