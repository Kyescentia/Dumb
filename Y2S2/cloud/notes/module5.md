# **Module 5: Networking and Content Delivery**

#### **Section 1: Networking Basics**
* **IP Addresses:** Numeric labels (IPv4 is 32-bit, IPv6 is 128-bit).
* **CIDR (Classless Inter-Domain Routing):** Method for allocating IP addresses (e.g., 192.0.2.0/24). The suffix (/24) indicates fixed bits.
* **OSI Model:** 7 layers including Physical, Network (IP), Transport (TCP/UDP), and Application (HTTP).

#### **Section 2: Amazon VPC (Virtual Private Cloud)**
* **Definition:** Logically isolated section of the AWS Cloud to launch resources in a virtual network.
* **Components:**
    * **Subnets:** Segments of a VPC's IP range residing in a specific Availability Zone. Can be Public or Private.
    * **Route Tables:** Rules directing traffic from subnets.
    * **Internet Gateway (IGW):** Enables communication between the VPC and the internet.
    * **NAT Gateway:** Allows private subnet instances to access the internet but prevents the internet from initiating connections.
* **Security Layers:**
    * **Security Groups:** Stateful firewalls at the instance level (allow rules only).
    * **Network ACLs:** Stateless firewalls at the subnet level (allow and deny rules).

#### **Section 3: VPC Networking**
* **VPC Peering:** Connects two VPCs to route traffic privately.
* **AWS Site-to-Site VPN:** Connects VPC to on-premises network via encrypted tunnel over the internet.
* **AWS Direct Connect:** Dedicated physical connection from on-premises to AWS (bypasses internet).
* **VPC Endpoints:** Private connection to supported AWS services (like S3) without using public IPs.
* **AWS Transit Gateway:** Hub to connect VPCs and on-premises networks centrally.

#### **Section 5: Amazon Route 53**
* **Definition:** Highly available and scalable DNS web service.
* **Functions:** Domain registration, DNS routing, and health checking.
* **Routing Policies:** Simple, Weighted, Latency, Geolocation, Geoproximity, Failover, Multivalue answer.

#### **Section 6: Amazon CloudFront**
* **Definition:** Fast, global Content Delivery Network (CDN) service.
* **Function:** Caches static and dynamic content at Edge Locations to lower latency for users.
* **Pricing:** Charged for data transfer out and HTTP/S requests.

---

