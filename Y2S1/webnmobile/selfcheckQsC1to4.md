
***

### **Chapter 1: ASP.NET MVC Basics**

**1. Suggest an appropriate software stack for hosting ASP.NET web applications.**
*   **EN:** A standard and appropriate software stack is the Microsoft stack:
    *   **Operating System:** Windows Server
    *   **Web Server:** Internet Information Services (IIS)
    *   **Database Server:** Microsoft SQL Server
    *   **Programming Runtime:** ASP.NET (using C#)
*   **中文:** 一套标准且合适的软件栈是微软技术栈：
    *   **操作系统:** Windows Server
    *   **Web 服务器:** Internet Information Services (IIS)
    *   **数据库服务器:** Microsoft SQL Server
    *   **编程运行时:** ASP.NET (使用 C#)

**2. Discuss the advantages of using the ASP.NET platform.**
*   **EN:**
    *   **Existing Software Environment:** Many companies already use a Windows-based environment, making adoption easier and more cost-effective.
    *   **Customer Support:** As a commercial Microsoft product, it comes with official, professional customer support.
    *   **Expandability & Scalability:** It is an enterprise-grade platform designed to handle large, complex projects that can grow over time.
    *   **Consistent Software Components:** The entire stack (OS, web server, database) is developed by Microsoft, ensuring **seamless integration**.
    *   **Strongly Typed Language:** C# is **strongly typed**, which is safer and less risky for large projects compared to dynamically typed languages like PHP.
*   **中文:**
    *   **利用现有软件环境:** 许多公司已在使用基于 Windows 的环境，这使得采用 ASP.NET 更容易、更具成本效益。
    *   **客户支持:** 作为微软的商业产品，它提供官方的专业客户支持。
    *   **可扩展性与可伸缩性:** 它是为处理可随时间增长的大型复杂项目而设计的企业级平台。
    *   **一致的软件组件:** 整个技术栈（操作系统、Web 服务器、数据库）由微软开发，确保**无缝集成**。
    *   **强类型语言:** C# 是**强类型**的，与 PHP 等动态类型语言相比，对于大型项目更安全、风险更低。

**3. Identify and discuss the role of the 3 core components of MVC web architecture. Provide 2 examples for each.**
*   **EN:**
    *   **Model:** Manages the application's data and business logic.
        *   *Examples:* A `Product.cs` class that defines the properties of a product; the `ApplicationDbContext` class that manages database connections.
    *   **View:** The user interface (UI). It is responsible for displaying the data provided by the controller.
        *   *Examples:* The `Login.cshtml` file that shows the login form; the `Product/Index.cshtml` file that displays a list of all products.
    *   **Controller:** The application's logic handler. It receives user requests, interacts with the Model to fetch or update data, and then selects a View to render the final response.
        *   *Examples:* The `ProductController.cs` class that handles all product-related requests; the `Index()` action method inside `HomeController.cs` that handles the request for the homepage.
*   **中文:**
    *   **模型 (Model):** 管理应用程序的数据和业务逻辑。
        *   *示例:* 定义产品属性的 `Product.cs` 类；管理数据库连接的 `ApplicationDbContext` 类。
    *   **视图 (View):** 用户界面 (UI)。它负责显示控制器提供的数据。
        *   *示例:* 显示登录表单的 `Login.cshtml` 文件；显示所有产品列表的 `Product/Index.cshtml` 文件。
    *   **控制器 (Controller):** 应用程序的逻辑处理器。它接收用户请求，与模型交互以获取或更新数据，然后选择一个视图来渲染最终响应。
        *   *示例:* 处理所有产品相关请求的 `ProductController.cs` 类；处理主页请求的 `HomeController.cs` 中的 `Index()` 操作方法。

**4. Discuss the advantages of MVC web architecture.**
*   **EN:**
    *   **Separation of Concerns:** This is the core advantage. Each component has a single, distinct responsibility, which makes the codebase organized and clean.
    *   **Parallel Development:** It allows a team to work simultaneously: designers can work on the View while developers work on the Controller and Model.
    *   **Maintainability & Reusability:** It is easier and safer to make changes. Updating the UI in the View has minimal impact on the Controller's logic. Components can also be easily reused.
    *   **Unit Testable:** The separation of logic from the UI makes it easy to write automated tests for the Controller and Model.
*   **中文:**
    *   **关注点分离:** 这是核心优势。每个组件都有一个单一、明确的职责，这使得代码库组织有序且整洁。
    *   **并行开发:** 它允许团队同时工作：设计师可以处理视图，而开发人员可以处理控制器和模型。
    *   **可维护性与可重用性:** 进行更改更容易、更安全。更新视图中的 UI 对控制器的逻辑影响最小。组件也可以轻松重用。
    *   **单元可测试性:** 将逻辑与 UI 分离，使得为控制器和模型编写自动化测试变得容易。

**5. Discuss why URL routing is necessary for ASP.NET MVC web applications.**
*   **EN:** URL routing is necessary because, unlike traditional web applications where a URL points to a physical file on the server (e.g., `/pages/about.html`), an MVC URL points to a **logical piece of code**: a specific action method inside a controller class. The URL routing engine is the mechanism that interprets an incoming URL and translates it to execute the correct method.
*   **中文:** URL 路由是必需的，因为与传统 Web 应用程序中 URL 指向服务器上的物理文件（例如 `/pages/about.html`）不同，MVC 中的 URL 指向的是**一段逻辑代码**：一个控制器类中的特定操作方法。URL 路由引擎是解析传入 URL 并将其转换为执行正确方法的机制。

**6. Discuss how the following URL is mapped: `https://.../Product/Update/P001?quantity=123`**
*   **EN:**
    *   `Product`: Maps to the controller class named **`ProductController`**.
    *   `Update`: Maps to the action method named **`Update()`** inside the `ProductController`.
    *   `P001`: Maps to a parameter in the `Update` method, typically named **`id`**.
    *   `?quantity=123`: Maps to a parameter in the `Update` method named **`quantity`** with a value of 123.
*   **中文:**
    *   `Product`: 映射到名为 **`ProductController`** 的控制器类。
    *   `Update`: 映射到 `ProductController` 中名为 **`Update()`** 的操作方法。
    *   `P001`: 映射到 `Update` 方法中通常名为 **`id`** 的参数。
    *   `?quantity=123`: 映射到 `Update` 方法中名为 **`quantity`**、值为 123 的参数。

**7. Write the URL to access the following controller and action method. Pass S001 for id and 2024 for year.**
*   **Controller:** `StudentController`
*   **Action Method:** `Search()`
*   **URL:** `https://www.abc.com/Student/Search/S001?year=2024`

**8. Rewrite the following codes by filling in the missing part so that it maps to the following URL: `https://.../Product/Update/P001?quantity=123`**
```csharp
public class ProductController : Controller
{
    public IActionResult Update(string id, int quantity)
    {
        // ... method logic here ...
        // id will be "P001"
        // quantity will be 123
        return View();
    }
}
```

***

### **Chapter 2: Reusable Layout**

**1. What are the advantages of using reusable layout?**
*   **EN:**
    *   **Consistency:** It provides a consistent look, feel, and user experience across all pages of a website.
    *   **Reduces Code Duplication:** It eliminates the need to repeat the same HTML code (like headers, navigation bars, and footers) in every single view file, making the application much easier to maintain.
*   **中文:**
    *   **一致性:** 它为网站的所有页面提供一致的外观、感觉和用户体验。
    *   **减少代码重复:** 它无需在每个视图文件中重复相同的 HTML 代码（如页眉、导航栏和页脚），使得应用程序更易于维护。

**2. What are tag helpers?**
*   **EN:** Tag helpers are a server-side feature in ASP.NET that allows developers to extend standard HTML elements with special attributes (usually prefixed with `asp-`). These attributes are processed on the server to generate HTML, making the code look cleaner and more like standard HTML.
*   **中文:** 标签助手是 ASP.NET 中的一项服务器端功能，它允许开发人员使用特殊属性（通常以 `asp-` 为前缀）来扩展标准的 HTML 元素。这些属性在服务器上处理以生成 HTML，使得代码看起来更整洁，更像标准的 HTML。

**3. Differentiate between tag helpers and HTML helpers.**
*   **EN:**
    *   **Syntax:** Tag helpers use an **HTML-like syntax** (`<a asp-controller="...">`). HTML helpers use a **C#-like function call syntax** (`@Html.ActionLink(...)`).
    *   **Readability:** Tag helpers are generally more readable for people familiar with HTML, like web designers. HTML helpers mix C# and HTML, which can be less readable.
    *   **Target Audience:** Tag helpers are friendlier to designers, while HTML helpers are more familiar to C# developers.
*   **中文:**
    *   **语法:** 标签助手使用**类似 HTML 的语法** (`<a asp-controller="...">`)。HTML 助手使用**类似 C# 的函数调用语法** (`@Html.ActionLink(...)`)。
    *   **可读性:** 对于熟悉 HTML 的人（如网页设计师）来说，标签助手通常更易读。HTML 助手混合了 C# 和 HTML，可读性可能较差。
    *   **目标用户:** 标签助手对设计师更友好，而 HTML 助手对 C# 开发人员更熟悉。

**4. What are partial views?**
*   **EN:** A partial view is a reusable view file that renders a **portion** of a web page. It is not a complete page on its own and must be called from within a main view. They are used to break down large, complex views into smaller, manageable components and to reuse UI elements in multiple places.
*   **中文:** 分部视图是一个可重用的视图文件，用于渲染网页的**一部分**。它本身不是一个完整的页面，必须从主视图中调用。它们用于将大型复杂的视图分解为更小的、可管理的组件，并在多个地方重用 UI 元素。

***

### **Chapter 3: JavaScript and AJAX Programming**

**1. Discuss how JavaScript (client-side) is different from C# (server-side).**
*   **EN:**
    *   **Execution Location:** C# runs on the **server**. JavaScript runs in the user's **web browser (client)**.
    *   **Purpose:** C# is used for secure business logic, database access, and generating the initial HTML. JavaScript is used for UI interactivity, client-side validation, and making asynchronous requests to the server.
    *   **Resource Access:** C# has full access to server resources like the database and file system. JavaScript is sandboxed in the browser and has very limited access to the user's computer.
*   **中文:**
    *   **执行位置:** C# 在**服务器**上运行。JavaScript 在用户的**网页浏览器（客户端）**中运行。
    *   **用途:** C# 用于安全的业务逻辑、数据库访问和生成初始 HTML。JavaScript 用于 UI 交互、客户端验证以及向服务器发出异步请求。
    *   **资源访问:** C# 可以完全访问服务器资源，如数据库和文件系统。JavaScript 在浏览器中是沙盒化的，对用户计算机的访问权限非常有限。

**2. Define unobtrusive JavaScript.**
*   **EN:** Unobtrusive JavaScript is a methodology that emphasizes the **separation of behavior (JavaScript) from structure (HTML)**. This means avoiding placing JavaScript code directly inside HTML tags (like using `onclick` attributes) and instead attaching event handlers programmatically from external scripts.
*   **中文:** 无侵入式 JavaScript 是一种强调**将行为 (JavaScript) 与结构 (HTML) 分离**的方法论。这意味着避免将 JavaScript 代码直接放在 HTML 标签内（例如使用 `onclick` 属性），而是从外部脚本以编程方式附加事件处理器。

**3. Suggest a better way to handle the event in `<button onclick="alert('Hello')">Hello</button>`.**
*   **EN:** The `onclick` attribute is an example of obtrusive JavaScript. A better, unobtrusive way is to:
    1.  Keep the HTML clean by giving the button an ID: `<button id="helloBtn">Hello</button>`.
    2.  Use a separate `<script>` block or `.js` file to attach the event handler:
        ```javascript
        document.getElementById('helloBtn').onclick = function() {
            alert('Hello');
        };
        ```
*   **中文:** `onclick` 属性是侵入式 JavaScript 的一个例子。一种更好、无侵入式的方法是：
    1.  通过给按钮一个 ID 来保持 HTML 的整洁：`<button id="helloBtn">Hello</button>`。
    2.  使用一个单独的 `<script>` 块或 `.js` 文件来附加事件处理器：
        ```javascript
        document.getElementById('helloBtn').onclick = function() {
            alert('Hello');
        };
        ```

**4. Discuss the advantages of writing unobtrusive JavaScript.**
*   **EN:**
    *   **Maintainability:** Separating code makes it cleaner and easier to find and update.
    *   **Task Distribution:** Designers can work on the HTML/CSS while developers work on the JavaScript without conflict.
    *   **Modularity:** JavaScript code can be organized into reusable modules.
    *   **Graceful Degradation:** The website can remain functional even if the JavaScript fails to load or is disabled by the user.
*   **中文:**
    *   **可维护性:** 分离代码使其更整洁，更容易查找和更新。
    *   **任务分配:** 设计师可以处理 HTML/CSS，而开发人员可以处理 JavaScript，两者不会冲突。
    *   **模块化:** JavaScript 代码可以被组织成可重用的模块。
    *   **平稳退化:** 即使 JavaScript 加载失败或被用户禁用，网站仍然可以保持功能性。

**5. Discuss the problems of traditional page loading approach without AJAX.**
*   **EN:**
    *   **Full-Page Reload:** Every action requires the entire page to be re-downloaded from the server.
    *   **Wasted Bandwidth:** Static content like headers and footers are reloaded unnecessarily.
    *   **Lost View Context:** The user's scroll position is lost, and the page always jumps back to the top.
    *   **Poor User Experience:** The process is slow and feels clunky, often with a noticeable "white flash" during reloads.
*   **中文:**
    *   **整页重新加载:** 每个操作都需要从服务器重新下载整个页面。
    *   **浪费带宽:** 像页眉和页脚这样的静态内容被不必要地重新加载。
    *   **丢失视图上下文:** 用户的滚动位置会丢失，页面总是跳回顶部。
    *   **糟糕的用户体验:** 过程缓慢且感觉笨拙，重新加载时通常会有明显的“白屏闪烁”。

**6. Discuss AJAX programming technique and its advantages.**
*   **EN:** AJAX (Asynchronous JavaScript and XML) is a technique that allows a web page to send requests to and retrieve data from a server in the background, without interfering with the current page. Its primary function is to enable **partial reloads**.
    *   **Advantages:**
        *   **Improved Responsiveness:** The application feels faster as only necessary data is updated.
        *   **Reduced Bandwidth:** It only fetches the data it needs, not the entire page markup.
        *   **Retained View Context:** Users stay on the same part of the page without being scrolled back to the top.
*   **中文:** AJAX (异步 JavaScript 和 XML) 是一种允许网页在不干扰当前页面的情况下，在后台向服务器发送请求和检索数据的技术。其主要功能是实现**局部刷新**。
    *   **优点:**
        *   **改善响应速度:** 由于只更新必要的数据，应用程序感觉更快。
        *   **减少带宽消耗:** 它只获取所需的数据，而不是整个页面的标记。
        *   **保留视图上下文:** 用户停留在页面的同一部分，而不会被滚动回顶部。

**7. Suggest some AJAX features that can be implemented into web applications.**
*   **EN:** Live search results, auto-suggestions, sorting/filtering/paging data tables without a full reload, submitting comments or likes, and infinite scrolling.
*   **中文:** 实时搜索结果、自动建议、无需整页刷新的数据表排序/筛选/分页、提交评论或点赞，以及无限滚动。

**8. Discuss the AJAX polling technique.**
*   **EN:** AJAX polling is a technique used to simulate real-time communication. The client-side JavaScript repeatedly sends AJAX requests to the server at a fixed interval (e.g., every 5 seconds) to check if there is any new data.
*   **中文:** AJAX 轮询是一种用于模拟实时通信的技术。客户端的 JavaScript 以固定的时间间隔（例如每5秒）重复向服务器发送 AJAX 请求，以检查是否有任何新数据。

**9. What is the problem of AJAX polling?**
*   **EN:** The main problem is that it is **inefficient** and creates **high server and client load**. Many requests are wasted if there is no new data, and a high frequency of requests can overwhelm the server.
*   **中文:** 主要问题是它**效率低下**，并会造成**高的服务器和客户端负载**。如果没有新数据，许多请求都会被浪费掉，而高频率的请求可能会使服务器不堪重负。

**10. Discuss the purpose of extension methods in C#.**
*   **EN:** The purpose of extension methods is to allow developers to **add new methods to existing types without modifying their original source code**, creating a new derived type, or recompiling them. This is useful for adding functionality to classes you don't own, like built-in .NET types.
*   **中文:** 扩展方法的目的是允许开发人员**在不修改原始源代码、创建新的派生类型或重新编译的情况下，向现有类型添加新方法**。这对于向您不拥有的类（如内置的 .NET 类型）添加功能非常有用。

***

### **Chapter 4: Object-Relational Mapping (ORM)**

**1. What is object-relational mapping (ORM)? Identify how relational model is mapped to object model.**
*   **EN:** ORM is a programming technique that acts as a translator between a relational database (which uses tables) and an object-oriented programming language (which uses objects).
    *   **Mapping:**
        *   Database `Table` → C# `Class`
        *   Table `Column` → Class `Property`
        *   Table `Record (Row)` → Class `Object` instance
        *   Database `Relationship` (Foreign Key) → Class `Association` (Navigation Property)
*   **中文:** ORM 是一种编程技术，它在关系型数据库（使用表）和面向对象的编程语言（使用对象）之间充当翻译器。
    *   **映射:**
        *   数据库 `表` → C# `类`
        *   表 `列` → 类 `属性`
        *   表 `记录 (行)` → 类 `对象` 实例
        *   数据库 `关系` (外键) → 类 `关联` (导航属性)

**2. Discuss the advantages of using an ORM tool.**
*   **EN:**
    *   **Automation:** It automatically generates SQL code or model classes, saving a lot of development time.
    *   **Object-Oriented:** Allows developers to work with data as objects, which is more natural in an object-oriented language like C#.
    *   **SQL-less:** Eliminates the need to write repetitive, boilerplate SQL for basic CRUD (Create, Read, Update, Delete) operations.
    *   **Database Support:** Makes it easier to switch between different database systems (e.g., from SQL Server to MySQL) because the ORM handles the vendor-specific SQL generation.
    *   **Secure Code:** Automatically handles parameterization of queries, which helps prevent SQL injection attacks.
*   **中文:**
    *   **自动化:** 它会自动生成 SQL 代码或模型类，节省大量开发时间。
    *   **面向对象:** 允许开发人员以对象的方式处理数据，这在像 C# 这样的面向对象语言中更自然。
    *   **无需编写 SQL:** 无需为基本的 CRUD (创建、读取、更新、删除) 操作编写重复的、样板式的 SQL。
    *   **数据库支持:** 使得在不同数据库系统之间切换（例如从 SQL Server 切换到 MySQL）变得更容易，因为 ORM 会处理特定于供应商的 SQL 生成。
    *   **代码更安全:** 自动处理查询的参数化，这有助于防止 SQL 注入攻击。

**3. Discuss the key disadvantage of using an ORM tool.**
*   **EN:** The key disadvantage is **performance**. The ORM adds a layer of abstraction that creates overhead. For complex queries, a hand-written, highly optimized SQL statement will almost always be faster than the SQL generated by the ORM.
*   **中文:** 主要缺点是**性能**。ORM 增加了一个会产生开销的抽象层。对于复杂的查询，手动编写的高度优化的 SQL 语句几乎总是比 ORM 生成的 SQL 更快。

**4. Differentiate between database-first and code-first database development.**
*   **EN:**
    *   **Database-First:** You start with a **pre-existing database**. The ORM tool is then used to read the database schema and automatically generate the C# model classes.
    *   **Code-First:** You start by **writing the C# model classes first**. The ORM tool then reads your code and automatically generates the database schema (tables, columns, etc.) based on your classes.
*   **中文:**
    *   **数据库优先:** 你从一个**已有的数据库**开始。然后使用 ORM 工具读取数据库模式并自动生成 C# 模型类。
    *   **代码优先:** 你首先**编写 C# 模型类**。然后 ORM 工具读取你的代码，并根据你的类自动生成数据库模式（表、列等）。

**5. Describe how services are made available to controllers via constructor dependency injection.**
*   **EN:** In this pattern, a controller does not create its own dependencies (like a database context service). Instead, it **declares the services it needs as parameters in its constructor**. When a request comes in, the ASP.NET framework's service container is responsible for creating an instance of the required service and "injecting" (passing) it into the controller's constructor when the controller is created.
*   **中文:** 在这种模式下，控制器不创建自己的依赖项（如数据库上下文服务）。相反，它在**其构造函数中将所需的服务声明为参数**。当请求传入时，ASP.NET 框架的服务容器负责创建所需服务的实例，并在创建控制器时将其“注入”（传递）到控制器的构造函数中。

**6. Discuss the reason and purpose of using database migration.**
*   **EN:**
    *   **Reason:** In a Code-First approach, the C# model classes are the "source of truth." As development progresses, these classes will inevitably change (e.g., adding a new property).
    *   **Purpose:** The purpose of database migration is to **manage these changes and keep the database schema in sync with the C# models**. It creates a versioned history of changes, allowing developers to apply (upgrade) or revert (downgrade) the database structure safely.
*   **中文:**
    *   **原因:** 在代码优先方法中，C# 模型类是“事实的来源”。随着开发的进行，这些类不可避免地会发生变化（例如，添加一个新属性）。
    *   **目的:** 数据库迁移的目的是**管理这些变化并保持数据库模式与 C# 模型同步**。它创建了一个带版本的变更历史，允许开发人员安全地应用（升级）或回滚（降级）数据库结构。
