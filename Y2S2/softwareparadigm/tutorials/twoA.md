# 📓 Tutorial 2 (a) Notes

### 1) Define the following terms:

**a) Software Process**

* **Software:** A collection of computer programs, data, and instructions that tell a computer how to work.
* **Process:** A series of steps taken to produce an intended output.
    * Involve activities, constraints, resources, tools and techniques.
    * **Why important?**
        * Impose consistency and structure on set of activities.
        * Guide in understanding, controlling, examining and improving the activities.
* **Definition:** Software process is a **sequence of activities that leads to the production of a software product**.
* **Note:** When a process involved building a software, the process may be referred to as **Software development life cycle (SDLC)**.

**b) Software Process Model**

* A **framework** used to structure, plan, and control flow of work required to develop a software.
* A **simplified description** of how software is developed which is **presented from a particular perspective**.
* **It includes:**
    * **Activities:** Key tasks and phases.
    * **Software Products:** The outputs or deliverables of each activity.
    * **Roles:** The people or teams responsible for carrying out each activity.
* By representing the software development process from different perspectives, software process models help in organizing and managing the development process, making it easier for teams to understand their responsibilities, track progress, and optimize workflows.

---

### 2) Briefly describe the fundamental activities of software process.

**The 4 Fundamental Activities:**

1.  **Software Specification**
    * Where the functionality of the software and constraints on its operation must be defined.
    * Defines the functional and non-functional requirements of the software.
    * Activities include requirements gathering, analysis, and documentation.

2.  **Software Development**
    * Where the software to meet the specification must be produced.
    * Developers translate requirements into a working system using programming languages and tools.
    * Activities includes software design, coding, testing and bug fixing.

3.  **Software Validation**
    * Where the software must be validated to ensure that it does what the customer wants (meet the business requirement).
    * Activities include testing (unit, integration, system, and acceptance testing).

4.  **Software Evolution**
    * Where the software must evolve to meet changing customer needs.
    * The software must adapt to changing requirements, environments, and technologies.
    * Activities include bug fixes, updates, and new feature additions.

**Whiteboard Flowchart (Related to Activities):**
* Planning $\to$ Analysis $\to$ Design
* (Planning $\uparrow$ Software Specification)
* (Design $\uparrow$ Software Development)
* Design $\downarrow$ Implementation
* Implementation $\to$ Testing
* Implementation $\downarrow$ Maintenance
* Testing $\to$ Software Validation
* Maintenance $\to$ Software Evolution

---

### 3) Explain the reason why waterfall model is not suitable for all types of software.

* A traditional, **plan-driven** model.
* Development progresses sequentially through fixed phases (requirements $\to$ design $\to$ implementation $\to$ testing $\to$ deployment $\to$ maintenance).
* **Any phase begins only if the previous phase is completed**, no overlap.
* Suitable for project with well defined and fixed requirements, sufficient resources, an established timeline, well understood technology and unlikely to require significant changes.
* **Not allow to backtrack** and go back to stage one to make corrections.
* **Not flexible for new requirement or change**. When a flaw is found, the entire process often needs to start over.
* It is **more difficult and expensive to fix bugs** discovered at this point. Problems identified late in the process can lead to delays and require significant rework.
* **No working product is available** until the later stages of the project lifecycle.

---

### V Model (Extension of Waterfall)

* Emphasizes **testing and validation** at every stage. Testing is **planned in parallel** with development.
* Errors can be detected earlier because testing activities are defined during each development phase.
* Suitable for Projects where requirement is clear and quality assurance and early testing are critical (e.g., safety-critical systems).

**Diagram Breakdown:**
* **Verification Phase (Descending):**
    * Requirement Gathering (links to $\to$ Acceptance Testing)
    * System Analysis (links to $\to$ System Testing)
    * Software Design (links to $\to$ Integration Testing)
    * Module Design (links to $\to$ Unit Testing)
* **Bottom:** Coding
* **Validation Phase (Ascending):**
    * Unit Testing
    * Integration Testing
    * System Testing
    * Acceptance Testing

---

### 4) Explain the condition when prototyping model is recommended.

* An **agile driven model**; an iterative, trial and error process.
* **Prototype** = A **toy implementation** of system.
* Builds a prototype to understand requirements before actual development. **Feedback from users refines requirements**.
* Suitable for **project with unclear or evolving requirements**.
* **Early and continuous user involvement**.
* Can receive partial product early in the life cycle $\to$ increase satisfaction and comfort.
* When software **customers and end-users** find it very **difficult to express their real requirements.**
    * A **system prototype** helps give end-users a concrete impression of the system capabilities.
    * **Missing functionalities** can be easily figured out.
* When the **developers are new to the domain**.
    * **Errors can be detected much earlier** to enhance the quality of software.

**Prototype Model Flow:**
1.  **Prototype Development (Loop):**
    * Requirement gathering $\to$ Quick Decision
    * Splits to:
        * Refine requirement (Incorporation customer Suggestion)
        * Build Prototype
    * Both lead to $\to$ Customer evaluation of Prototype (which can loop back).
2.  **Iterative Development (Sequence):**
    * (After "Acceptance by customer")
    * Design $\to$ Implementation $\to$ Testing $\to$ Maintainance

---

### 5) Differentiate between throw-away prototyping model and evolutionary prototyping model.

| Type of Prototype | Description | Key Features | Example / Use Case |
| :--- | :--- | :--- | :--- |
| **Rapid (Throwaway)** | A **quick, rough model built to understand requirements** and get feedback. The prototype is **discarded**. | - Focuses on requirements gathering <br> - **Final product is completely new** <br> - Fast and inexpensive | Creating a simple mock-up to confirm design before coding. |
| **Evolutionary** | A **continuously refined prototype** that **evolves into the final system** through multiple iterations. | - The **prototype grows into the final system** <br> - Continuous improvement <br> - Suitable for unclear requirements | Developing an AI chatbot that improves over multiple iterations. |
| **Incremental** | The **final system is decimated into different small prototypes and developed individually**. Each part adds new features. | - Different prototypes are **merged into a single product** <br> - Each version is usable <br> - Easier testing and feedback | A banking app built in modules ("balance check", then "fund transfer", etc.). |
| **Extreme** | Used **mainly in web development**. Involves 3 phases: static mock-up, functional prototype, then backend integration. | - Common in web-based systems <br> - 3 stages (presentation $\to$ functional $\to$ integration) <br> - Focus on user experience | Developing an e-commerce site (static pages $\to$ interactive $\to$ database). |

---

### 6) Propose a model for a cheap and fast delivery.

* **Model:** **Rapid Application Development (RAD)**
* **Justification:**
    * Emphasizes **quick development** through **iterative prototyping, high user involvement, and reuse of existing components**.
    * This significantly **reduces both time and cost**.
    * **Continuous customer feedback** ensures the product meets expectations, reducing the **risk of costly rework**.
    * Since **RAD is iterative**, modifications can be **easily incorporated at any stage**.

---

### 7) Briefly describe agile methods.

* Incremental development methods in which the increments are small.
* Customers are involved in the development process to get rapid feedback.
* **Key characteristics:**
    * **Iterative and incremental:** Working software is delivered frequently.
    * **Emphasizes individuals and interactions:** Close, daily cooperation; face-to-face conversation; self-organizing teams.
    * **Adapts to changing requirements:** Welcome changing requirements, even late in development.

**Agile Cycle Diagram:** 1. Requirements $\to$ 2. Design $\to$ 3. Development $\to$ 4. Testing $\to$ 5. Deployment $\to$ 6. Review (and repeat).

---

### Types of Agile Methodology

| Methodology | Description | Key Features | Best Suited For |
| :--- | :--- | :--- | :--- |
| **Extreme Programming (XP)** | Focuses on improving software quality and responsiveness to change. | - **Communication:** Pair programming <br> - **Feedback:** Small, frequent releases <br> - **Continuous integration** <br> - **Test-driven development (TDD)** | Projects with **high code quality, tight deadlines, frequent changes**. |
| **Feature-Driven Development (FDD)** | Emphasizes designing and building software by **features**. | - **User centric approach** <br> - **Feature-based planning and tracking** <br> - **Regular, short iterations (2-10 days)** | **Large or complex projects** where progress is measured feature by feature. |
| **Scrum** | A lightweight, iterative framework that divides work into **sprints (2-4 weeks)**. | - **Iterative and incremental** <br> - **Roles:** Product Owner, Scrum Master, Team <br> - **Artifacts:** Product Backlog, Sprint Backlog <br> - **Meetings:** Sprint Planning, Daily Scrum, etc. | Projects with **changing or unclear requirements**, needing regular feedback. |
| **Rapid Application Development (RAD)** | Prioritizes **fast development** using **iterative prototyping** and user feedback. | - **Prototyping and iteration** <br> - **User involvement throughout** <br> - **Reusable components** <br> - **Short development cycles (2-3 months)** | Projects needing **quick delivery and constant user input**. Not for high-risk projects. |

**Agile Process Diagrams:**
* **Extreme Programming:** Test Scenarios/Requirements $\to$ Stories $\to$ Iteration $\to$ Release planning $\to$ Small releases $\to$ Release.
* **Scrum Process:** Product Backlog (from User Stories) $\to$ Sprint Planning Meeting $\to$ Sprint Backlog $\to$ Sprint (1-4 Weeks) $\to$ Finished Work. (Daily Stand Up occurs during Sprint).
* **RAD:** Requirements Planning $\to$ User Design (iterative) $\to$ Construction $\to$ Cutover.

---

### 8) Distinguish plan-based and agile software development process.

| Aspect | Predictive methodology (Plan-driven) | Adaptive methodology (Agile driven) |
| :--- | :--- | :--- |
| **Definition** | **Traditional, plan-driven** where **all requirements and schedule are known in advance**. | **Flexible, change-driven** that **adapts to evolving requirements and feedback**. |
| **Planning** | **Detailed planning done before development starts**. | **Planning is continuous**, plans evolve with each iteration. |
| **Requirements** | **Fixed at the start of the project**, changes discouraged. | **Evolving and can change based on user feedback**; not known in advance. |
| **Customer Involvement** | **Minimal** after initial requirements. | **Continuous** involvement throughout the project. |
| **Flexibility** | **Low** - changes are costly and time-consuming. | **High** - embraces change, even late in development. |
| **Risk Management** | Risks are analyzed and **mitigated early**. | Risks are **managed continuously** through rapid feedback. |
| **Documentation** | Emphasizes **comprehensive** documentation. | **Focuses on working software** over documentation. |
| **Best Suited For** | Projects with **stable, well-understood requirements**. | Projects with **uncertain or rapidly changing requirements**. |
| **Examples** | Waterfall Model, V-Model, Spiral (in predictive mode). | Prototyping model, Agile Model (XP, FDD, Scrum, RAD). |

**Additional Notes:**
* ***Incremental model -> can be predictive or semi adaptive methodology**
* **Plan-based:** Uses formal documents to communicate between stages. Involves significant overhead in planning, designing, and documenting.
* **Agile:** Involves iteration across activities; requirements and design are developed together. Allows team to focus on the software itself.

---

### 💡 Summary from Whiteboard

* **Prototyping:** Agile-driven, Unclear req, Flexible, Used to find req or new to the domain.
* **Spiral:** Risk Driven, Flexible, Iterative, Unclear Req.
* **Incremental:** Iterative, Features $\checkmark$, Well-defined Req.
* **V-Model:** Testing & Validation, Plan-driven.
* **Waterfall:** Step-by-Step, Plan-driven, Well defined req, $\times$ No back trace, $\times$ Flexibility.
* **Agile (General):** Fastest, Iterative, Communication, Agile-driven.
