---

### **Chapter 10: Network Automation**

This chapter introduces concepts and tools for automating network management.

#### **10.1-10.2 Automation and Data Formats**

*   **Automation Benefits**: Increased efficiency, consistency, and the ability to manage complex, large-scale networks.
*   **Data Formats**: Structured formats for exchanging data are the foundation of automation.
    *   **JSON**: Human-readable key/value pairs. Uses `{}` for objects and `[]` for arrays.
    *   **YAML**: A superset of JSON that is easier to read. Uses indentation to define structure instead of brackets.
    *   **XML**: A markup language that uses tags to enclose data, similar to HTML.

#### **10.3-10.4 APIs and REST**

*   **API (Application Programming Interface)**: A set of rules that allows applications to communicate with each other. It acts as an intermediary for requesting and receiving data or services.
*   **REST (Representational State Transfer)**: An architectural style for creating web services. A "RESTful" API uses the standard HTTP protocol for communication.
*   **RESTful Principles**:
    *   **Client-Server Architecture**: Separation of concerns.
    *   **Stateless**: The server does not store client state between requests.
    *   **Cacheable**: Responses can be cached to improve performance.
*   **Anatomy of a RESTful Request**: A request is made to a URI (Uniform Resource Identifier) and typically includes:
    *   An HTTP method (GET, POST, PUT, DELETE).
    *   A path to a resource.
    *   Parameters and an optional authorization key.

#### **10.5 Configuration Management Tools**

*   **Purpose**: These tools use APIs to automate network configuration and management tasks at scale.
*   **Key Tools**:
    *   **Ansible**: Agentless, uses Python and YAML. Configurations are defined in "Playbooks".
    *   **Puppet**: Uses a master-agent model and its own declarative language. Configurations are in "Manifests".
    *   **Chef**: Also uses a master-agent model and Ruby. Configurations are in "Recipes" and "Cookbooks".
    *   **SaltStack (Salt)**: A Python-based system that is very fast and scalable.

---
