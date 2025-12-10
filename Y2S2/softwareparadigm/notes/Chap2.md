
# Chapter 2: Software Process Model (Part A)

### Software Process
* **Definition:** A sequence of activities leading to the production of a software product.
* **Process Model:** A framework to plan and control the flow of work, comprising specific activities and tasks.
* **Core Activities:**
    1.  **Specification:** Defining functionality and constraints.
    2.  **Development:** Producing the software.
    3.  **Validation:** Ensuring software meets customer wants.
    4.  **Evolution:** Evolving to meet changing needs.

### SDLC Models
* **Waterfall Model:**
    * Linear-Sequential Life Cycle.
    * **Phases:** Requirements $\rightarrow$ Design $\rightarrow$ Implementation $\rightarrow$ Testing $\rightarrow$ Maintenance.
    * **Usage:** Embedded systems or large partner systems where hardware/software must interface.
    * **Pros/Cons:** Systematic but rigid; does not allow backtracking for corrections easily.
* **Prototyping Model:**
    * Helps validate requirements when users struggle to express them.
    * **Throw-away:** Built to understand requirements then discarded.
    * **Evolutionary:** Prototype evolves into the final system.
    * **Pros:** Saves time/money, early user engagement.
    * **Cons:** Management problems, potential for poor reliability in throw-aways.
* **Rapid Application Development (RAD):**
    * "High-speed" waterfall where the application is modularized and built by parallel teams.
    * **Usage:** When requirements are known, the project is modular, and manpower is sufficient.
* **Spiral Model:**
    * Risk-driven process model.
    * Adopts elements of multiple models based on risk patterns.
    * **Process:** Planning $\rightarrow$ Risk Analysis $\rightarrow$ Engineering $\rightarrow$ Evaluation (Repeated in loops).
* **Agile Software Development:**
    * Incremental development with rapid feedback.
    * **Main Elements:** Minimal documentation, Informal communication, Embracing Change.
    * **Extreme Programming (XP):** First agile methodology emphasizing simplicity, feedback, and courage. Includes practices like pair programming and continuous integration.

***

# Chapter 2: Software Process Model (Part C)

### Incremental Model
* **Concept:** Delivers core product functions in the first increment and supplementary features in subsequent increments.
* **Process:** Builds software through multiple iterations (Analysis $\rightarrow$ Design $\rightarrow$ Code $\rightarrow$ Test).
* **Advantages:** Early delivery of working system, useful when staff is unavailable, improves risk management.
* **Disadvantages:** Difficult to estimate time/cost accurately, requires comprehensive planning.

### Component-Based Software Engineering (CBSE)
* **Definition:** Approach based on software reuse ("Buy, don't build").
* **Shift:** Moves emphasis from *programming* to *composing* software systems.
* **Essentials:** Independent components, component standards, middleware, and a development process geared to reuse.
* **Component Model:** Definition of standards for implementation and deployment (e.g., EJB, COM+, CORBA).
* **Domain Engineering:** Identifying and constructing components for a specific domain.
* **Challenges:** Component trustworthiness (no source code), component certification, predicting emergent properties, and requirement trade-offs.
* **Failure Case:** The Ariane 5 rocket failed due to a reused component from Ariane 4.

***
