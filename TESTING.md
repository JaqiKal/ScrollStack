# Testing

Return back to the [README.md](README.md) file.

---

## CONTENT

- [Testing overview & environment](#testing-overview--environment)
    - [Test environment](#test-environment)
    - [Browser compatibility](#browser-compatibilty)
    - [Responsiveness](#responsiveness)
- [Automated Testing](#automated-testing)
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
- [Manual testing](#manual-testing)
    - [User Stories test](#user-stories-test)
    - [Function Testing](#function-testing)
- [DEFECTS](#defects)
    - [Unsolved issue](#unsolved-issue)
    - [Known issue](#known-issue)


---
## Testing overview & environment

Testing was ongoing throughout the entire development. I used the various linters and GITPOD terminal output whilst building to pinpoint and troubleshoot any issues as I went along.

### Test environment

* Desktop:
  * Lenovo Legion T7
* Screen:
  * Samsung Odyssey G3 / 27" / 1920 x 1080 /

### Browser compatibility

* Google Chrome, version 121.0.6167.86 (Official Build) (64-bit)
* Firefox, version 123.0 (64-bit)
* Edge, version 123.0.2420.97 (Official build) (64-bit)

### Responsiveness

```text
T.B.D
```

*<span style="color: blue;">[Back to Content](#content)</span>*

## Automated Testing

No automatic testing apart from using the pep8 validator was performed.

*<span style="color: blue;">[Back to Content](#content)</span>*

## Code Validation

### HTML

All HTML files were validated using the recommended [HTML W3C Validator](https://validator.w3.org).

Exceptions:

The presence of Jinja templates in the code, which include syntax like {% for loops %}, {% url 'home' %}, and {{ variable|filter }}, means that direct copy-pasting from source files does not validate correctly.

Normally, the [validate by URI method](https://validator.w3.org/#validate_by_uri) on deployed Heroku pages is suggested. However, this approach is impractical for my project because most pages require user login, and the W3C HTML Validator cannot access these authenticated pages.

**Alternative Validation Approach:**

To validate HTML pages that incorporate Jinja syntax and require authentication, I followed these steps:

Navigate to the authenticated pages on the deployed site.
Right-click on the page and select View Page Source (shortcut CTRL+U or ⌘+U on Mac).
This reveals the fully rendered HTML, free of Jinja syntax.
Copy this HTML and paste it into the validate by input section of the W3C validator.
This procedure was repeated for each authenticated page.

### CSS

[CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to to validate the CSS file(s).

### JavaScript

[JShint Validator](https://jshint.com) was used to validate all JS files / content.

### Python

The recommended [CI Python Linter](https://pep8ci.herokuapp.com) was to validate all Python files.

*<span style="color: blue;">[Back to Content](#content)</span>*


## Manual Test

|  Goals | Expected Outcome | Testing Performed | Result |
| :--- | :--- | :--- | :--- |

### Normal Test Case (NRM)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|

### Input validation Test (IPU)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|

### Error Handling (ERR)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|

### User Interaction Test (UIA)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|


### Integration Test (ITC)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|

*<span style="color: blue;">[Back to Content](#content)</span>*

## DEFECTS

### Bug-01

xx

#### Solution-Bug-01

xx


*<span style="color: blue;">[Back to Content](#content)</span>*

## UNSOLVED issue 

*<span style="color: blue;">[Back to Content](#content)</span>*

### KNOWN issue 

#### Gitpod IDE
Three notifications suggest that specific VS Code extensions are either installed or recommended in the workspace but are not listed in the .gitpod.yml file. To address these notifications and ensure consistent synchronization of these extensions across various setups, the extensions should be included under the vscode.extensions section of the .gitpod.yml file.

Tutor support has indicated that these notifications can be safely ignored as they merely warn that the three extensions are installed but not synchronized.

![x](/documentation/testing-img/ext-error.webp)

*<span style="color: blue;">[Back to Content](#content)</span>*