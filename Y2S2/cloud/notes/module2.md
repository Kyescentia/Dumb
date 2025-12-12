# **Module 2: Cloud Economics and Billing**

#### **Section 1: Fundamentals of Pricing**
* **Three Drivers of Cost:**
    1.  **Compute:** Charged per hour or second (Linux only).
    2.  **Storage:** Charged typically per GB.
    3.  **Data Transfer:** Outbound is charged; inbound is typically free.
* **Pricing Philosophy:** Pay for what you use, pay less when reserving, and pay less with volume discounts as AWS grows.
* **Free Tier:** Offers free hands-on experience for new customers for 1 year (e.g., some EC2, S3, RDS usage).
* **Services with No Charge:** VPC, Elastic Beanstalk, Auto Scaling, CloudFormation, IAM (though underlying resources they provision may incur costs).

#### **Section 2: Total Cost of Ownership (TCO)**
* **Definition:** Financial estimate to help identify direct and indirect costs of a system.
* **Use Case:** Budgeting and building business cases for migration (on-premises vs. cloud).
* **Cost Considerations:** Includes server, storage, network, and IT labor costs (power, cooling, space, administration).
* **Calculator:** The **AWS Pricing Calculator** estimates monthly costs, models solutions, and allows exploring price points.

#### **Section 3: AWS Organizations**
* **Function:** Consolidate and centrally manage multiple AWS accounts.
* **Features:**
    * Group accounts into Organizational Units (OUs).
    * **Consolidated Billing:** Combine usage across accounts to share volume pricing discounts.
    * **Service Control Policies (SCPs):** Allow or deny access to AWS services for individual or group accounts.

#### **Section 4: AWS Billing and Cost Management**
* **AWS Billing Dashboard:** View monthly-to-date spend, forecast, and spend by service.
* **Tools:**
    * **AWS Budgets:** Set custom budgets and receive alerts when costs or usage exceed limits.
    * **AWS Cost Explorer:** Visualize usage trends and cost drivers over time (last 13 months).
    * **AWS Cost and Usage Report:** Granular details of usage and costs, delivered to an S3 bucket.

#### **Section 5: Technical Support**
* **Support Plans:**
    * **Basic:** Free; access to Resource Center, Service Health Dashboard, FAQs.
    * **Developer:** For experimenting and early development; business hour access via email.
    * **Business:** For production workloads; 24/7 access via phone, chat, email; <1 hour response for urgent issues.
    * **Enterprise:** For mission-critical workloads; includes a Technical Account Manager (TAM) and Support Concierge; <15 min response for critical issues.
* **AWS Trusted Advisor:** Provides real-time guidance on best practices (cost, security, fault tolerance, performance).

---
