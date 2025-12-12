# **Module 6: Compute**

#### **Section 1: Compute Services Overview**
* **Categories:**
    * **Virtual Machines (IaaS):** Amazon EC2.
    * **Serverless:** AWS Lambda.
    * **Container-based:** Amazon ECS, EKS, Fargate.
    * **Platform (PaaS):** AWS Elastic Beanstalk.

#### **Section 2: Amazon EC2**
* **Definition:** Provides resizable virtual computing capacity in the cloud.
* **Instance Types:**
    * **General Purpose:** Balanced resources.
    * **Compute Optimized:** High performance processors.
    * **Memory Optimized:** Large datasets in memory.
    * **Storage Optimized:** High, sequential read/write access.
    * **Accelerated Computing:** Graphics/GPU workloads.
* **Pricing Models:**
    * **On-Demand:** No commitment, pay by hour/second.
    * **Reserved Instances:** 1-3 year commitment, discount up to 75%.
    * **Spot Instances:** Spare capacity, up to 90% discount, can be interrupted.
    * **Dedicated Hosts:** Physical servers dedicated to user.
* **User Data:** Scripts run upon instance launch to bootstrap configuration.

#### **Section 3: Amazon EC2 Cost Optimization**
* **Four Pillars:**
    1.  **Right Size:** Match instance type/size to workload performance needs.
    2.  **Increase Elasticity:** Stop idle instances, use Auto Scaling.
    3.  **Optimal Pricing Model:** Mix On-Demand, Reserved, and Spot.
    4.  **Optimize Storage:** Resize volumes, delete unused snapshots.

#### **Section 4: Container Services**
* **Containers:** Method of OS virtualization; repeatable, self-contained environments.
* **Docker:** Platform to build, test, and deploy applications in containers.
* **Amazon ECS:** Orchestration service for Docker containers.
* **Amazon EKS:** Managed Kubernetes service.
* **AWS Fargate:** Serverless compute engine for containers (removes need to manage servers).
* **Amazon ECR:** Fully managed Docker container registry.

#### **Section 5: Introduction to AWS Lambda**
* **Definition:** Serverless compute service running code in response to events.
* **Benefits:** No server management, sub-second metering, scales automatically.
* **Triggers:** Events from S3, DynamoDB, API Gateway, etc.
* **Limits:** Max 15-minute runtime, 10GB memory.

#### **Section 6: Introduction to AWS Elastic Beanstalk**
* **Definition:** PaaS for deploying and scaling web applications.
* **Function:** Handles deployment, capacity provisioning, load balancing, and auto-scaling automatically.
* **Cost:** Free to use; pay only for underlying resources (e.g., EC2).

---
