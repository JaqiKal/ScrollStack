<!-- THIS IS A DRAFT! -->

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

#### Manual steps to render error page on local host and in production

**Note:** If the project is set up to collect static files in a production-like environment (i.e., DEBUG = False), missing static files might cause warnings or errors that can affect the rendering of the error pages.

<details>
  <summary>Local host environment</summary><br>

- Manual steps to simulate error 403 in local host:

  1. Ensure the 403.html template exists in the templates/errors directory properly formatted.
  2. In scroll_core/views.py, create a test_403 function that raises a PermissionDenied.
  3. In scroll_manager/urls.py, Add URL pattern 'test_403' for testing view.
  4. In scroll_core/views.py, add a custom_403 function to return the 403 error page.
  5. In settings.py set DEBUG = True
  6. Visit localhost and add /test-403 to the end of the www url path.
  7. Verify that the custom 403.html template is displayed with the error message: "Error 403: Forbidden".

- Manual steps to simulate error 404 in local host:

  1. Ensure the 404.html template exists in the templates/errors directory properly formatted.
  2. In scroll_core/views.py, create a custom_404 function that returns a '404' response.
  3. In scroll_manager/urls.py, add the custom error handler for 404
  4. In settings.py set DEBUG = False
  5. Visit localhost and add a non-existent path such as /non-existent to the end of the www url path.
  6. Verify that the custom 404.html template is displayed with the error message: "Error 404: Not Found".

- Manual steps to simulate error 500 in local host:

  1. Ensure the 500.html template exists in the templates/errors directory properly formatted.
  2. In scroll_core/views.py, create a test_500 function that raises an exception to simulate a server error.
  3. In scroll_core/views.py, add a custom_500 error handler that returns a 500 response.
  4. In scroll_manager/urls.py, add the test_500 view.
  5. In scroll_manager/urls.py, add the custom_500 error handler.
  6. In settings.py set DEBUG = False
  7. Visit localhost and add /test-500 to the end of the www url path.
  8. Verify that the custom 500.html template is displayed with the error message: "Error 500: Internal Server Error.".

</details>


<details>
  <summary>Production environment</summary><br>

- Manual steps to simulate error 403 in production: 

  1. Add permissions to Book model

  ```text
  class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Book Title’)

    # Other fields...

  class Meta:
        ordering = ['title'] # Orders by title alphabetically by default
        
        permissions = [
            ("view_all_books", "Can view all books"),
            ("edit_books", "Can edit books"),
        ]

    # Other fields...
  ```

  2.   Create a view requiring specific permissions.

  ```text
    # Other fields...

  from django.contrib.auth.decorators import login_required, permission_required

     # Other fields...

  @login_required
  @permission_required('scroll_core.edit_books', raise_exception=True)
  def restricted_edit_books(request):
      """
      View that allows editing of books only to users with edit_books permission.
      """
      return render(request, 'scroll_core/restricted_edit_books.html')

    # Other fields...
  ```

  3. Add the new view to your URLs.

    ```text
    # Other fields...

    urlpatterns = [
          
          # Other paths...
          
          path('restricted-edit-books/', views.restricted_edit_books, name='restricted-edit-books’),
    ]
    ```
  4. Access the Django Admin Panel in Heroku.
  5. Log in with your admin credentials.
  6. Assign the edit_books permission to some users/groups, in this case the superuser have all permissions required.
  7. Edit another User: Check the box for Can edit books, save changes.
  8. Provoke a 403 error by visiting https://scrollstack-af4b226be9f2.herokuapp.com/restricted-edit-books/
  9. ensure the custom 403 error page is rendered.
  
    ![x](/documentation/images/testing/error-403-production.webp) 


- Manual steps to simulate error 404 in in production

  1. Make sure the 404.html template exists in the templates/errors directory and is properly formatted.
  2. Ensure you have the custom_404 error handler defined in scroll_core/views.py.
      ```text
      from django.http import HttpResponseNotFound

      def custom_404(request, exception):
          """Custom view to handle 404 Not Found errors."""
          html_content = render(request, 'errors/404.html', status=404)
          return HttpResponseNotFound(html_content)
        ```
  3. In scroll_manager/urls.py, set the custom error handler for 404.
      ```text
      from scroll_core.views import custom_404

      urlpatterns = [

        # Path fields...

      ]

      # Setting custom error handlers
      handler404 = 'scroll_core.views.custom_404'
      ```
  4. Push your changes to the Heroku repository to ensure the new error page is available in production.
  5. Ensure DEBUG is set to False in the Heroku environment variables.
  6. Visit the deployed Heroku app URL with the /idontextist/ path to trigger a 404 error and see the custom error page.

    ![x](/documentation/images/testing/error-404-production.webp) 

- Manual steps to simulate error 500 in production

  1. Make sure the 500.html template exists in the templates/errors directory and is properly formatted.
  2. In scroll_core/views.py, create a test_500 function that raises an exception to simulate a server error.
  3. In scroll_manager/urls.py, add the test_500 view.
  4. Ensure you have the custom_500 error handler defined in scroll_core/views.py.
  5. Push your changes to the Heroku repository to ensure the new error page is available in production.
  6. Ensure DEBUG is set to False in the Heroku environment variables.
  7. Visit the deployed Heroku app URL with the /test-500/ path to trigger a 500 error and see the custom error page.

    ![x](/documentation/images/testing/error-500-production.webp) 

<br></details>


| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|ERR-001|Custom 403 Error Page - localhost|Display the custom 403.html page with error message|Visit http://localhost:8000/test-403|PASS|localhost|
|ERR-002|Custom 404 Error Page - localhost|Display the custom 404.html page with error message|Visit http://localhost:8000/test-404|PASS|localhost|
|ERR-003|Custom 500 Error Page - localhost|Display the custom 500.html page with error message|Visit http://localhost:8000/test-500|PASS|localhost|
|ERR-004|Custom 403 Error Page - production|Display the custom 403.html page with error message|Visit http://localhost:8000/test-403|PASS|production|
|ERR-005|Custom 404 Error Page - production|Display the custom 404.html page with error message|Visit http://localhost:8000/test-404|PASS|production|
|ERR-006|Custom 500 Error Page - production|Display the custom 500.html page with error message|Visit http://localhost:8000/test-500|PASS|production|

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