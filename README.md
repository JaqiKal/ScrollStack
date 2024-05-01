# Welcome to the ScrollStack

Ever wished your personal library could be as organized and accessible as your favorite bookstore? 
Welcome to ScrollStack, where your digital bookshelf comes to life, effortlessly organized and accessible from anywhere at any time.

This is a web application designed to transform the way users manage their personal libraries. Tailored for book enthusiasts, students, researchers, minimalists, and anyone in between, it provides a user-friendly and efficient solution for cataloging, organizing, and accessing book collections digitally.

In a world where space is a premium and the ease of accessing information is paramount. The ScrollStack stands out as a digital haven for books. Whether users are tracking their reading habits,decluttering their physical space, or simply organizing their vast collection of literature. This platform caters to their needs. It allows for the addition, editing, categorization, and detailed viewing of each book in their personal collection.

Developed with the user in mind, this application aims to enhance the reading experience, making personal libraries accessible at the click of a button, anywhere, anytime. Dive into a world where managing books is no longer a chore but a delightful experience.


![ScrollStack Preview](/documentation/readme-img/)

Developer: [JaqiKal](https://github.com/JaqiKal)<br>
Deployed website: [Link to website](#)<br>

---

# Table of Contents

- [Introduction](#introduction)
    - [Project Overview](#project-overview)
    - [Objectives](#objectives)
    - [Developer Goals](#developer-goals)
    - [User Goals](#user-goals)
- [Learning Outcomes and Skill Development](#learning-outcomes-and-skill-development)
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
    - <a href="#overview-of-agile-methodology">Epics and User Stories</a>
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

ScrollStack is a Full-Stack application that redefines personal library management. Using advanced web technologies, it enable users to maintain an organized digital bookshelf, accessible anywhere, anytime.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Objectives

The primary objective is to provide an intuitive, responsive platform that simplifies book management. This digital solution aims to meet the needs of readers by offering functionalities like book categorization and easy access to a vast literature collection.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Developer Goals

As developers, the goal is to craft a robust, scalable application using the Django framework. This project demonstrates their proficiency in Full-Stack development, emphasizing clean, maintainable code and efficient database usage.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### User Goals

For its users, ScrollStack aims to be a reliable, user-friendly tool that makes book management a pleasure rather than a chore. It caters to readers seeking a minimalist approach to organize and access their books with ease.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Learning Outcomes and Skill Development

The fundamental ambition of this project is to enhance my knowledge in contemporary web development through the practical application of the Django framework. 
The objectives are multifaceted:

- To comprehend  the principles of Full-Stack development and demonstrate the ability to create a feature-rich web application from the ground up.
- To enhance my proficiency in front-end technologies, ensuring the creation of an intuitive and responsive user interface that adheres to the principles of user-centered design.
- To refine my back-end development skills, especially with respect to database design and management, user authentication, and server-side logic.
- To understand the principles of Agile development methodology, allowing for a flexible design process that can adapt to user feedback and changing requirements.

The competencies developed through this project are intended not just to satisfy the criteria for a successful course completion, but to lay a robust foundation for future endeavors in the field of web development.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*


## Technologies Used

### Programming Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) - is used to structure the content of the application.
- [CSS](https://en.wikipedia.org/wiki/CSS) - is applied to style the application, enhancing the user interface..
- [JavaScript](https://sv.wikipedia.org/wiki/Javascript) - adds interactivity to web pages, improving the user experience.
- [Python](https://www.python.org) - serves as the back-end programming language.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Frameworks and Libraries

- [Django](https://www.djangoproject.com/) - a framework for developing web applications written in Python, structures the back-end functionality.
- [Bootstrap](https://getbootstrap.com/) - a front-end framework, is used to help developers build responsive and mobile-first websites and web applications. It provides a collection of CSS and JavaScript tools for creating layouts, forms, buttons, navigation, and other interface components. 
- [Cloudinary](https://cloudinary.com/) -  cloud-based platform, is used for storing and serving images, enhancing media management in the application.
- [os](https://www.geeksforgeeks.org/os-module-python-examples/?ref=lbp) - The OS module in Python provides functions for interacting with the operating system.
- [datetime](https://docs.python.org/3/library/datetime.html) - supplies classes to work with date and time
- [psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter for the Python programming language
- [dj-database-url](https://pypi.org/project/dj-database-url/) - enables the ability to represent their database settings via a string
- [gunicorn](https://gunicorn.org/) - handles HTML rendering, authentication, administration, and backend logic
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) - allows web app to serve its own static files
- [django-Allauth](https://docs.allauth.org/en/latest/) - addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - controls the rendering behavior of Django forms
- [crispy-bootstrap](https://pypi.org/project/crispy-bootstrap5/) - enables crispy forms to use bootstrap for styling
- [Pillow](https://pypi.org/project/pillow/) image resizing, rotation and transformation

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Database

-  [PostgreSQL](https://dbs.ci-dbs.net/) - provided by the Code Institute, is employed as the database system for its robustness and compatibility with Django.

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
- [Github](https://github.com/) - Essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
- [Google Dev Tools](https://developers.google.com/web/tools) - used during testing, debugging and styling.
- [Google Fonts](https://fonts.google.com/) - A catalog of free, open-source fonts. Used for typography.
- [Heroku](https://www.heroku.com)- A platform for deploying and hosting web applications. 
- [Look](https:www.looka.com)  - For the logo and symbol
- [Lucidchart](https://www.lucidchart.com) - Used for ERD (entity relationship diagram) 
- [Markup Validation Service](https://validator.w3.org/) - Used to check code ensuring that my HTML is error-free and adheres to the latest web standards.
- [PEP8](https://peps.python.org/pep-0008/)- Style Guide for Python Code.
- [PostgreSQL](https://www.postgresql.org/) - Is a powerful, open source object-relational database system.
- [Shields.io](https://shields.io/) - To add badges to the README.
- [Tiny PNG](https://tinypng.com/) - To compress images.
- [UXwing](https://uxwing.com/) - Provider of free icons free for commercial use.
- [Wave](https://wave.webaim.org) - WAVE® is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities.
- [Web Disability Sim](https://chromewebstore.google.com/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) - a google chrome extension that allows you to view your site as people with accessibility needs would see it.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details>

## System Architecture

### Application Structure

ScrollStack is structured around the Model-View-Controller (MVC) pattern, which separates the application into three interconnected components. This separation helps manage complex development and enables efficient teamwork by segmenting the app into manageable parts.

The frontend is built using HTML, CSS and JavaScript to create a mobile-first, responsive design. Bootstrap is chosen for its comprehensive library of pre-styled components and responsive grid system, which accelerated the development process and ensured a seamless, mobile-first user experience across different devices.

The backend architecture is built on Python and Django. Where Django simplifies the application's backend logic, manages URL routing, and ensures efficient database interactions. Providing a stable and efficient backbone for the app's operations.

In this project, a relational database 'PostgreSQL' is employed for its robustness, scalability, and compatibility with Django. Structuring it to store user and book information in an organized manner. Which optimizes data retrieval and supports complex queries efficiently.

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
The application utilizes various programming paradigms including:
- Object orientated programming
- Procedural programming
- Event-driven Programming
```

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Agile Development Process

### Overview of Agile Methodology

Agile methodologies and principles guide the planning and creation of ScrollStack. While not adhering strictly to traditional Agile methodologies, such as scheduled sprints or scrums. The development process is inspired by Agile principles, focusing on flexibility, continuous improvement, and rapid adaptation to change. I don't use sprints as my project benefits more from focusing directly on larger goals and milestones, which are already well-defined with clear start and end dates. The approach is straightforward, development of features in a logical sequence, addressing core functionalities first before expanding to more complex features.

When encountering bugs or issues, rather than halting development, these are recorded as bug issues and added to the backlog. This allows to continue progressing in other areas while periodically revisiting and prioritizing the backlog based on severity and impact. This method ensures that development momentum is maintained while systematically addressing and resolving issues.

Feedback from users are actively sought and analyzed to identify areas for improvement, ensuring that the product continuously evolves to meet the needs and expectations of its users effectively.

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

<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### MoSCoW Prioritization

Labels were added to user stories to assist with prioritization of tasks. The MoSCoW system involves adding labels for MUST HAVE, SHOULD HAVE, COULD HAVE and WON'T HAVE. This method assists in ensuring that essential features are completed first, optimizing resource allocation and meeting critical deadlines.

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10) and/or [Issues list](https://github.com/JaqiKal/ScrollStack/issues)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Project Tracking (GitHub Projects)

ScrollStack employs a Kanban board for project tracking, organizing tasks into categories such as Backlog, In Progress, and Done. This dynamic document is continually managed to prioritize and organize the workload effectively, ensuring a flexible and responsive development process.

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

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

**Relationships**

- AdminPanel_Django to User_Django_AllAuth
    - **Many to One**: The AdminPanel_Django entity records actions taken within the Django admin panel, such as log entries or administrative changes. Each log or action entry is associated with exactly one user from the User_Django_AllAuth entity, which holds the authentication and authorization information.
    - In the ERD, this relationship is indicated by a line with a crow's foot at the AdminPanel_Django end, pointing towards the User_Django_AllAuth, showing that each action is tied to a single user, while a user can have many logged actions.

- User_Django_AllAuth to Book
    - **One to Many**: A `User` can have multiple `Books`, but each `Book` is associated with exactly one `User`.
    - This is represented by the crow's foot notation at the `Book` end of the connector, and a single line at the `User_Django_AllAuth` end.

- Book to Genre
    - **Many to One**: Each `Book` is associated with exactly one `Genre`, but a `Genre` can include many `Books`.  
    - The line has a crow's foot at the `Book` end, pointing towards the `Genre`, indicating the many side of the relationship.

- Book to Author (through BookAuthor)
    - **Many to Many**: A `Book` can have multiple `Authors`, and an `Author` can write multiple `Books`. This is represented by a join table, `BookAuthor`.
    - Since ERD diagrams typically do not directly show Many-to-Many relationships without a join table, the diagram shows two One-to-Many relationships instead: 
        - One from `Book` to `BookAuthor`
        - One from `Author` to `BookAuthor`
    - Each of these is depicted with a crow's foot at the `BookAuthor` end of the connectors.

**Permissions and Roles**

The is_superuser field within the User_Django_AllAuth entity indicates whether a user is a superuser. Superusers are granted all permissions across the application without explicitly assigning them. This allows them to perform any operation in the Django admin panel and access all data. Regular users, lacking the is_superuser flag, are restricted to actions within their scope, typically only able to manipulate their own data as defined by the application's permission logic.


![ERD](/documentation/readme-img/erd-scroll-stack-transp.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Database Schema

For ScrollStack, PostgreSQL is adopted for its advanced capabilities and flexibility in handling datasets, it is a PostgreSQL provided by Code Institute. This relational database supports essential features for our digital bookshelf, including book CRUD operations. The structure features entities like Book and User, with a one-to-many relationship from User to Books indicating ownership. Data integrity is enforced through constraints, such as foreign keys and NOT NULL, ensuring reliability and well-organized data that underpins ScrollStack's seamless functionality. 

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Data Flow and Architecture

ScrollStack leverages the MVC (Model-View-Controller) architecture to optimize the flow of data between the user interface and the database, ensuring a dynamic and responsive experience. The process works as follows:

- When a user performs an action, such as adding a book, the request is handled by the Controller. 
- The Controller then interfaces with the Model to perform database operations. 
- Upon successful database update, the Model signals the Controller, which instructs the View to update the display accordingly—showing the latest book list without needing a page reload.

This setup is made efficient through the use of AJAX<sup>1)</sup>, enabling asynchronous data updates that enhance user interaction. Middleware plays a critical role in routing requests, authentication, and overall data management. The MVC framework, together with AJAX and middleware<sup>2)</sup>, allows ScrollStack to provide quick and seamless updates to the user interface, facilitating a better user experience and streamlined maintenance.

<sup>1)</sup>AJAX is built into the web development environment through JavaScript and does not require external installation. It's readily available for use in creating dynamic, interactive web applications."

 <sup>2)</sup>Middleware in the context of web development acts as a bridge between the client and server, managing requests and responses, and performing various tasks such as authentication, authorization, routing, session management, error handling, data processing, logging, monitoring, and CORS (Cross-Origin Resource Sharing) management.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Features

### Current Features

#### Navigation 

![x]()


- The navigation bar is consistent across all pages, with slight modifications based on the context of the user's session status (e.g., whether the user is logged in or not). 
    - For Non-Logged-In Users: Landing Page/Logo, Contact, Register, Login
    - For Logged-In Users: Landing Page/Logo, My Books, Add Book, Contact, Logout

- Common elements across all pages
    - Logo/Home: Clicking this should always take the user back to the landing page.
    - Contact: Link to the contact page where users can find ways to reach out or get support.

- Dynamic Elements Based on User State
    - Register/Login: Visible only when the user is not logged in. These should redirect to their respective pages for authentication.
    - Logout: Visible only when the user is logged in, allowing users to log out of the application.

- Specific to Logged-in Users
    - My Books: Leads to the book details page where users can view all their books. This should be visible only when the user is logged in.
    - Add Book: Link to the Add page where users can fill out the form to add a new book. Visible only for logged-in users. 

- Error Pages: Navigation is simple. Only the Home, Contact are included and depending on user status, Login or Logout options. 

#### Landing Page

![x]()

#### User account pages

![x]()

The Django templates for SignUp, Login, and Logout have been customized and styled to align with the overall aesthetic of the application.
- Register allows users to create a new account. After clicking to establish their account, users are redirected to 'Add a book'. 
- Login in grants users access to their content. If a user doesn't have an account yet, an active link on the Login page allows them to navigate to the Register page.
- Logout process is handled through a simple logout button or link in the navigation menu. When clicked, this button triggers the logout functionality, and then redirects the user to the landing page.

#### Books List and Details page
This page serves as the digital equivalent of a user's personal bookshelf or library.
- Responsive Book Cards: Each book is displayed on a responsive card that adjusts to screen size.
- CRUD Operations: Options to add, update, and delete books are integrated into each card.
- Form Navigation: Adding or updating a book redirects the user to a form page, streamlining list management.
- Deletion Confirmation: A confirmation pop-up ensures intentional deletions. Confirming deletion redirects the user to the landing page.

![x]()

#### Contact page
This page offers a straightforward method for users to contact the site owner.
- Upon submitting feedback, users will receive a confirmation message, acknowledging their input.

![x]()

#### Error page
The site features error handling for Error 403 (Forbidden Page View), Error 404 (Page Not Found), and Error 500 (Internal Server Error). When one of these errors occurs, a custom message specific to the error is displayed, offering the user an option to navigate back.

![x]()

#### Footer

- Links to social media; Facebook, Youtube and Instagram
- Hovering over the icons, will change their color respectively to their original color
- Clicking on them, will open the respective site in a new tab

![x]()


*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Future Features

In no particular order: 

- Implement a recommendation system that suggests books based on the user's reading history, preferences, and ratings. 
- Allow users to follow other users, share books on their digital shelves, and comment on/review books. 
- Create partnerships and APIs to allow users to check the availability of physical copies in local libraries or bookstores, and possibly even reserve or purchase them directly through ScrollStack.
- Allow users to personalize their dashboard views with widgets or sections that matter most to them, such as recent reads, recommendations, or friend activity .
- Integrate features to track users' reading habits, such as time spent reading, pages read per session, and completion dates for books. 
- Implement functionality for users to mark their current reading status for each book (e.g., not started, in progress, completed) and save their progress by page number or chapter.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## User Experience Design

### Strategy

The ScrollStack project is envisioned as a digital bookshelf that provides a platform for users to manage their book collections. The strategy behind this project is to leverage Full-Stack development techniques to create a user-friendly, mobile-first MVP (Minimum Viable Product) that meets the basic CRUD (Create, Read, Update, Delete) functionalities for book management. It also incorporates authentication, profile management and responsive design. This strategy is rooted in the Agile methodology to ensure flexibility, iterative development, and user feedback incorporation throughout the project lifecycle.

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

ScrollStack is structured around a series of epics and user stories that detail the development process and features to be implemented. Each epic encompasses a broad area of functionality, such as Project Setup, Model Related Development, User Authentication, and Book Management. Within these epics, user stories break down the development tasks into manageable units, ensuring a focused and user-centered approach. The application follows a logical flow to facilitate ease of use and intuitive navigation, supporting these actions through a clear, organized database and front-end design.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Skeleton

The skeleton of ScrollStack is defined through wireframes and Entity-Relationship Diagrams (ERDs) that outline the user interface and database design. Wireframes provide a visual guide for the layout of web pages, focusing on user experience and efficient navigation. ERDs detail the database schema, illustrating the relationships between different data models such as Book, Genre, and Author. This skeletal framework serves as the blueprint for developing a structured and well-organized application that meets both functional and aesthetic requirements.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Frontend Design

<details id="wireframes">
<summary style="font-size: 1.2em; font-weight: bold;">Wireframes</summary>

Wireframes for the ScrollStack project were created to outline the basic layout and interface elements for the core pages. These wireframes are the blueprint for developing a responsive and accessible web interface, adhering to the principles of mobile-first design.

- Landing Page: Simple start page, user can register or login

![x](/documentation/wireframes/wireframe-landing.webp)

- Home Page and Book List and detail Page: Displaying all books with options to search. Providing detailed information about a book with options to edit or delete

![x](/documentation/wireframes/wireframe-detail.webp)

- Add book page: A form 

![x](/documentation/wireframes/wireframe-create.webp)

- Edit book page: A form 

![x](/documentation/wireframes/wireframe-update.webp)

- Contact Page:  A form where one can send feed-back.

![x](/documentation/wireframes/wireframe-contact.webp)

- User Profile Page: Allowing users to view and edit their profile information.

![x]()

- Authentication Pages: Including sign-up and log-in forms.

![x](/documentation/wireframes/wireframe-register.webp)

![x](/documentation/wireframes/wireframe-login.webp)

- Error page:  Page not found, Page forbidden, Server error

![x](/documentation/wireframes/wireframe-error.webp)


*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

</details><br>

### Color Scheme

The color scheme uses a gradient starting with #F6E84B, a luminous shade of yellow, evoking the brightness and energy of the first rays of dawn, sparking curiosity right at the top of our interface. As the gradient flows into #ff9102, a vivid orange akin to the morning sun's warm glow, it subtly encourages the user to remain engaged and interact with the content. The gradient culminates in a deep maroon (#800000), grounding the design with a sense of depth and seriousness, reflecting the solid foundation of the knowledge within.

This choice of gradient not only provides a striking backdrop but also supports the user's visual flow from the top of the page to the bottom, naturally guiding them through the content. The color transition from light to dark symbolizes the user's progression from initial curiosity to deeper engagement with our application. The goal is to make this transition as smooth and natural as reading a page, ensuring that the users' experiences are both visually appealing and emotionally resonant.

![Colour palette](/documentation/readme-img/colour-scheme.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Fonts

Roboto sourced from [Google Fonts](https://fonts.google.com/specimen/Roboto?preview.text=The%20ScrollStack%20&query=roboto) is chosen for its readability and professional appearance, suitable for a diverse audience.

![font](/documentation/readme-img/roboto-400.webp)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Imagery

Images on the site includes AI-generated images and those sourced from Wikimedia Commons, selected to enhance the content and provide a visually engaging experience for users.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*  

### Accessibility Features

Accessibility is a priority, achieved through semantic HTML, appropriate use of colors, and responsive design features. These elements ensure the website is accessible to users with various disabilities.

  ![x](#IMAGE)

    - For more details pls see:
        - [Wave Web Accessibility Evaulation Tool - AAA.HTML](#)
        - [Wave Web Accessibility Evaulation Tool - BBB.HTML](#)
        - [Wave Web Accessibility Evaulation Tool - CCC.HTML](#) 

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Responsiveness

The website's design is responsive, tested across multiple devices to ensure a consistent and user-friendly experience regardless of device size. ![x](https://ui.dev/amiresponsive?url=https://github.com/JaqiKal/ScrollStack)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Testing

This section of the README details all testing activities and documents any bugs encountered during development, along with their resolutions. It ensures transparency and ongoing improvement of the application

Please refer to [TESTING.md](/TESTING.md) for details.

### Documented Bugs and Fixes

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

## Deployment

<details id="prerequisites">
<summary style="font-size: 1.2em; font-weight: bold;">Prerequisites</summary>

Ensure that Python and pip (Python's package installer) are installed on your system. These tools are necessary for setting up the local development environment. The process works as follows:

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

<details id="local-deployment">
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

### Media

This project uses third-party assets that require attribution:
- The site logo is provided by [Vecteezy](https://www.vecteezy.com/free-vector/open-book). The [image](https://www.vecteezy.com/vector-art/4911390-book-icon-template-black-color-editable-book-icon-symbol-flat-vector-illustration-for-graphic-and-web-design) itself. These vectors are used under the terms of their license which requires public attribution. For more details on the licensing, please visit the provider's website.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*   

### Content

Throughout the development of ScrollStack, a variety of resources have been utilized to ensure the platform is robust, user-friendly, and engaging. Below is a list of key documentation, blogs, tutorials, and guides that have been instrumental in crafting the features and functionality of ScrollStack:

- **Bootstrap**: Extensively used for styling and responsive design, making the site accessible on a variety of devices - [Bootstrap documentation](https://getbootstrap.com/).
- **Django**: As the backbone of our platform, Django's comprehensive documentation has been crucial for backend development - [Django documentation](https://docs.djangoproject.com/en/5.0/).
- **MDN Server-side website programming**:(https://developer.mozilla.org/en-US/docs/Learn/Server-side) -  how to set up a development environment, and how to start using it to create your own web applications.
- **django-allauth**: Implemented for authentication processes; setup guidance was followed from both the official documentation and additional tutorials provided by Code Institute's PP4 blog walkthrough - [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html) - 
- **django-richtextfield**: Integrated into the book model to enhance content creation with rich text capabilities - [django-richtextfield](https://pypi.org/project/django-richtextfield/).
- **Inspiration for Forms**: In ScrollStack, the BookForm utilizes Django's form and Meta options to efficiently manage book data, ensuring fields are defined for user input and Meta class attributes are properly configured.
    - [125. Form To Add Books in Django](https://youtu.be/StOth98gHHw?si=Asy57HYhEwZIX5yy)
    - [126. 125. Form To Add Books Part -2](https://youtu.be/z98z_8ihqew?si=4j2ElUhSVi86NCDG)
    - [Django Tutorial Part 9: Working with forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
    - [django doc, working with forms](https://docs.djangoproject.com/en/5.0/topics/forms/)
    - [Building Django forms with django-crispy-forms](https://youtu.be/MZwKoi0wu2Q?si=jOYV4S3nGU1oCu7c)
    - [Style Django Forms With Bootstrap - Django Blog #5](https://youtu.be/6-XXvUENY_8?si=m-Ck3ucJ20ReV1Sp)
    - [Django Meta options](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options)  
    - [Override the save() method in Django ModelForm to create or update](https://stackoverflow.com/questions/45923410/override-the-save-method-in-django-modelform-to-create-or-update)
- **Style Hamburger toggler**: [Change Hamburger-Icon, by richards](https://forum.bootstrapstudio.io/t/change-hamburger-icon/8990/2?fbclid=IwAR17UiU_5vC8sNPMZ6ZOLTAfHd5jDoKYJcOY2QogODhdRuw42l2XpcmjHTA)
- **User profile setup:** is amended from: [Django - User Profile](https://dev.to/earthcomfy/django-user-profile-3hik)
- **Sources of inspiration and guidance in general**:
    - The Django Recipe Sharing Tutorial series by Dee Mc - [Django Recipe Sharing Tutorial series](https://www.youtube.com/@IonaFrisbee).
    - [Django Tutorial](https://youtu.be/n-FTlQ7Djqc?si=Hfm94TiD4vbWolwj) by Net Ninja.


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
