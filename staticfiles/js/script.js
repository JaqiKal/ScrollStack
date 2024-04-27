/*
 * Script for Delete Confirmation
 * This script provides a confirmation dialog for users trying to delete a book.
 * It uses standard JavaScript to ensure compatibility across all browsers, including older versions.
 */

function confirmDelete(event, bookId) {
    event.preventDefault(); // Stop the form from submitting immediately

    // Confirm deletion with the user
    if (window.confirm('Are you sure you want to delete this book?')) {
        // Redirect to the deletion URL if the user confirms
        window.location.href = '/books/' + bookId + '/delete/'; // Concatenation used for ES5 compatibility
    }
}