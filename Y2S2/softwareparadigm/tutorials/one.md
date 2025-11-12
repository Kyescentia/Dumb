
📝 Tutorial 1(a)
2. Compare the three categories of software paradigm.
|  | Software Development Paradigm | Software Design Paradigm | Programming Paradigm |
|---|---|---|---|
| Hierarchy | Broadest category | (Middle) | Most granular level |
| Scope | Refers to Software Engineering. Includes all engineering concepts related to the software development lifecycle. | Can be used to describe a design solution or as an approach to design problem-solving. Guides the organization of code, components, and interfaces. | Represents diverse methods for organizing programming languages and applications. Deals with how code is written and structured. |
| Summary | How the entire software project is organized and managed. | How the system architecture or components are structured. | How individual code is written and organized logically. |
| Activities | Requirement gathering, system design, programming. | Design, maintenance, programming. | Coding, testing, integration. |
| Example | Object-oriented paradigm, Procedural paradigm. | MVC, Microservices. | Functional programming, Object-oriented programming, Imperative programming. |
 * Hierarchy Diagram: Software Development ➔ Software Design ➔ Programming
3. Draw a diagram to show the stages of SDLC.
The SDLC is a continuous cycle: Planning ➔ Analysis ➔ Design ➔ Implementation ➔ Maintenance ➔ (back to Planning)
 * 1) Planning: Plan for the software design, resources, timeline, and budget.
 * 2) Analysis: Gather and analyze business/technical requirements; create a specifications document.
 * 3) Design: Create the system's architecture and detailed design (a blueprint).
 * 4) Implementation: The actual coding and testing of the application.
 * 5) Maintenance: Ongoing support, updates, and monitoring to keep the software functional, secure, and efficient.
4. Why is a software paradigm important?
 * Provides a Framework for Problem-Solving: Offers a systematic approach to structure solutions.
 * Shapes Software Design and Structure: Provides specific principles and patterns for design.
 * Improves Development Efficiency: Simplifies the process by providing tested and proven methodologies.
 * Facilitates Communication and Collaboration: Creates a shared understanding for team members, stakeholders, and clients.
5. Explain the term Problem Paradigm.
 * A conceptual framework or approach to understand, model, and solve problems.
 * Refers to a model for classifying problems that share a common set of characteristics.
 * Defines how problems are perceived, structured, and addressed using specific methodologies, principles, and tools.
 * Diagram Flow: Fundamental Operations ➔ Algorithmic Structures ➔ Problem Classes
6. Compare Function Oriented with Object Oriented.
| Feature | Functional Oriented Paradigm | Object-Oriented Paradigm |
|---|---|---|
| Main Focus | Breaking down problems into smaller, reusable functions or procedures. | Modeling real-world entities using objects (data + behavior). |
| Data Handling | Functions operate on data passed as arguments. Data is often global and shared. | Data and operations are bundled together in an object. |
| Code Structure | Divided into smaller, reusable functions or modules. | Divided into classes and objects, emphasizing encapsulation. |
7. Explain the following terms/principles in Object Oriented.
 * Encapsulation
   * Hiding an object's internal details and protecting its state. Involves information hiding and restricted access.
   * Example: Using private data members (like balance) and public methods (like deposit()) to control access.
 * Inheritance
   * Allows a new object (child class) to extend the characteristics of an existing object (parent class).
   * Example: A Dog class inherits the eat() method from an Animal class and also has its own bark() method.
 * Abstraction
   * Hiding complex details and showing only the essential features. Focuses on what an object does, not how it does it.
   * Example: An abstract Shape class defines a draw() function, but the specific implementation is left to child classes like Circle.
 * Polymorphism
   * The ability of objects to implement the same interface but behave differently.
   * Example: Dog and Cat classes both inherit from Animal and have a sound() method. When called, the Dog outputs "Woof!" and the Cat outputs "Meow!".
📊 Summary of Software Paradigm (In Chap 1 b)
| Paradigm | Problem classification |
|---|---|
| Imperative (Procedural) | Focus on how a program operates (sequence of steps). E.g., loops, data processing. |
| ⭐ Declarative Paradigm
(Midterm Highlight) | Focus on what should be done (not how).
Example: SQL queries (Select...), LINQ. |
| Object-Oriented | Focus on objects (encapsulated data and behavior).
Example: Simulating real-world systems (cars, traffic lights). |
| Functional Paradigm | Focus on pure functions and avoids state changes/mutable data.
Example: Mathematical modeling (Fibonacci series). |
| Event-Driven | Focus on reacting to events (user actions, sensor inputs).
Example: GUI applications (button clicks). |
| Concurrent/Parallel | Focus on dividing a task for simultaneous execution.
Example: Distributed systems. |
| Component-Based | Focus on creating software from reusable components.
Example: Using APIs (like a payment gateway). |
| Aspect-Oriented | Focus on separating cross-cutting concerns.
Example: Logging, security, error handling. |
| Reactive Paradigm | Focus on reacting to asynchronous events or changes in data.
Example: Real-time dashboards, social media feeds. |
| Artificial Intelligence | Focus on machine learning, reasoning, and optimization algorithms.
Example: Pattern recognition (image, speech). |
| Search-Based Paradigm | Focus on exploring a search space for optimal solutions.
Example: Traveling Salesman Problem (TSP). |