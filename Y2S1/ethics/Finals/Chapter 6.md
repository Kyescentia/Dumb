---
### Chapter 6: Risk Assessment and Trustworthy Computing

#### **Learning Objectives**
1.  Explain the purpose and steps of security risk assessment.
2.  Provide the core principles of trustworthy computing: security, privacy, reliability, and business integrity.
3.  Compare and contrast the core principles of the CIA Triad—Confidentiality, Integrity, and Availability.
4.  Discuss the importance of an IT Security Policy.
5.  Describe the role of the International Organization for Standardization (ISO) and the scope of ISO 27001.
6.  Describe the role of the National Institute of Standards and Technology (NIST) and the scope of the NIST Cybersecurity Framework (NCF).

#### **Chapter Outline**
1.  General Security Risk Assessment
2.  Trustworthy Computing
3.  CIA Triad
4.  IT Security Policy
5.  International Organization for Standardization (ISO)
6.  National Institute of Standards and Technology (NIST)

#### **1. General Security Risk Assessment**
*   A **risk assessment** is a method for determining the security risks an organization's systems and networks face from internal and external threats.
*   The goal of risk management is to determine how to best use time and capital to defend against the most significant threats.
*   An **asset** is any hardware, software, computer system, network, or database used to achieve business goals.
*   A **failure case** is any event with a detrimental effect on an asset, such as a virus infection or a DDoS attack.

*   **Steps in a General Security Risk Evaluation Process:**
    1.  **Identify Assets:** Identify the IT properties the company is most worried about, prioritizing those key to business objectives.
    2.  **Specify Loss Events:** Identify potential loss cases, risks, and threats (e.g., DDoS attack, insider theft).
    3.  **Frequency of Events:** Estimate the probability of each threat.
    4.  **Impact of Events:** Determine the severity of each hazard.
        *   **Risk Tolerance Level = Probability x Impact**
    5.  **Options to Mitigate:** Decide if each hazard can be mitigated to be less likely or have a smaller impact. Organizations often focus on risks with high frequency and high impact.
    6.  **Feasibility of Options:** Evaluate the viability of putting mitigation options into action.
    7.  **Cost/Benefit Analysis:** Conduct a study to ensure the activities are profitable and that the cost of control does not outweigh the system's benefits.
    8.  **Decision:** Determine whether to implement a particular countermeasure. If not, consider if the threat is serious enough to warrant a less costly option.

*   **Examples of Risk Analysis:**
    *   **Scenario 1:** A database with publicly available information has low security controls.
        *   **Probability of data breach:** High.
        *   **Impact of data breach:** Non-critical.
        *   **Decision:** Accept the risk with current security controls.
    *   **Scenario 2:** A database with sensitive customer information has very high security controls.
        *   **Probability of data breach:** Low.
        *   **Impact of data breach:** Critical (reputational damage, legal lawsuits, financial losses).
        *   **Decision:** Prioritize the risk and take all necessary actions to prevent it.

#### **2. Trustworthy Computing**
*   **Trustworthy computing** is an approach that provides stable, confidential, and consistent computing interactions based on sound market practices. It is a top priority for the computer industry.
*   Microsoft, for example, has committed to a trustworthy programming campaign.
*   The four pillars of Trustworthy Computing are:
    1.  **Security:** The system is resilient to attack, and the confidentiality, integrity, and availability of the system and its data are protected.
    2.  **Privacy:** People can control their personal information, and organizations that use it protect it faithfully.
    3.  **Reliability:** The computer system is dependable, available when needed, and performs as expected.
    4.  **Business Integrity:** Companies are responsible to customers, help them find appropriate solutions, address problems with products or services, and are open in their interactions.

#### **3. CIA Triad**
*   **Confidentiality:** Only approved individuals can access sensitive information. This can be achieved through tools like encryption and physical security (e.g., door locks).
*   **Integrity:** Ensures that information is correct and has not been altered by an unauthorized person or malicious software. For example, preventing an attacker from changing the price of an online purchase.
*   **Availability:** Designated users have constant access to assets. Data is accessible to authorized users when needed.

#### **4. IT Security Policy**
*   An **IT Security Policy** is a written document stating how an organization plans to protect its IT assets.
*   **Examples of IT Security Policies:**
    *   **Acceptable Use Policy (AUP):** Provides users with clear direction on the permissible uses of information resources.
    *   **Information Security Policy:** Provides high-level guidance for the security program.
    *   **Incident Response Policy:** Describes how the organization will respond to security incidents.
    *   **Business Continuity and Disaster Recovery Policy:** Outlines procedures to ensure essential business functions continue during and after a disaster.
    *   **Software Development Life Cycle (SDLC) Policy:** Establishes standards for maintaining software, ensuring security is integrated at every stage.
    *   **Change Management and Change Control Policy:** Describes how the organization will review, approve, and implement changes to information systems.

#### **5. International Organization for Standardization (ISO)**
*   The **ISO** has created a wide array of cybersecurity standards.
*   **ISO 27001** is a standard that provides requirements for an **information security management system (ISMS)**. An ISMS is a systematic approach to managing sensitive assets (people, processes, and IT systems) to keep them secure.
*   **ISO 27001 includes control objectives covering 14 categories:**
    *   Information Security Policies
    *   Organization of information security
    *   Human resource security
    *   Asset Management
    *   Access Control
    *   Cryptography
    *   Physical and environmental security
    *   Operation Security
    *   Communications Security
    *   System acquisition, development and maintenance
    *   Supplier relationships
    *   Information security incident management
    *   Information security aspects of business continuity management
    *   Compliance with internal and external requirements (e.g., laws).

#### **6. National Institute of Standards and Technology (NIST)**
*   **NIST** is a U.S. Commerce Department agency that promotes U.S. innovation and industrial competitiveness.
*   NIST created the **NIST Cybersecurity Framework (CSF)**, a set of guidelines for private companies to identify, detect, and respond to cyberattacks. The latest version is **NIST CSF 2.0**.
*   The NIST CSF is divided into three basic parts:
    1.  **CSF Core:** Defines the activities needed to achieve cybersecurity outcomes. It consists of Functions, Categories, and Subcategories. The six functions are: Govern, Identify, Protect, Detect, Respond, and Recover.
    2.  **CSF Organizational Profiles:** Relate to the current status of an organization's cybersecurity measures and provide a "road map" toward compliance.
        *   A **Current Profile** specifies the outcomes an organization is currently achieving.
        *   A **Target Profile** specifies the desired outcomes for achieving cybersecurity risk management objectives.
        *   Steps for creating a profile include scoping, gathering information, creating the profile, analyzing gaps, and implementing an action plan.
    3.  **CSF Tiers:** Four tiers help organizations identify their level of compliance. The higher the tier, the more compliant the organization.
        *   **Tier 1:** Partial
        *   **Tier 2:** Risk-Informed
        *   **Tier 3:** Repeatable
        *   **Tier 4:** Adaptive

