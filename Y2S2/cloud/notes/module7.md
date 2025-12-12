# **Module 7: Storage**

#### **Section 1: Amazon Elastic Block Store (Amazon EBS)**
* **Type:** Block-level storage.
* **Use Case:** Boot volumes, database hosts, enterprise applications.
* **Features:** Persists independently of the instance, replicated within AZ, scalable.
* **Volume Types:**
    * **SSD:** General Purpose (gp2/3), Provisioned IOPS (io1/2) for performance.
    * **HDD:** Throughput Optimized (st1) for streaming, Cold (sc1) for infrequent access.
* **Snapshots:** Point-in-time backups stored in S3.

#### **Section 2: Amazon Simple Storage Service (Amazon S3)**
* **Type:** Object-level storage.
* **Structure:** Data stored as objects within buckets.
* **Durability:** Designed for 11 9s (99.999999999%) durability.
* **Storage Classes:**
    * **Standard:** Frequently accessed data.
    * **Intelligent-Tiering:** Automatically moves data between tiers.
    * **Standard-IA / One Zone-IA:** Infrequent access, lower cost.
    * **Glacier / Deep Archive:** Long-term archive.
* **Permissions:** Controlled via Bucket Policies and ACLs.

#### **Section 3: Amazon Elastic File System (Amazon EFS)**
* **Type:** Network file storage (NFS).
* **Features:** Scalable, elastic, shared access across multiple EC2 instances.
* **Use Case:** Big data, content management, home directories.

#### **Section 4: Amazon S3 Glacier**
* **Purpose:** Data archiving and long-term backup.
* **Retrieval Options:**
    * **Expedited:** 1-5 minutes.
    * **Standard:** 3-5 hours.
    * **Bulk:** 5-12 hours.
* **Security:** Vault Lock policies for compliance (WORM).

---
