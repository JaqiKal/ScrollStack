# Welcome to the ScrollStack

This is your personal book register, a web application designed to transform the way you manage your personal library. Tailored for book enthusiasts, students, researchers, minimalists, and anyone in between, this platform provides a user-friendly and efficient solution for cataloging, organizing, and accessing your book collection digitally.

In a world where space is a premium and the ease of accessing information is paramount, the ScrollStack stands out as a digital haven for your books. Whether you're tracking your reading habits, decluttering your physical space, or simply organizing your vast collection of literature, this platform caters to your needs. It allows for the addition, editing, categorization, and detailed viewing of each book in your personal collection.

Developed with the user in mind, this application aims to enhance your reading experience, making your personal library accessible at the click of a button, anywhere, anytime. Dive into a world where managing your books is no longer a chore but a delightful experience.


![ScrollStack Preview](/documentation/readme-img/placeholder.webp)

Developer: [JaqiKal](https://github.com/JaqiKal)<br>
Deployed website: [Link to website](#)<br>

---

# Table of Contents

- Introduction
    - Project Overview
    - Objectives
    - Developer Goals
    - User Goals
- Technologies Used
    - Programming Languages
    - Frameworks and Libraries
    - Database
    - Tools and Services
- System Architecture
    - Application Structure
    - Backend Logic
    - Programming Paradigms
- Agile Development Process
    - Overview of Agile Methodology
    - Epics and User Stories
    - MoSCoW Prioritization
    - Project Tracking (GitHub Projects)
- Data Modeling and Database Design
    - Entity-Relationship Diagram (ERD)
    - Database Schema
    - Data Flow and Architecture
- Features
    - Current Features
    - Future Features
- User Experience Design
    - Strategy
    - Scope
    - Structure
    - Skeleton
         - Wireframes
- Frontend Design
    - Color Scheme
    - Accessibility Features
    - Responsiveness
- Navigation and Page Layouts
    - Landing Page
    - Registration & Login
    - User Profile
    - Book Management
    - Administration Panel
    - Logout
- Testing
    - Documented Bugs and Fixes
- Setup and Installation
    - Prerequisites
    - Local Development Setup
    - Cloning and Forking Instructions
    - Dependencies and Environment Setup
- Deployment
    - Prerequisites
    - Heroku Deployment
    - Local Deployment
        - How to Fork
        - How to clone
        - Setting up your local environment
- Credits and Acknowledgements
    - Code
    - Media
    - Content
    - Acknowledgements


## Introduction

### Project Overview

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Objectives

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Developer Goals

*<span style="color: blue;">[Back to Content](#content)</span>*   

### User Goals

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Technologies Used

### Programming Languages

- HTML : Structure the content of our application.
- CSS : Style the application to enhance the user interface.
- JavaScript : Add interactivity to web pages, improving the user experience.
- Python : Backend development 

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Frameworks and Libraries

- Django - a framework for developing web applications written in Python.
- Bootstrap - a front-end framework designed to help developers build responsive and mobile-first websites and web applications. It provides a collection of CSS and JavaScript tools for creating layouts, forms, buttons, navigation, and other interface components, as well as optional JavaScript extensions. 
- Cloudinary - a cloud-based platform for storing and serving images

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Database

-  [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/)

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Tools and Services

- Balsamiq Cloud:used for drawing wireframes
- cdnjs: content delivery network
- Code Institute Python Linter: a tool to check Python code against some of the style conventions in PEP8.
- Coolors: used for generating the colour palette.
- DB diagram: used for building an ER diagram.
- Draw.io: useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
- Favicon Generator: used for generating a favicon.
- Git: used for version control. (git add, git commit, git push)
- Gitpod: streamlines your development process by providing a pre-configured, cloud-based development environment that's instantly ready for coding.
- GitHub: essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
- Google Developer Tools: used during testing, debugging and styling.
- Google Fonts: a catalog of free, open-source fonts. Used for typography.
- Font Awesome: a catalog of free, open-source icons. Used for profile, heart and speech bubble icons.
- Heroku: a platform for deploying and hosting web applications.
- JSHint: a code validation tool used for JavaScript.
- Markup validation Service: Used to check code ensuring that my HTML is error-free and adheres to the latest web standards.
- PEP8: style Guide for Python Code.
- W3C Validator: code validation tool used for HTML and CSS.

*<span style="color: blue;">[Back to Content](#content)</span>*   

## System Architecture

### Application Structure

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Backend Logic

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Programming Paradigms

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Agile Development Process

### Overview of Agile Methodology

Agile methodologies and principles were used when planning and creating The ScrollStack. Development was organized by focusing on the prioritization of user story or stories. The user stories are arranged on a KanBan board, which was continuously managed throughout development to enable prioritization of the workload.

*<span style="color: blue;">[Back to Content](#content)</span>*   

<details>
<summary style="font-size: 1.2em; font-weight: bold;">Epics and User Stories</summary>

<br>

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10)
<br>

**EPIC: Initial Project Planning and Documentation**
- US: Review LO in PP4 Assessment Material
- US: Initiate and Continuously Update README File
- US: Structured Planning and Documentation Framework
- US: Prioritize User Stories
- US: Create Wireframe
- US: Create ERD 

**EPIC: Project Setup and Initial Configuration**
- US: GitHub Repository Setup
- US: IDE Setup

**EPIC: Model Related**
- US: Create Book Model
- US: Implement other applicable Models, eg. Genre and Author Models

**EPIC: User Authentication and Authorization**
- US: Sign Up for an Account
- US: Log In and Out of the Application
- US: Reset Forgotten Password

**EPIC: Book Management**
- US: Add New Books to Collection
- US: View List of Books
- US: Edit Book Details
- US: Delete a Book

**EPIC: Searching and Filtering**

- US: Search by Title or Author
- US: Filter by Genre

**EPIC: Profile Management**

- US: Update Profile Details
- US: Upload a Profile Picture

**EPIC: View Related**

- US: Develop Dashboard View

**EPIC: Template Related**

- US: Design Base Template
- US: Create Error Handling Template

**EPIC: Responsiveness and Accessibility**

- US: Ensure Website Responsiveness
- US: Follow Accessibility Best Practices

**EPIC: User Feedback**

- US: Implement Feedback and Issue Reporting Feature
- US: Provide User Access to Documentation and Help Guides

**EPIC: Testing and Quality Assurance**

- US: Write Unit Tests for the Book Model
- US: User Acceptance Testing on Mobile Devices
- US: Manually Test User Registration and Profile Management
- US: Perform Comprehensive Cross-Browser and Device Compatibility Testing

**EPIC: Deployment, Documentation**

- US: Document Deployment Process
- US: Secure Application for Deployment
- US: Prepare Application for Cloud Deployment
- US: Document Design and Development Process

*<span style="color: blue;">[Back to Content](#content)</span>*   

</details>

### MoSCoW Prioritization

Labels were added to user stories to assist with prioritization of tasks. The MoSCoW system involves adding labels for MUST HAVE, SHOULD HAVE, COULD HAVE and WON'T HAVE. By labelling issues in such a way, the developer can focus on completing all the MUST HAVE tasks before moving onto tasks of lower priority, this is critical when working to a tight deadline to ensure a minimum viable product is completed in time.

For details please follow link to: [Github Project board](https://github.com/users/JaqiKal/projects/10) and/or [Issues list](https://github.com/JaqiKal/ScrollStack/issues)

*<span style="color: blue;">[Back to Content](#content)</span>*

### Project Tracking (GitHub Projects)

The project use a Kanban board for organization, serving as a dynamic document continually managed to effectively prioritize and organize workload. The board categorized tasks into various stages, from Backlog for items not yet started to Done for completed tasks. As development commenced on a User Story, it transitioned from Backlog to In Progress, and upon completion, both the User Story and its associated Epic were moved to Done. Additionally, unresolved bugs were tracked separately until resolved, at which point they were also moved to the Done column. Kanban methodology proved invaluable in tracking project progress through its various phases, offering flexibility to adapt to the project's unique needs.

A link to the GitHub project board can be found [here](https://github.com/users/JaqiKal/projects/10).

| Kanban | Description |
|--|--|
| Backlog (EPIC, US) | Items not yet started|
| Ready to Start (EPIC, US) | Tasks ready for implementation |
| In Progress (EPIC) | Epic currently being worked on |
| In Progress (US) | User story currently being worked on |
| In Review | Tasks undergoing testing |
| BUG | Newly discovered and unresolved issues |
| Done | Completed tasks |
| Future Feature | Features planned for future enhancement beyond the minimum viable product (MVP), and not included by handover (2024-05-10)  |
| Won't have | Ideas considered but not included in the project scope |

*<span style="color: blue;">[Back to Content](#content)</span>*  

## Data Modeling and Database Design

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Entity-Relationship Diagram (ERD)

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Database Schema

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Data Flow and Architecture

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Features

### Current Features

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Future Features

*<span style="color: blue;">[Back to Content](#content)</span>*   

## User Experience Design

### Strategy

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Scope

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Structure

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Skeleton

*<span style="color: blue;">[Back to Content](#content)</span>*   

#### Wireframes

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Frontend Design

### Color Scheme

The site begin with #F6E84B, a luminous shade of yellow, evoking the brightness and energy of the first rays of dawn, sparking curiosity right at the top of our interface. As the gradient flows into #ff9102, a vivid orange akin to the morning sun's warm glow, it subtly encourages the user to remain engaged and interact with the content. The gradient culminates in a deep maroon (#800000), grounding the design with a sense of depth and seriousness, reflecting the solid foundation of the knowledge within.

This choice of gradient not only provides a striking backdrop but also supports the user's visual flow from the top of the page to the bottom, naturally guiding them through the content. The color transition from light to dark symbolizes the user's progression from initial curiosity to deeper engagement with our application. The goal is to make this transition as smooth and natural as reading a page, ensuring that the users' experiences are both visually appealing and emotionally resonant.

![Colour palette](/documentation/readme-img/colour-scheme.webp)

*<span style="color: blue;">[Back to Content](#content)</span>*

### Fonts

Roboto was chosen from [Google Fonts](https://fonts.google.com/specimen/Roboto?preview.text=The%20ScrollStack%20&query=roboto) as the font for this website. It is simple, easy to read and appropriate for a professional site.

![font](/documentation/readme-img/roboto-400.webp)

*<span style="color: blue;">[Back to Content](#content)</span>*

### Accessibility Features

While developing the website, I've focused on its accessibility. This goal was achieved through the following methods:

* Using semantic HTML.
* Using a hover state on all buttons on the site to make it clear to the user if they are hovering over a button.
* Choosing a sans serif font for the site - these fonts are suitable for people with dyslexia.
* The use of aria-labelledby and attributes in the game's buttons and player sections improves the accessibility of dynamic content and interactive elements for users with screen readers.
* The use of colors is considered for visibility.
* No contrast errors were detected in the page;

  ![x](#IMAGE)

  * For more details pls see:
    * [Wave Web Accessibility Evaulation Tool - AAA.HTML](#)
    * [Wave Web Accessibility Evaulation Tool - BBB.HTML](#)
    * [Wave Web Accessibility Evaulation Tool - CCC.HTML](#)

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Responsiveness

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Navigation and Page Layouts

### Landing Page

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Registration & Login

*<span style="color: blue;">[Back to Content](#content)</span>*   

### User Profile

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Book Management

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Administration Panel

*<span style="color: blue;">[Back to Content](#content)</span>*   

### Logout

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing and trouble shooting carried out.

### Documented Bugs and Fixes

*<span style="color: blue;">[Back to Content](#content)</span>*   

## Deployment

### Prequisites


- Ensure [Python](https://www.python.org/) is installed on your system.
- Verify that Python is installed on your system by checking its version. This can be done through a command in the terminal `python --version` or by running a small piece of Python code that outputs the version information.
- For installing libraries and modules, use `pip` or `pip3` depending on your Python version.

Important points for before deployment:
- The requirements for the project were added to a requirements.txt file using the command 'pip3 freeze > requirements.txt' in the terminal.
-  In .gitignore, include env.py to ensure sensitive information is not pushed to GitHub. 
-  In settings.py, link SECRET_KEY to the env.py file where the secret key variable is defined.
-  In settings.py, set 'DEBUG = False' to prevent verbose error pages and to prevent Django serving static files itself instead of relying on Cloudinary.
-  It is necessary to make migrations and migrate the models to the database before deployment.

*<span style="color: blue;">[Back to Content](#content)</span>*  

<details>
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
        - DATABASE_URL will be added automaticaly
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

*<span style="color: blue;">[Back to Content](#content)</span>*   

</details>

<details>
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

*<span style="color: blue;">[Back to Content](#content)</span>*

</details>

## Credits and Acknowledgements

### Code

```txt
T.B.D.!
```

*<span style="color: blue;">[Back to Content](#content)</span>*

### Media

Media were not used.

*<span style="color: blue;">[Back to Content](#content)</span>*

### Content

The following documentation, blogs, tutorials and guides were used to aid development.
- Bootstrap documentation
- [Django documentation](https://docs.djangoproject.com/en/5.0/)
- x

*<span style="color: blue;">[Back to Content](#content)</span>*

### Acknowledgements

I would like to thank! 

- [The Literature Map](https://www.literature-map.com/): A valuable resource provided by Gnod, the Global Network of Discovery.
- The whole team at [Code Institute Slack community](https://code-institute-room.slack.com) for their teaching and support.
- To all engaged fellow students at all channels and a special shout out to slack channel [community sweden](https://app.slack.com/client/T0L30B202/C03J2BCURV3).
- [Kera Cudmore](https://github.com/kera-cudmore) for her excellent readme example.
- My mentor [Jubril Akolade](https://github.com/jubrillionaire/)
- My immediate and extended family, as well as my friends, who support and cheer me on!

*<span style="color: blue;">[Back to Content](#content)</span>*