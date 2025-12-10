# Chapter 1(a): Introduction to Software Paradigm (Part 1)

### Introduction
* **Purpose:** Software is built to solve problems.
* **Key Aspects:** Creating software involves two main aspects: Architecture and the selection of a programming language.
* **Software Development Life Cycle (SDLC):**
    * It is an effective and efficient process used by development teams to design and build high-quality software.
    * **Goal:** To minimize project risks through careful planning and ensure software meets customer expectations.
    * It outlines a series of steps breaking the process into manageable, measurable tasks.
    * **Phases:** Planning, Analysis, Design, Implementation, Maintenance.

### Defining Paradigm
* **Origin:** The term comes from the Greek word "paradeigma," meaning pattern, example, or sample.
* **Software Paradigm:** A set of principles and practices or a theoretical framework guiding the development and structure of software systems.
* **Aspects of a Paradigm:**
    1.  **Disciplinary Matrix:** Ideas/methods consisting of symbolic generalizations, model beliefs, and values.
    2.  **Exemplars:** Examples shared that demonstrate the paradigm's characteristics.

### Types of Paradigms
1.  **Software Development Paradigm (Software Engineering):** Applies engineering concepts (requirement gathering, design, programming) to software development (e.g., Object-oriented, procedural).
2.  **Software Design Paradigm:** Describes a design solution or an approach to design problem solving.
3.  **Programming Paradigm:** Diverse methods for organizing programming languages and applications (e.g., imperative, declarative, functional, OOP).

### Influential Paradigms
* **The Algorithmic Paradigm (AP):** Based on the notion that problems are well-structured and involve executing a domain-specific algorithm. Algorithms function as problem-solving systems relying on inherent knowledge.
* **The Analysis-Synthesis-Evaluation Paradigm (ASE):**
    * Involves Requirement Analysis $\rightarrow$ Synthesis (driven by decomposition) $\rightarrow$ Evaluation.
    * **Critique:** Often too rigid for software development as decomposition can lead to unbounded problems due to component interactions.
* **The Formal Design Paradigm (FD):**
    * Uses abstraction and refinement as an alternative to decomposition.
    * Based on mathematical tools because programs are mathematical expressions describing functionality.
* **The Artificial Intelligence Paradigm (AI):**
    * Applicable for non-well-structured problems where the system possesses domain-specific knowledge.
    * Design process involves a problem space (initial state, goal state) and transitions via operators (searching).
* **The Theory of Evolutionary Design Paradigm (TED):**
    * Views software design as an evolutionary "empirical scientific" activity rather than a mathematical modeling activity.
    * Recognizes that designers often settle for adequate designs rather than ideal ones due to implementation limitations.

***

# Chapter 1(b): Introduction to Software Paradigm (Part 2)

### Problem Paradigm
* **Definition:** A model for classifying problems that share a common set of characteristics.
* **Common Challenges:** Applications consistently face challenges related to searching, enumerating, classifying, manipulating, and organizing data.
* **Hierarchy:**
    1.  **Fundamental Operations:** Lowest level of computation (e.g., assigning values, decision making).
    2.  **Algorithmic Structures:** Ordered sets of unambiguous steps defining a terminating process.
    3.  **Problem Classes:** Sets of problems similar in nature regardless of origin (e.g., checking a book in a library vs. a module in a system library).

### Software Paradigms & Problem Classification
* **Imperative (Procedural):** Focuses on describing *how* a program operates through a sequence of steps. Used for calculations and data processing.
* **Object-Oriented (OOP):** Focuses on objects encapsulating data and behavior. Used for modeling real-world entities and simulations.
* **Declarative:** Focuses on *what* should be done rather than *how*. Used for SQL queries and logic-based problems.
* **Functional:** Emphasizes pure functions and immutability. Used for mathematical modeling and data processing pipelines.
* **Event-Driven:** Reacts to external inputs or triggers. Used for GUI applications and real-time monitoring.
* **Concurrent/Parallel:** Executes tasks simultaneously. Used for distributed systems and multi-core applications.
* **Component-Based:** Creates software from reusable components. Used for microservices.
* **Aspect-Oriented:** Separates cross-cutting concerns (logging, security).
* **Reactive:** Reacts to asynchronous data streams. Used for IoT and real-time web apps.
* **Artificial Intelligence:** Uses ML and reasoning for pattern recognition.
* **Search-Based:** Explores a search space for optimal solutions (e.g., traveling salesman problem).

### Principles
* **Importance:** Reduce defects, improve productivity, encourage collaboration, and mitigate risks.
* **Function-Oriented Principles:**
    * **Immutability:** Objects do not change state; new objects are created instead.
    * **First-class functions:** Functions can be treated as objects (passed as arguments, returned, stored).
    * **Pure Functions:** Results depend only on input parameters and do not change system state.
* **Object-Oriented Principles:**
    * **Encapsulation:** Hiding internal details.
    * **Inheritance:** Extending characteristics of ancestor objects.
    * **Polymorphism:** Objects taking on various forms.
* **SOLID Principles:**
    * **S:** Single Responsibility Principle.
    * **O:** Open/Closed Principle.
    * **L:** Liskov Substitution Principle.
    * **I:** Interface Segregation Principle.
    * **D:** Dependency Inversion Principle.
* **Other Principles:**
    * **Modularity:** Breaking down systems into smaller, manageable parts.
    * **Abstraction:** Hiding details to reduce complexity.
    * **YAGNI:** "You Ain't Gonna Need It" – avoid implementing features not immediately necessary.

***
