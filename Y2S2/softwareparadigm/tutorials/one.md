# Tutorial 1(a) - Complete Lecture Notes

## 📝 Tutorial 1 (a): Question 2

### Compare the three categories of software paradigm.

| | **Software Development Paradigm** | **Software Design Paradigm** | **Programming Paradigm** |
| :--- | :--- | :--- | :--- |
| **Hierarchy** | Broadest category | (Middle) | Most granular level |
| **Scope** | Refers to **Software Engineering**. Includes all engineering concepts related to the software development lifecycle. | Can be used to describe a design solution or as an approach to design problem-solving. Guides the organization of code, components, and interfaces. | Represents diverse methods for organizing programming languages and applications. Deals with how code is written and structured. |
| **Summary** | How the **entire software project** is organized and managed. | How the **system architecture** or components are structured. | How **individual code** is written and organized logically. |
| **Activities** | Requirement gathering, system design, programming. | Design, maintenance, programming. | Coding, testing, integration. |
| **Example** | Object-oriented paradigm, Procedural paradigm. | MVC, Microservices. | Functional programming, Object-oriented programming, Imperative programming. |

* **Diagram Note:** The slide also shows a Venn diagram illustrating this hierarchy:
    **Software Development** (largest circle) ➔ **Software Design** (middle circle) ➔ **Programming** (smallest circle).

---

## 🔁 Tutorial 1 (a): Question 3

### Draw a diagram to show the stages of SDLC.

The slide shows the Software Development Life Cycle (SDLC) as a continuous cycle:
**Planning ➔ Analysis ➔ Design ➔ Implementation ➔ Maintenance ➔ (back to Planning)**

Here are the definitions for each stage:

* **1) Planning**
    * Plan for the software design, resources needed, timeline, and budget based on the project needs and requirements.
* **2) Analysis**
    * Requirement gathering and requirement analysis.
    * Gather detailed business and technical requirements for the software and then analyze them into a format like a requirements specifications document.
* **3) Design**
    * The system's architecture and detailed design are created based on the requirements defined in the previous phase.
    * This is a blueprint for the system that developers can follow.
* **4) Implementation**
    * Where the actual coding of the software occurs.
    * Developers take the design specifications and convert them into a working application, followed by testing.
* **5) Maintenance**
    * Ongoing support and updates to ensure the software remains functional, secure, and efficient.
    * Monitor the software performance and address user-reported issues.

---

## 💡 Tutorial 1 (a): Question 4

### Why is a software paradigm important?

* **Provides a Framework for Problem-Solving**
    * A software paradigm offers a **systematic approach** to solving problems by guiding how developers think about and structure solutions.
* **Shapes Software Design and Structure**
    * Each paradigm provides specific **principles and patterns** that influence how software is designed and structured.
* **Improves Development Efficiency**
    * Software paradigms simplify the development process by providing **tested and proven methodologies**.
* **Facilitates Communication and Collaboration**
    * A **shared understanding** of the paradigm being used enables better collaboration among team members, stakeholders, and clients.

---

## 🧩 Tutorial 1 (a): Question 5

### Explain the term Problem Paradigm.

* A **problem paradigm** refers to the conceptual **framework** or approach used to understand, model, and solve problems in the context of software development or other disciplines.
* It refers to a model for **classifying problems** that share a **common set of characteristics**.
* It defines **how problems are perceived, structured, and addressed** using specific methodologies, principles, and tools.
* There may be more than one (multiple) algorithm to solve a problem.

### (Question 5 Add-on: Diagram)

The slide shows a diagram labeled "Problem paradigm" with the following top-down flow:

**Fundamental Operations**
↓
**Algorithmic Structures**
↓
**Problem Classes**

---

## 🆚 Tutorial 1 (a): Question 6

### Compare Function Oriented with Object Oriented.

| Feature | Functional Oriented Paradigm | Object-Oriented Paradigm |
| :--- | :--- | :--- |
| **Main Focus** | Focuses on breaking down problems into smaller, reusable **functions or procedures**. | Focuses on modeling real-world entities using **objects** that encapsulate data (attributes) and behavior (methods). |
| **Data Handling** | Functions operate on data, and the data is usually passed explicitly as **arguments**. | Places **data and the operations** pertaining to the data within a single entity called an **object**. |
| **Code Structure** | Code is divided into smaller, reusable **functions or modules**. | Code is divided into **classes and objects**, emphasizing **encapsulation and abstraction**. |

### (Question 6 Add-on: Diagram/Code Examples)

**Functional Oriented Example:**

This diagram shows a central `main()` function that calls other separate functions:

* `main()`
    * Calls `inputData()` -> which `modifies global data`
    * Calls `calculateAverage()` -> which `reads marks[]`
    * Calls `displayResult()` -> which `prints result`

The key takeaway noted on the slide is: "Data is **global and shared** among all functions."

**Object-Oriented Example:**

This diagram shows a `Student (struct)` which bundles data and functions together:

* **`Student (struct)`**
    * **Data:**
        * `name[]` -> `holds student name`
        * `marks[]` -> `holds student marks`
    * **Methods (functions):**
        * `calculateAverage()` -> `computes average`
        * `displayResult()` -> `prints result`

---

## 🔐 Tutorial 1 (a): Question 7

### Explain the following terms/principles in Object Oriented.

* **Encapsulation**
    * This is when an object **hides its internal details**, protecting its state from external interference. It contains two crucial aspects: **information hiding** and **restricted access**.
    * **Example:** Use private data members and public methods to control access.
    * **Code Example:**
        ```cpp
        class BankAccount {
        private:
            double balance; // private: Hidden from outside

        public:
            BankAccount(double initialBalance) {
                balance = initialBalance;
            }

            void deposit(double amount) {
                balance += amount;
            }
        }
        ```

* **Inheritance**
    * This allows an object to **extend the characteristics of its ancestor objects**, enabling it to specialize its behavior based on those inherited traits.
    * **Code Example:**
        ```cpp
        class Animal {
        public:
            void eat() {
                cout << "Eating..." << endl;
            }
        };

        class Dog : public Animal { // Dog inherits from Animal
        public:
            void bark() {
                cout << "Barking..." << endl;
            }
        };

        int main() {
            Dog d;
            d.eat();  // Inherited from Animal
            d.bark(); // Own method
            return 0;
        }
        ```

* **Abstraction**
    * Abstraction refers to the practice of **hiding details** (showing only the essential features) in order to reduce complexity and enhance efficiency or quality.
    * It focuses on **what** an object does, **not how** it does it.
    * **Code Example:**
        ```cpp
        // Abstract class (has at least one pure virtual function)
        class Shape {
        public:
            virtual void draw() = 0; // pure virtual function
        };

        class Circle : public Shape {
        public:
            void draw() {
                cout << "Drawing a Circle" << endl;
            }
        };
        ```

* **Polymorphism**
    * This refers to the ability of objects that implement the **same interface** to **behave differently** or take on various forms depending on their specific implementation.
    * **Code Example:**
        ```cpp
        class Animal {
        public:
            virtual void sound() {
                cout << "Some generic animal sound" << endl;
            }
        };

        class Dog : public Animal {
        public:
            void sound() override {
                cout << "Woof! Woof!" << endl;
            }
        };

        class Cat : public Animal {
        public:
            void sound() override {
                cout << "Meow!" << endl;
            }
        };
        ```

---

## 📊 Summary of Software Paradigm (In Chap 1 b)

| Paradigm | Problem classification |
| :--- | :--- |
| **Imperative Paradigm (Procedural)** | Focus on describing **how a program operates** through a sequence of steps or commands.<br>**Example:**<br>• Calculations -> need to do multiply / divide only continue for additional / subtraction<br>• Data processing -> when processing a list of numbers, you may loop through the list... |
| **Declarative Paradigm** | Focus on **what should be done** rather than how to do it.<br>**Example:**<br>• Database queries (e.g., SQL) -> Select name, department from employee where salary > 5000<br>• Logic-based problem (e.g., LINQ) -> `EmployeeList.Any(x => x.salary > 5000)` |
| **Object-Oriented Paradigm** | Focus on **objects**, which **encapsulate both data and behavior**. Problems are categorized based on entities and their interactions.<br>**Example:**<V>• Simulation of real-world systems<br>• Modeling Real-world entities (like cars, roads, traffic lights...) |
| **Functional Paradigm** | Focus on the use of **pure functions** and avoids **state changes or mutable data**. Problems are divided into smaller, reusable functions.<br>**Example:**<br>• Mathematical modeling (e.g., the Fibonacci series)<br>• Does not mutate any data... |

---

## 📊 Summary of Software Paradigm (In Chap 1 b) - Continued

| Paradigm | Problem classification |
| :--- | :--- |
| **Event-Driven Paradigm** | Focus on **reacts to events**, such as user actions or sensor outputs.<br>**Example:**<br>• GUI-based applications (e.g., responding to button clicks or user input) |
| **Concurrent/Parallel Paradigm** | Focus on **dividing a task into smaller parts** that can be executed **simultaneously**.<br>**Example:**<br>• Distributed systems (e.g., data processing across multiple machines) |
| **Component-Based Paradigm** | Focus on creating software from **reusable components** that interact through well-defined interfaces.<br>**Example:**<br>• Developing software by composing independent modules (e.g., APIs)... |
| **Aspect-Oriented Paradigm** | Focus on **separating cross-cutting concerns (aspects)** that are scattered across application code.<br>**Example:**<br>• Logging, security, or error handling |
| **Reactive Paradigm** | Focus on **react to asynchronous events or changes in data**.<br>**Example:**<br>• Real-time web applications (e.g., live data dashboards, social media feeds) |
| **Artificial Intelligence Paradigm** | Focus on using **machine learning, reasoning, and optimization algorithms**...<br>**Example:**<br>• Pattern recognition (e.g., image recognition, speech recognition) |
| **Search-Based Paradigm** | Focus on solving problems by **exploring a search space** to find optimal or feasible solutions.<br>**Example:**<br>• Traveling Salesman Problem (TSP)... |

