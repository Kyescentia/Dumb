# **Module 4: AWS Cloud Security**

#### **Section 1: AWS Shared Responsibility Model**
* **AWS Responsibility (Security OF the Cloud):** Protects the physical infrastructure (regions, AZs, edge locations), hardware, software, and networking.
* **Customer Responsibility (Security IN the Cloud):** Manages customer data, IAM, operating system configuration (patching), network/firewall settings, and client-side/server-side encryption.
* **Service Types:**
    * **IaaS (e.g., EC2):** Customer manages more (OS, patches, firewalls).
    * **PaaS (e.g., RDS):** AWS manages OS and patching; Customer manages data.
    * **SaaS (e.g., Trusted Advisor):** Customer does not manage infrastructure at all.

#### **Section 2: AWS Identity and Access Management (IAM)**
* **Function:** Manage access to AWS resources securely.
* **Identities:**
    * **IAM User:** Person or application.
    * **IAM Group:** Collection of users with identical permissions.
    * **IAM Role:** Identity with specific permissions, not associated with one person, assumable by users, apps, or services for temporary access.
* **Policies:** JSON documents defining permissions (Effect, Action, Resource).
    * **Principle of Least Privilege:** Grant only necessary permissions.
* **Authentication:**
    * **Programmatic:** Access Key ID + Secret Access Key (CLI/SDK).
    * **Console:** Account ID + User Name + Password (+ MFA).

#### **Section 3: Securing a New AWS Account**
1.  **Stop using the root user:** It has unrestricted access. Create IAM users/groups instead.
2.  **Enable MFA:** Require multi-factor authentication for root and IAM users.
3.  **Use AWS CloudTrail:** Track user activity and API calls across the account.
4.  **Enable Billing Reports:** Monitor usage and costs (e.g., Cost and Usage Report).

#### **Section 4: Securing Accounts**
* **AWS Organizations:** Central management of multiple accounts using Service Control Policies (SCPs) to limit permissions across OUs.
* **AWS Key Management Service (KMS):** Create and manage encryption keys to control encryption across services.
* **Amazon Cognito:** Adds user sign-up/sign-in and access control to web/mobile apps (supports social/enterprise identity providers).
* **AWS Shield:** Managed DDoS protection service.

#### **Section 5: Securing Data on AWS**
* **Data at Rest:** Encrypt data stored on disk (EBS, S3, RDS) using keys managed by KMS.
* **Data in Transit:** Encrypt data moving across networks using TLS/SSL (HTTPS endpoints).
* **S3 Security:** Use Block Public Access, bucket policies, and ACLs to secure objects.

#### **Section 6: Working to Ensure Compliance**
* **Compliance Programs:** AWS provides certifications (ISO, PCI), legal support (GDPR, HIPAA), and alignments (CIS).
* **AWS Config:** Continuous monitoring and auditing of resource configurations against desired states.
* **AWS Artifact:** Portal for on-demand access to AWS compliance reports and agreements.


    * **Standard:** 3-5 hours.
    * **Bulk:** 5-12 hours.
* **Security:** Vault Lock policies for compliance (WORM).
