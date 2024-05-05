/**
 * This script manages the functionality of toggling the dropdown menu 
 * in scroll_core/book-details.html. It allows users to show or hide dropdown content 
 * by clicking on a designated button.
 * 
 * Other:
 * - jshint esversion: 6, please see README.md for further details
 * 
 * Author: YourName
 * Date: May 2024
 */

// jshint esversion: 6

document.addEventListener('DOMContentLoaded', function () {
    // ID for the dropdown toggle button
    var dropdownMenuButton = document.getElementById('dropdownMenuButton');
    // Select the dropdown menu
    var dropdownMenu = document.getElementById('dropdownMenu');
    // Select the optional arrow icon (if present)
    var toggleArrow = document.getElementById('toggleArrow');

    // Function to toggle the dropdown menu
    function toggleDropdown() {
        // Toggle the 'show' class on the dropdown menu
        dropdownMenu.classList.toggle('show');
        // If an arrow icon is present, toggle its direction
        if (toggleArrow) {
            toggleArrow.classList.toggle('arrow-up');
        }
    }

    // Attach an event listener to the dropdown toggle button
    dropdownMenuButton.addEventListener('click', function (event) {
        // Prevent the default action of the button
        event.preventDefault();
        // Call the toggleDropdown function
        toggleDropdown();
    });
});