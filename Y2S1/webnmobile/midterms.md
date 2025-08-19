## **Chapter 1: ASP.NET MVC Basics**

**1. Core Concepts / 核心概念**
*   **ASP.NET Software Stack / ASP.NET 软件栈**
    *   **EN:** A collection of software components required to host ASP.NET web applications.
    *   **中文:** 托管 ASP.NET Web 应用程序所需的一组软件组件。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** Think of building a restaurant. You need the **land** (Operating System), the **building** with a kitchen (Web Server), a fully-stocked **pantry** (Database), and a **team of chefs** who know the recipes (Programming Runtime).
        *   **中文:** 把它想象成开一家餐厅。你需要**土地**（操作系统）、带厨房的**建筑**（Web 服务器）、一个存货充足的**食品储藏室**（数据库），以及一个懂得食谱的**厨师团队**（编程运行时）。

*   **MVC Architecture / MVC 架构**
    *   **EN:** A design pattern that separates an application into three main logical components: the Model, the View, and the Controller.
    *   **中文:** 一种将应用程序分为三个主要逻辑组件的设计模式：模型（Model）、视图（View）和控制器（Controller）。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** Ordering food at a restaurant. The **menu** is the **View** (what you see). The **waiter** is the **Controller** (takes your request). The **kitchen** is the **Model** (prepares the food).
        *   **中文:** 在餐厅点餐。**菜单**就是**视图 (View)**（你所看到的）。**服务员**是**控制器 (Controller)**（接收你的请求）。**厨房**就是**模型 (Model)**（准备食物）。

*   **URL Routing / URL 路由**
    *   **EN:** The mechanism that maps incoming browser requests (URLs) to specific controller action methods.
    *   **中文:** 将传入的浏览器请求 (URL) 映射到特定控制器操作方法的机制。
    *   **Code Example / 代码示例:**
        *   **URL:** `https://example.com/Product/Details/P123`
        *   This URL maps to:
        ```csharp
        // Inside a class named "ProductController"
        // 在名为 "ProductController" 的类中
        public IActionResult Details(string id) // id will be "P123"
        {
            // ... code to find product P123 ...
            return View();
        }
        ```
    *   **Daily Life Example / 生活示例:**
        *   **EN:** Giving an address like "Plaza Singapura, Level 3, Zara store". The driver (URL Routing) interprets this to take you to the correct destination.
        *   **中文:** 告诉出租车司机地址，如“Plaza Singapura，3楼，Zara 专卖店”。司机（URL路由）会解读这个逻辑地址，带你到正确的目的地。
---
## **Chapter 2: Reusable Layout & Views**

**1. Core Concepts / 核心概念**
*   **Reusable Layout / 可重用布局**
    *   **EN:** A master view that defines a common structure (e.g., header, footer) for multiple views.
    *   **中文:** 一个主视图，为应用程序中的多个视图定义一个通用结构（例如，页眉、页脚）。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** A company's letter template with a fixed logo at the top and address at the bottom.
        *   **中文:** 公司的信件模板，顶部有固定的标志，底部有地址。

*   **Partial Views / 分部视图**
    *   **EN:** A reusable view that renders a portion of a web page's content.
    *   **中文:** 一种可重用的视图，用于渲染网页内容的一部分。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** The user profile box (with picture and name) seen on social media is a single component (Partial View) reused everywhere.
        *   **中文:** 社交媒体上的用户信息框（有头像和名字）是一个在各处重复使用的独立组件（分部视图）。

**2. Key Differentiations / 主要区别**
*   **Tag Helpers vs. HTML Helpers / 标签助手 vs. HTML 助手**
    *   **EN:** Two ways to generate HTML with server-side logic. Tag Helpers use an HTML-like syntax, while HTML Helpers use C# method syntax.
    *   **中文:** 两种使用服务器端逻辑生成 HTML 的方式。标签助手使用类似 HTML 的语法，而 HTML 助手使用 C# 方法语法。
    *   **Code Example / 代码示例:** (Both generate an HTML link: `<a href="/Home/Index">Go Home</a>`)
        *   **Tag Helper (HTML-like) / 标签助手 (类似HTML):**
            ```html
            <a asp-controller="Home" asp-action="Index">Go Home</a>
            ```
        *   **HTML Helper (C#-like) / HTML 助手 (类似C#):**
            ```csharp
            @Html.ActionLink("Go Home", "Index", "Home")
            ```
    *   **Daily Life Example / 生活示例:**
        *   **EN:** Building with LEGOs. **Tag Helpers** are like using a pre-built LEGO car part. **HTML Helpers** are like using a robot arm that takes complex commands to build the part for you.
        *   **中文:** 玩乐高积木。**标签助手**就像使用一个预先搭建好的乐高汽车零件。**HTML 助手**则像一个机械臂，你给它下达复杂的指令，它为你搭建零件。
---
## **Chapter 3: JavaScript and AJAX Programming**

**1. Core Concepts / 核心概念**
*   **Client-Side (JavaScript) vs. Server-Side (C#) / 客户端 (JavaScript) vs. 服务器端 (C#)**
    *   **EN:** Server-side (C#) code runs on the web server. Client-side (JavaScript) code runs in the user's browser.
    *   **中文:** 服务器端 (C#) 代码在 Web 服务器上运行。客户端 (JavaScript) 代码在用户的浏览器中运行。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** A **calculator** in your hand is **Client-Side** (fast, local). A **bank transfer** is **Server-Side** (requires central processing).
        *   **中文:** 你手中的**计算器**是**客户端**（快速，本地）。而**银行转账**是**服务器端**（需要中央系统处理）。

*   **AJAX (Asynchronous JavaScript and XML)**
    *   **EN:** A technique that allows web applications to send and retrieve data from a server in the background without reloading the page.
    *   **中文:** 一种允许 Web 应用程序在不刷新页面的情况下，在后台从服务器发送和检索数据的技术。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** When you scroll through an Instagram feed, new posts load automatically without the whole page reloading.
        *   **中文:** 当你浏览 Instagram 动态时，新的帖子会自动加载，而整个页面无需刷新。

*   **AJAX Polling / AJAX 轮询**
    *   **EN:** A process of repeatedly sending AJAX requests to a server at a fixed interval to check for new data.
    *   **中文:** 以固定的时间间隔重复向服务器发送 AJAX 请求以检查新数据的过程。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** A food delivery tracking app that updates the driver's location every 10 seconds by repeatedly asking the server for the new position.
        *   **中文:** 一个外卖跟踪应用，通过每10秒重复向服务器询问新位置来更新骑手的位置。
---
## **Chapter 4: Object-Relational Mapping (ORM)**

**1. Core Concepts / 核心概念**
*   **Object-Relational Mapping (ORM) / 对象关系映射**
    *   **EN:** A programming technique that automates the transfer of data between database tables and application objects.
    *   **中文:** 一种自动在数据库表和应用程序对象之间传输数据的技术。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** An ORM is like a **multilingual translator**. You speak "C# Object language," and the database speaks "SQL Table language." The ORM translates between you both.
        *   **中文:** ORM 就像一个**多语言翻译官**。你说“C# 对象语言”，数据库说“SQL 表格语言”。ORM 在你们之间进行翻译。

*   **Database-First vs. Code-First / 数据库优先 vs. 代码优先**
    *   **EN:** **Database-First** generates code from an existing database. **Code-First** generates a database from code.
    *   **中文:** **数据库优先**从现有数据库生成代码。**代码优先**从代码生成数据库。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** Building a house. **Database-First** is having the blueprint first, then building the house. **Code-First** is building the house first, then drawing a blueprint that matches it.
        *   **中文:** 盖房子。**数据库优先**是先有建筑蓝图，再盖房子。**代码优先**是先把房子盖好，再画一张匹配的蓝图。

*   **Constructor Dependency Injection / 构造函数依赖注入**
    *   **EN:** A software design pattern where the dependencies (services) a class needs are provided to it through its constructor.
    *   **中文:** 一种软件设计模式，类所需的依赖项（服务）通过其构造函数提供给它。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** You are a chef who needs a special oven. Instead of building it yourself, the restaurant **provides you with one (injects the dependency)** when you start your job.
        *   **中文:** 你是一名需要特殊烤箱的厨师。你不用自己建造烤箱，而是在你入职时，餐厅就**为你提供了一个（注入依赖项）**。

*   **Database Migration / 数据库迁移**
    *   **EN:** A tool-managed process for evolving the database schema over time, keeping a versioned history of changes.
    *   **中文:** 一种通过工具管理数据库模式随时间演变的过程，并保留一个带版本的变更历史。
    *   **Daily Life Example / 生活示例:**
        *   **EN:** It's like a logbook for house renovations. Each time you add a room, you create a new entry. This log (the Migrations) shows the entire history of how your house was built and modified.
        *   **中文:** 就像一本房屋装修日志。每次你增加一个房间，你都会创建一个新条目。这本日志（迁移）记录了你房子建造和修改的完整历史。
