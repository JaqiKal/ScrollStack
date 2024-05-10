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
- [Lighthouse](#lighthouse)
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

App is fully responsive on breakpoints supported by Bootstrap 5.3.3.

| **Breakpoint** | **Prefix** | **Minimum Width** |
|----------------|------------|-------------------|
| Extra Small    | `xs`       | `< 576px`         |
| Small          | `sm`       | `≥ 576px`         |
| Medium         | `md`       | `≥ 768px`         |
| Large          | `lg`       | `≥ 992px`         |
| Extra Large    | `xl`       | `≥ 1200px`        |
| Extra Extra Large | `xxl`   | `≥ 1400px`        |


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

#### Landing non authenticated

![x](/documentation/images/testing/validate-landing-non-auth.png)

#### Sign Up

![x](/documentation/images/testing/validate-signup.png)

#### Log In

![x](/documentation/images/testing/validate-login.png)

#### Home authenticated

![x](/documentation/images/testing/validate-landing-auth.png)

#### Book Details

![x](/documentation/images/testing/validate-book-details.png)

#### Add / Edit book

Please, see chapter [Unsolved Issues](#unsolved-issue)
![x](/documentation/images/testing/validate-add-book-error.png)

#### Confirm Delete

![x](/documentation/images/testing/validate-confirm-delete.png)

#### Log Out

![x](/documentation/images/testing/validate-logout.png)

#### Forgot Password

![x](/documentation/images/testing/validate-forgot-pw.png)

#### Change Password

![x](/documentation/images/testing/validate-change-pw.png)

#### Password reset done

![x](/documentation/images/testing/validate-pw-reset-done.png)


### CSS

[CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to to validate the CSS file(s).

![x](/documentation/images/testing/validate-css.png)
![x](/documentation/images/testing/validates-css-warning.png)

### JavaScript

[JShint Validator](https://jshint.com) was used to validate all JS files / content.

- **auto-dismiss-alerts.js**

The error happens because the variable bootstrap is not directly defined in the JavaScript code. The Bootstrap JavaScript components is imported in the base.html file, and it is the parent template for the page that use the alert.

![x](/documentation/images/testing/validates-auto-dismiss-alert.png)

- toggle-animated-line.js

![x](/documentation/images/testing/validate-toggle-animated-line.png)

### Python

The recommended [CI Python Linter](https://pep8ci.herokuapp.com) was to validate all Python files.

![x](/documentation/images/testing/pep8.png)

*<span style="color: blue;">[Back to Content](#content)</span>*

## Lighthouse - Desktop

### Landing non authenticated

![x](/documentation/images/testing/lighthouse-landing-non-auth.png)

### Sign Up

![x](/documentation/images/testing/lighthouse-signup.png)

### Log In

![x](/documentation/images/testing/lighthouse-login.png)

### Home authenticated

![x](/documentation/images/testing/lighthouse-book-list.png)

![x](/documentation/images/testing/lighthouse-book-list-issues.png)

### Book Details

![x](/documentation/images/testing/lighthouse-book-details.png)

![x](/documentation/images/testing/lighthouse-book-list-issues.png)

### Add / Edit book

![x](/documentation/images/testing/lighthouse-add-edit.png)

### Confirm Delete

![x](/documentation/images/testing/lighthouse-confirm-delete.png)

### Log Out

![x](/documentation/images/testing/lighthous-logout.png)


## Manual Test

|  Goals | Expected Outcome | Testing Performed | Result |
| :--- | :--- | :--- | :--- |

### **Normal Functionality Tests (NRM)**

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|NRM-001|Sign Up | Register a new user account successfully | Fill out and submit the sign-up form | PASS | Valid credentials |
|NRM-002|Login | Login to an existing user account | Fill out and submit the login form | PASS | Valid credentials |
|NRM-003|Logout | Successfully log out of the application | Click "Logout" in the navbar | PASS | |
|NRM-004|Reset Forgotten Password | Receive a reset password email | Submit the forgotten password form | PASS | |
|NRM-005|Add Book | Add a new book to the user's collection | Fill out and submit the "Add Book" form | PASS | Valid book details |
|NRM-006|Edit Book | Update the details of an existing book | Fill out and submit the "Edit Book" form | PASS | Valid book details |
|NRM-007|Delete Book | Remove a book from the user's collection | Confirm the book deletion on the "Confirm Delete" page | PASS | Confirm dialog |
|NRM-008|Search Books | Find books by title or author | Enter a query and submit the search form | PASS | Matching results |
|NRM-009|View Book List | Display a list of all the user's books | Visit "My Library" page | PASS | All books shown |
|NRM-010|View Book Details | Display the details of a specific book | Visit the book details page |PASS | Correct book data |

### **Error Handling Tests (ERR)**

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
  6. Visit the deployed Heroku app URL with the /idontexist/ path to trigger a 404 error and see the custom error page.

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
|ERR-001|Custom 403 Error Page - localhost|Display the custom 403.html page with error message|Visit http: localhost/test-403|PASS|localhost|S
|ERR-002|Custom 404 Error Page - localhost|Display the custom 404.html page with error message|Visit http: localhost/non-existent|PASS|localhost|
|ERR-003|Custom 500 Error Page - localhost|Display the custom 500.html page with error message|Visit http: localhost/test-500|PASS|localhost|
|ERR-004|Custom 403 Error Page - production|Display the custom 403.html page with error message|Visit heroku.../restricted-edit-books|PASS|production|
|ERR-005|Custom 404 Error Page - production|Display the custom 404.html page with error message|Visit heroku...//idontexist|PASS|production|
|ERR-006|Custom 500 Error Page - production|Display the custom 500.html page with error message|Visit heroku...//test-500|PASS|production|


### **Integration Tests**

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|INT-001|Guide Access | Access the guide for book management | Visit the "Guide" page | PASS | Guide page content |

### **Robustness Tests**

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|ROB-001|Duplicate Book | Prevent adding a duplicate book | Attempt to add a book with an existing ISBN | PASS | Validation error |
|ROB-002|Invalid ISBN | Prevent adding a book with an invalid ISBN | Attempt to add a book with an invalid ISBN | PASS | Validation error |
|ROB-003|Blank Fields | Prevent form submission with blank required fields | Submit forms with missing data | PASS | Validation error |
|ROB-004|Unauthorized Book Edit | Prevent unauthorized book editing | Attempt to edit a book not owned by the user | PASS | Custom 403 page |
|ROB-005|Unauthorized Book Deletion | Prevent unauthorized book deletion | Attempt to delete a book not owned by the user | PASS | Custom 403 page |
|ROB-006|Invalid Image | Prevent uploading an unsupported image format | Attempt to upload a non-image file as the cover picture | PASS | Validation error |

### **Accessibility Tests**

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|ACC-001|Keyboard Navigation | Navigate the website using only the keyboard | Use tab and enter keys to navigate | PASS | Smooth navigation |
|ACC-002|Screen Reader Compatibility | Ensure compatibility with screen readers | Use a screen reader to browse the site | PASS | All content read properly |
|ACC-003|Color Contrast | Verify sufficient color contrast | Use color contrast tools | PASS | Meets WCAG guidelines |

### **Responsive Design Tests**

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
|RESP-001|Mobile Navigation | Ensure proper display and navigation on mobile devices | Browse the site on mobile devices | PASS | Mobile-first design |
|RESP-002|Tablet Navigation | Ensure proper display and navigation on tablet devices | Browse the site on tablets | PASS| Consistent behavior |
|RESP-003|Desktop Navigation | Ensure proper display and navigation on desktop devices | Browse the site on desktop | PASS | Consistent behavior |


*<span style="color: blue;">[Back to Content](#content)</span>*

## DEFECTS

### Solved Issues

1. [BUG#50: Swedish characters are not accepted in Django Admin Interface when adding names](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=60193635)
2. [BUG#51: favicon does not display](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=60338451)
3. [BUG#52: When authenticated (logged in) the body is showing base template.](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=60868592)
4. [BUG#53: Author is missing from book_form.html](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61223109)
5. [BUG#54: Author fields not present in the book_form.html](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61223029)
6. [BUG#55: UnorderedObjectListWarning: Pagination may yield inconsistent results...](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61232158)
7. [BUG#57: When adding book with long title Data errror:value too long for type character varying(50) is thrown](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61786547)
8. [BUG#58: '__str__returnedon-string (type NoneType)](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61790424)
9. [BUG#59: Fixing Role-Based Permissions for Book Editing](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61910824)
10. [BUG#60: Fix Incorrect Redirection on Custom Error Pages for Authenticated Users](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=61934027)
11. [BUG#61: Change password does not work](https://github.com/users/JaqiKal/projects/10/views/1?pane=issue&itemId=62030839)

*<span style="color: blue;">[Back to Content](#content)</span>*

## UNSOLVED issue 

While validating the add/edit form, an error message is received, "The src attribute of the <img> tag is empty, which results in an invalid value.".
    ```text
    Bad value for attribute src on element img: Must be non-empty.
    From line 136, column 21; to line 137, column 41
    <img id="current-image" src="" width="150" height="225" alt="Book cover">
    ```

Following attempts is made to solve issue, however it failed with 500 error, current site is deployed with this error. This is not fatal in the sense that it will crash the application. However, it indicates a validation issue related to an empty src attribute for an <img> element. This issue could affect the user experience because:
- An image placeholder or broken image icon will be displayed due to the missing image source.
- Although an empty image will still show the alternative text (alt attribute), it isn't ideal for a good user experience.

1. The logic in book_form.html is changed to secure that the src attribute is not be empty. The image is in static/image folder.

    ```html
    {% if form.instance.image %}
    <div class="form-group">
        <a href="{{ form.instance.image.url }}" target="_blank" style="cursor: pointer;">
            <img id="current-image" src="{{ form.instance.image.url }}" width="150" height="225"
                alt="{{ form.instance.title|default:'Book cover' }}">
        </a>
    </div>
    {% else %}
    <div class="form-group">
        <img id="current-image" src="{% static 'images/default-book-cover.webp' %}" width="150" height="225"
            alt="Default book cover">
    </div>
    {% endif %}
    ````
2. Adjust the validation logic for the BookForm to ensure that the image field, if missing, is not saved with an empty src.

    ```python
    class BookForm(forms.ModelForm):
        # Image Field Validator
        image = forms.ImageField(
            validators=[validate_image_file_extension],
            required=False,
            help_text="Upload a cover image. Only jpg, jpeg, png, and webp formats are allowed."
        )

        def save(self, commit=True):
            """
            Save the form instance and handle the creation or linking
            of the author. Avoid duplicate author entries and ensure author
            details are updated if necessary.
            """
            book = super(BookForm, self).save(commit=False)

            # Ensure book image is set or a default one is assigned
            if not book.image:
                book.image = 'https://res.cloudinary.com/dsbcjtatz/image/upload/v1714578907/scroll_core/book_cover_images/default-book-cover_t2lyio.webp'

            # Other author and book linking logic...

            if commit:
                book.save()
                self.save_m2m()  # Save many-to-many fields

            return book
    ```

3. Set initial values in the form to ensure that an image is provided for an existing book.

    ```python
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            authors = self.instance.get_authors()
            if authors:
                author = authors[0]
                self.fields['author_first_name'].initial = author.first_name
                self.fields['author_middle_name'].initial = author.middle_name
                self.fields['author_last_name'].initial = author.last_name
            # Ensure the image field has an initial value
            if self.instance.image:
                self.fields['image'].initial = self.instance.image
      ```



*<span style="color: blue;">[Back to Content](#content)</span>*

### KNOWN issue 

#### Empty Non-Editable "Currently" Field for Book Cover Image. 
- When editing a book's details in the form, an empty non-editable input field labeled "Currently" appear next to the "Book Cover Image" field. Despite attempts to remove it using custom Crispy Forms layouts and explicit HTML templates, the field remains visible. This field is likely rendered due to how the Django `ImageField` widget works with Crispy Forms. By default, it tries to provide an indication of the current file path, even if the image is not explicitly displayed.

#### Gitpod IDE
- Three notifications suggest that specific VS Code extensions are either installed or recommended in the workspace but are not listed in the .gitpod.yml file. To address these notifications and ensure consistent synchronization of these extensions across various setups, the extensions should be included under the vscode.extensions section of the .gitpod.yml file.

Tutor support has indicated that these notifications can be safely ignored as they merely warn that the three extensions are installed but not synchronized.

![x](/documentation/images/testing/ext-error.webp)

*<span style="color: blue;">[Back to Content](#content)</span>*