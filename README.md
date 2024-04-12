# Welcome to the ScrollStack

This is your personal book register, a web application designed to transform the way you manage your personal library. Tailored for book enthusiasts, students, researchers, minimalists, and anyone in between, this platform provides a user-friendly and efficient solution for cataloging, organizing, and accessing your book collection digitally.

In a world where space is a premium and the ease of accessing information is paramount, the ScrollStack stands out as a digital haven for your books. Whether you're tracking your reading habits, decluttering your physical space, or simply organizing your vast collection of literature, this platform caters to your needs. It allows for the addition, editing, categorization, and detailed viewing of each book in your personal collection.

Developed with the user in mind, this application aims to enhance your reading experience, making your personal library accessible at the click of a button, anywhere, anytime. Dive into a world where managing your books is no longer a chore but a delightful experience.


![ScrollStack Preview](/documentation/readme-img/placeholder.webp)

Developer: [JaqiKal](https://github.com/JaqiKal)<br>
Deployed website: [Link to website](#)<br>

---

# Table of Contents

- [Introduction](#introduction)
    - [Project Overview](#project-overview)
    - [Objectives](#objectives)
    - [Developer Goals](#developer-goals)
    - [User Goals](#user-goals)
- [Technologies Used](#technologies-used)
    - [Programming Languages](#programming-languages)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Database](#database)
    - <a href="#tools-services">Tools and Services</a>
- [System Architecture](#system-architecture)
    - [Application Structure](#application-structure)
    - [Backend Logic](#backend-logic)
    - [Programming Paradigms](#programming-paradigms)
- [Agile Development Process](#agile-development-process)
    - [Overview of Agile Methodology](#overview-of-agile-methodology)
    - <a href="#epics-and-user-stories">Epics and User Stories</a>
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Project Tracking (GitHub Projects)](#project-tracking-github-projects)
- [Data Modeling and Database Design](#data-modeling-and-database-design)
    - [Entity-Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Database Schema](#database-schema)
    - [Data Flow and Architecture](#data-flow-and-architecture)
- [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)
- [User Experience Design](#user-experience-design)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
- [Frontend Design](#frontend-design)
    - [Wireframes](#wireframes)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Imagery](#imagery)
    - [Accessibility Features](#accessibility-features)
    - [Responsiveness](#responsiveness)
- [Navigation and Page Layouts](#navigation-and-page-layouts)
    - [Landing Page](#landing-page)
    - [Registration & Login](#registration--login)
    - [User Profile](#user-profile)
    - [Book Management](#book-management)
    - [Administration Panel](#administration-panel)
    - [Logout](#logout)
- [Testing](#testing)
    - [Documented Bugs and Fixes](#documented-bugs-and-fixes)
- [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Local Development Setup](#local-development-setup)
    - [Cloning and Forking Instructions](#cloning-and-forking-instructions)
    - [Dependencies and Environment Setup](#dependencies-and-environment-setup)
- [Deployment](#deployment)
    - <a href="#prerequisites">Prerequisites</a>
    - <a href="#heroku-deployment">Heroku Deployment</a>
    - <a href="#local-deployment">Local Deployment</a>
        - [How to Fork](#how-to-fork)
        - [How to clone](#how-to-clone)
        - [Setting up your local environment](#setting-up-your-local-environment)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
    - [Code](#code)
    - [Media](#media)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)



## Introduction

### Project Overview

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Objectives

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Developer Goals

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### User Goals

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Technologies Used

### Programming Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) - Structure the content of our application.
- [CSS](https://en.wikipedia.org/wiki/CSS) - Style the application to enhance the user interface.
- [JavaScript](https://sv.wikipedia.org/wiki/Javascript) - Add interactivity to web pages, improving the user experience.
- [Python](https://www.python.org) - is used as the back-end programming language.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Frameworks and Libraries

- [Django](https://www.djangoproject.com/) - a framework for developing web applications written in Python.
- [Bootstrap](https://getbootstrap.com/) - a front-end framework designed to help developers build responsive and mobile-first websites and web applications. It provides a collection of CSS and JavaScript tools for creating layouts, forms, buttons, navigation, and other interface components, as well as optional JavaScript extensions. 
- [Cloudinary](https://cloudinary.com/) - a cloud-based platform for storing and serving images

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Database

-  [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

<details id="tools-services">
<summary style="font-size: 1.2em; font-weight: bold;">Tools and Services</summary>

<br>

- [Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.
- [ASPOSE](https://products.aspose.app/pdf/sv/conversion/jpg-to-webp#): Used to convert image to WEBP.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
- [Birme](https://www.birme.net/) - To resize images and change to webp format.
- cdnjs: content delivery network
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/): A tool to check Python code against some of the style conventions in [PEP8](https://peps.python.org/pep-0008/).
- [Coolors](https://coolors.co/) - Used to create the colour scheme palette.
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) - Used to check code ensuring that my CSS is error-free and adheres to the latest web standards.
- DB diagram: used for building an ER diagram.
- [DevTools](https://developer.chrome.com/docs/devtools) -  help in edit pages on-the-fly and diagnose problems quickly.
- [Diffchecker - text](https://www.diffchecker.com/text-compare/) - used to check code snippets
- Draw.io: useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
- [Draw.io](https://www.drawio.com/)- Useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
- [Favicon.io](https://favicon.io/) - To create favicon.
- [Font Awesome](https://fontawesome.com/) - For the iconography on the website.
- [Git](https://git-scm.com/) - For version control.
- [Gitpod](https://gitpod.io) Streamlines your development process by providing a pre-configured, cloud-based development environment that's instantly ready for coding.
- [Github](https://github.com/) - essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
- [Google Dev Tools](https://developers.google.com/web/tools) - used during testing, debugging and styling.
- [Google Fonts](https://fonts.google.com/) - a catalog of free, open-source fonts. Used for typography.
- [Heroku](https://www.heroku.com)- A platform for deploying and hosting web applications. 
- JSHint: a code validation tool used for JavaScript.
- [Markup Validation Service](https://validator.w3.org/) - Used to check code ensuring that my HTML is error-free and adheres to the latest web standards.
- [PEP8](https://peps.python.org/pep-0008/)- Style Guide for Python Code.
- [Shields.io](https://shields.io/) - To add badges to the README.
- [Tiny PNG](https://tinypng.com/) - To compress images.
- [Wave](https://wave.webaim.org) - WAVE® is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities.
- [Web Disability Sim](https://chromewebstore.google.com/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) - a google chrome extension that allows you to view your site as people with accessibility needs would see it.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

## System Architecture

### Application Structure

ScrollStack is structured around the Model-View-Controller (MVC) pattern, which separates the application into three interconnected components. This separation helps manage complex development and enables efficient teamwork by segmenting the app into manageable parts.

Frontend is built using HTML, CSS and JavaScript to create a mobile-first, responsive design. I chose Bootstrap for its comprehensive library of pre-styled components and responsive grid system, which  
accelerated the development process and ensured a seamless, mobile-first user experience across different devices.

The backend architecture is built on Python and Django, where Django simplifies the application's backend logic, manages URL routing, and ensures efficient database interactions, providing a stable and efficient backbone for the app's operations.

In this project, we employ a relational database 'PostgreSQL' for its robustness, scalability, and compatibility with Django, structuring it to store user and book information in an organized manner, which optimizes data retrieval and supports complex queries efficiently.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Backend Logic

Placeholder text!

```text
- Detail the data models used, such as Book, User, Author, and Genre, explaining the relationships between them (e.g., one-to-many from Author to Book).
- Describe how business logic is implemented in Django views and models, including user authentication, book management (CRUD operations), and permissions for different user roles.
- If any external APIs or integrations are used (e.g., for user authentication, email services), explain their purposes and how they’re incorporated into the backend.
```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   


### Programming Paradigms

Placeholder text!

```text
- Object orientated programming
- Procedural programming
- Event-driven Programming
```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Agile Development Process

### Overview of Agile Methodology

Agile methodologies and principles were used when planning and creating The ScrollStack. Development was organized by focusing on the prioritization of user story or stories. The user stories are arranged on a KanBan board, which was continuously managed throughout development to enable prioritization of the workload.

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10)


*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

<details id="epics-and-user-stories">
<summary style="font-size: 1.2em; font-weight: bold;">Epics and User Stories</summary>

<br>

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10)
<br>

| Epic | User Story|
| - | - |
| Initial Project Planning and Documentation | Review LO in PP4 Assessment Material|
| | Initiate and Continuously Update README File |
| | Structured Planning and Documentation Framework |
| | Prioritize User Stories |
| | Create Wireframe |
| | Create ERD |
| Project Setup and Initial Configuration | GitHub Repository Setup |
| | IDE Setup |
| Model Related | Create Book Model |
| | Implement other Models (e.g., Genre, Author) |
| User Authentication and Authorization | Sign Up for an Account |
| | Log In and Out of the Application |
| | Reset Forgotten Password |
| Book Management | Add New Books to Collection |
| | View List of Books  |
| | Edit Book Details |
| | Delete a Book  |
| Searching and Filtering | Search by Title or Author |
| | Filter by Genre |
| Profile Management | Update Profile Details |
| | Upload a Profile Picture |
| View Related | Develop Dashboard View |
| Template Related | Design Base Template |
| | Create Error Handling Template |
| Responsiveness and Accessibility | Ensure Website Responsiveness |
| | Follow Accessibility Best Practices |
| User Feedback | Implement Feedback and Issue Reporting Feature |
| | Provide User Access to Documentation and Help Guides |
| Testing and Quality Assurance | Write Unit Tests for the Book Model |
| | User Acceptance Testing on Mobile Devices |
| | Manually Test User Registration and Profile Management|
| | Perform Comprehensive Cross-Browser and Device Compatibility Testing |
| Deployment, Documentation | Document Deployment Process |
| | Secure Application for Deployment |
| | Prepare Application for Cloud Deployment |
| | Document Design and Development Process |

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

### MoSCoW Prioritization

Labels were added to user stories to assist with prioritization of tasks. The MoSCoW system involves adding labels for MUST HAVE, SHOULD HAVE, COULD HAVE and WON'T HAVE. By labelling issues in such a way, the developer can focus on completing all the MUST HAVE tasks before moving onto tasks of lower priority, this is critical when working to a tight deadline to ensure a minimum viable product is completed in time.

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10) and/or [Issues list](https://github.com/JaqiKal/ScrollStack/issues)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Project Tracking (GitHub Projects)

The project use a Kanban board for organization, serving as a dynamic document continually managed to effectively prioritize and organize workload. The board categorized tasks into various stages, from Backlog for items not yet started to Done for completed tasks. As development commenced on a User Story, it transitioned from Backlog to In Progress, and upon completion, both the User Story and its associated Epic were moved to Done. Additionally, unresolved bugs were tracked separately until resolved, at which point they were also moved to the Done column. Kanban methodology proved invaluable in tracking project progress through its various phases, offering flexibility to adapt to the project's unique needs.

For details please follow link to: [GitHub Project board](https://github.com/users/JaqiKal/projects/10).

| Kanban | Description |
|--|--|
| Backlog (EPIC, US) | Items not yet started|
| Ready to Start (EPIC, US) | Tasks ready for implementation |
| In Progress (EPIC) | Epic currently being worked on |
| In Progress (US) | User story currently being worked on |
| In Review | Tasks undergoing testing |
| BUG | Newly discovered and unresolved issues |
| Done | Completed tasks (Epic, US and fixed bugs) |
| Future Feature | Features planned for future enhancement beyond the minimum viable product (MVP), and not included by handover (2024-05-10)  |
| Won't have | Ideas considered but not included in the project scope |

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Data Modeling and Database Design

### Entity-Relationship Diagram (ERD)

This diagram serves as a quick reference to understand the database's structure at a glance.

Placeholder text!
```text
- Include a simplified ERD img
- Briefly describe the key entities, their attributes, and the types of relationships.
```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Database Schema

For ScrollStack, we've adopted PostgreSQL for its advanced capabilities and flexibility in handling our dataset. This relational database supports essential features for our digital bookshelf, including book CRUD operations. The structure features entities like Book and User, with a one-to-many relationship from User to Books indicating ownership. Data integrity is enforced through constraints, such as foreign keys and NOT NULL, ensuring reliability and well-organized data that underpins ScrollStack's seamless functionality.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Data Flow and Architecture

ScrollStack leverages the MVC (Model-View-Controller) architecture to optimize the flow of data between the user interface and the database, ensuring a dynamic and responsive experience. Here's how it works:

When a user performs an action, such as adding a book, the request is handled by the Controller. It then interfaces with the Model to perform database operations. Upon successful database update, the Model signals the Controller, which instructs the View to update the display accordingly—showing the latest book list without needing a page reload.

This setup is made efficient through the use of AJAX<sup>1)</sup>, enabling asynchronous data updates that enhance user interaction. Middleware plays a critical role in routing requests, authentication, and overall data management. The MVC framework, together with AJAX and middleware<sup>2)</sup>, allows ScrollStack to provide quick and seamless updates to the user interface, facilitating a better user experience and streamlined maintenance.

<sup>1)</sup>AJAX is built into the web development environment through JavaScript and does not require external installation. It's readily available for use in creating dynamic, interactive web applications."

 <sup>2)</sup>Middleware in the context of web development acts as a bridge between the client and server, managing requests and responses, and performing various tasks such as authentication, authorization, routing, session management, error handling, data processing, logging, monitoring, and CORS (Cross-Origin Resource Sharing) management.


*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Features

### Current Features

- Initial Project Planning and Documentation: Structured planning, README file updates, wireframing, ERD creation.
- Project Setup and Configuration: GitHub setup, IDE configuration.
- Model Related: Creation of Book (Optional: genre, and Author models).
- User Authentication and Authorization: Account signup, login/logout, password reset.
- Book Management: Adding, viewing, editing, and deleting books.
- Searching and Filtering: Search by title or author, filter by genre.
- Profile Management: Update profile details, upload a profile picture.
- View Related: Development of a dashboard view.
- Template and Design: Base template design, error handling templates.
- Responsiveness and Accessibility: Ensuring website responsiveness, accessibility best practices.
- User Feedback: Feedback and issue reporting, access to documentation and help guides.
- Testing and Quality Assurance: Writing unit tests, user acceptance testing, cross-browser testing.
- Deployment and Documentation: Documenting deployment and design/development process, securing and preparing the application for cloud deployment.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Future Features

In no particular order: 

- Implement a recommendation system that suggests books based on the user's reading history, preferences, and ratings. 
- Allow users to follow other users, share books on their digital shelves, and comment on/review books. 
- Create partnerships and APIs to allow users to check the availability of physical copies in local libraries or bookstores, and possibly even reserve or purchase them directly through ScrollStack
- Allow users to personalize their dashboard views with widgets or sections that matter most to them, such as recent reads, recommendations, or friend activity 

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## User Experience Design

### Strategy

The ScrollStack project is envisioned as a digital bookshelf that provides a platform for users to manage their book collections. The strategy behind this project is to leverage Full-Stack development techniques to create a user-friendly, mobile-first MVP (Minimum Viable Product) that not only meets the basic CRUD (Create, Read, Update, Delete) functionalities for book management but also incorporates authentication, profile management, searching, filtering, and responsive design. This strategy is rooted in the Agile methodology to ensure flexibility, iterative development, and user feedback incorporation throughout the project lifecycle.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Scope

To achieve our strategy, the project's scope includes:

- Developing a responsive and accessible front-end design that adheres to UX principles and accessibility guidelines.
- Implementing CRUD functionality for book management.
- Ensuring secure user authentication and authorization.
- Offering searching and filtering capabilities to enhance user interaction.
- Providing a user-friendly profile management interface.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Structure

ScrollStack is structured around a series of epics and user stories that detail the development process and features to be implemented. Each epic encompasses a broad area of functionality, such as Project Setup, Model Related Development, User Authentication, and Book Management. Within these epics, user stories break down the development tasks into manageable units, ensuring a focused and user-centered approach. The application follows a logical flow to facilitate ease of use and intuitive navigation, supporting these actions through a clear, organized database and front-end design. This structure supports the Agile methodology by allowing for adaptability and iterative improvements based on user feedback and project requirements.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Skeleton

The skeleton of ScrollStack is defined through wireframes and ERDs (Entity-Relationship Diagrams) that outline the user interface and database design. Wireframes provide a visual guide for the layout of web pages, focusing on user experience and efficient navigation. ERDs detail the database schema, illustrating the relationships between different data models such as Book, Genre, and Author. This skeletal framework serves as the blueprint for developing a structured and well-organized application that meets both functional and aesthetic requirements.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Frontend Design

### Wireframes

Wireframes for the ScrollStack project were created to outline the basic layout and interface elements for the core pages. These wireframes are the blueprint for developing a responsive and accessible web interface, adhering to the principles of mobile-first design.

- Home/Landing Page: Showcasing featured books and user testimonials.
- Book List Page: Displaying all books with options to filter and search.
- Book Detail Page: Providing detailed information about a book with options to edit or delete.
- User Profile Page: Allowing users to view and edit their profile information.
- Authentication Pages: Including sign-up and log-in forms.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   
### Color Scheme

The site begin with #F6E84B, a luminous shade of yellow, evoking the brightness and energy of the first rays of dawn, sparking curiosity right at the top of our interface. As the gradient flows into #ff9102, a vivid orange akin to the morning sun's warm glow, it subtly encourages the user to remain engaged and interact with the content. The gradient culminates in a deep maroon (#800000), grounding the design with a sense of depth and seriousness, reflecting the solid foundation of the knowledge within.

This choice of gradient not only provides a striking backdrop but also supports the user's visual flow from the top of the page to the bottom, naturally guiding them through the content. The color transition from light to dark symbolizes the user's progression from initial curiosity to deeper engagement with our application. The goal is to make this transition as smooth and natural as reading a page, ensuring that the users' experiences are both visually appealing and emotionally resonant.

![Colour palette](/documentation/readme-img/colour-scheme.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Fonts

Roboto was chosen from [Google Fonts](https://fonts.google.com/specimen/Roboto?preview.text=The%20ScrollStack%20&query=roboto) as the font for this website. It is simple, easy to read and appropriate for a professional site.

![font](/documentation/readme-img/roboto-400.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Imagery

Images used on this website have been sourced from free online resources, either generated by AI technology or obtained from Wikimedia Commons. Each image has been carefully selected to enhance the content and provide a visually engaging experience for our visitors.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*  

### Accessibility Features

While developing the website, I've focused on its accessibility. This goal was achieved through the following methods:

- Using semantic HTML.
- Using a hover state on all buttons on the site to make it clear to the user if they are hovering over a button.
- Choosing a sans serif font for the site - these fonts are suitable for people with dyslexia.
- The use of aria-labelledby and attributes in the game's buttons and player sections improves the accessibility of dynamic content and interactive elements for users with screen readers.
- The use of colors is considered for visibility.
- No contrast errors were detected in the page;

  ![x](#IMAGE)

    - For more details pls see:
        - [Wave Web Accessibility Evaulation Tool - AAA.HTML](#)
        - [Wave Web Accessibility Evaulation Tool - BBB.HTML](#)
        - [Wave Web Accessibility Evaulation Tool - CCC.HTML](#) 

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Responsiveness

The website shown on a variety of screen sizes ![x](https://ui.dev/amiresponsive?url=https://github.com/JaqiKal/ScrollStack)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Navigation and Page Layouts

### Landing Page

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Registration & Login

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### User Profile

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Book Management

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Administration Panel

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Logout

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing and trouble shooting carried out.

### Documented Bugs and Fixes

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Deployment

<details id="prerequisites">
<summary style="font-size: 1.2em; font-weight: bold;">Prerequisites</summary>


- Ensure [Python](https://www.python.org/) is installed on your system.
- Verify that Python is installed on your system by checking its version. This can be done through a command in the terminal `python --version` or by running a small piece of Python code that outputs the version information.
- For installing libraries and modules, use `pip` or `pip3` depending on your Python version.

Important points for before deployment:
- The requirements for the project were added to a requirements.txt file using the command 'pip3 freeze > requirements.txt' in the terminal.
-  In .gitignore, include env.py to ensure sensitive information is not pushed to GitHub. 
-  In settings.py, link SECRET_KEY to the env.py file where the secret key variable is defined.
-  In settings.py, set 'DEBUG = False' to prevent verbose error pages and to prevent Django serving static files itself instead of relying on Cloudinary.
-  It is necessary to make migrations and migrate the models to the database before deployment.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

<details id="heroku-deployment">
<summary style="font-size: 1.2em; font-weight: bold;">Heroku Deployment</summary>

<br>

1. **Heroku Account:**
   - Make sure you have a Heroku account. If not, sign up on the Heroku website.
   
2. **GitHub Repository:**
   - Ensure your project is hosted on GitHub.
   
3. **Heroku Dashboard:**
   - Log in to your Heroku account and go to the Heroku Dashboard.
   
4. **Create a New App:**
   - On the dashboard, click `New` and choose `Create new app`.
   
5. **App Name:**
   - Choose a unique name for your app, it cannot be the same as this app.
   
6. **Region & Create App:**
   - Choose a region closest to you (EU or USA), then Select **Create App**

7.  **The page of your project opens.**

8.  **Heroku Postgres**
    - Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. **New App**
   - From the new app choose **Settings**, goto section 'Config Vars' click **Reveal Config Vars**, 
   
    - Config Vars for development of this project:
        - DATABASE_URL will be added automatically
        - SECRET_KEY - the django secret key can be generated here.
        - PORT = 8000
        - DISABLE_COLLECTSTATIC = 1
        - CLOUDINARY_URL can be obtained from cloudinary follow the steps on the website to register.
        - Google API key can be obtained here. Wou have to register with google and create new app to get the API key. Follow the instructions on the website.
        - Email host password (if any).
   
    - **Confidential credentials**
        - If one needs to use any private credentials, like CREDS.JSON, you should also add them to the Config Variables section. This is a crucial step for maintaining the security and integrity of your application, especially when it interacts with external services or APIs that require authentication. 

    - Config Vars for production:
        - DATABASE_URL
        - SECRET_KEY
        - CLOUDINARY_URL

**=> Go back to your code**

10. **Procfile**
    - Add the Procfile to your application's root directory ```echo web: node index.js > Procfile```. Heroku relies on this file to determine how to run your application, ensuring the correct setup of your web server. Use commands like `web: gunicorn PROJ_NAME.wsgi` in the Procfile to instruct Heroku on starting your web server with Gunicorn

11. In settings in your app add Heroku to ALLOWED_HOSTS

12. Add and commit the changes in your code and push to github

13. **Add Buildpack**
   - Scroll further down on the page, select **Add Buildpack**. The buildpacks will install further dependencies that are not included in the 'requirements.txt'. 
   - It's crucial to arrange the build packs correctly! First, choose Python and then Node.js. If they're not in this sequence, you can reorder them by dragging.
   
14. **Deploy**
    - From the tab above select the 'deploy section'.

15. **GitHub**
    - For deploying this project, we're using GitHub as our method. After choosing GitHub, make sure to confirm the connection. Then, search for your repository name and once Heroku finds your repository - click "connect"

16. **Choose deploy method**
    - Scroll down to the section "Automatic Deploys". 
    - Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy.
    - Click "Deploy branch" wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed. 
    - Click the button "View" to see the app.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

<details id="local-deployment>
<summary style="font-size: 1.2em; font-weight: bold;">Local Deployment</summary>

<br>
#### How to Fork

1. Log in (or sign up) to Github.
2. Go to the [repository](https://github.com/JaqiKal/ScrollStack) for this project, 
3. Click the Fork button in the top right corner and select create a fork.
4. One can change the name of the fork and add description
5. Choose to copy only the main branch or all branches to the new fork.
6. Click Create a Fork. A repository should appear in your GitHub

#### How to Clone

1. Log in (or sign up) to GitHub.
2. Go to the [repository](https://github.com/JaqiKal/ScrollStack) for this project, 
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor or open command-line interface on your computer and change the current working directory to the location you want to use for the cloned directory. 
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
    - `$ git clone https://github.com/JaqiKal/ScrollStack`
6. Press Enter. Your local clone will be created.

#### Setting up your local environment

1. Create Virtual environment on your computer or use gitpod built in virtual environment feature.
2. Create .env file. Place in inside ScrollStack folder. It needs to contain the variables from step 9.
- Database URL can be obtained from XXX app, add PostgreSQL as an add-on when creating an app.
- Secret_key - is the django secret key can be generated here.
- Google API key can be obtained here you will have to register with google and create new app to get the API key. Follow the instructions on the website.

```text
DATABASE_URL = ...
SECRET_KEY = ...
GOOGLE_API_KEY = ...
DEVELOPMENT = True
```
3. Run command
``` pip3 install -r requirements.txt ```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

## Credits and Acknowledgements

### Code

```txt
T.B.D.!
```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Media

Media were not used.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Content

Website content crafted by the developer for personalized, authentic information.

The following documentation, blogs, tutorials and guides were used to aid development.
- Bootstrap documentation
- [Django documentation](https://docs.djangoproject.com/en/5.0/)
- x

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Acknowledgements

I would like to thank! 

- [The Literature Map](https://www.literature-map.com/): A valuable resource provided by Gnod, the Global Network of Discovery.
- The whole team at [Code Institute Slack community](https://code-institute-room.slack.com) for their teaching and support.
- To all engaged fellow students at all channels and a special shout out to slack channel [community sweden](https://app.slack.com/client/T0L30B202/C03J2BCURV3).
- [Kera Cudmore](https://github.com/kera-cudmore) for her excellent readme example.
- My mentor [Jubril Akolade](https://github.com/jubrillionaire/)
- My immediate and extended family, as well as my friends, who support and cheer me on!

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   
