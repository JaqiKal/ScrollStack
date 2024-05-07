/**
 * This script manages the functionality of toggling the animated line in book-list.html
 *
 * Other:
 * - jshint esversion: 6, please see README.md for further details
 *
 * Author: JaqiKal
 * Date: May 2024
 */

// jshint esversion: 6

document.addEventListener("DOMContentLoaded", function () {
    const animationToggle = document.getElementById('animation-toggle');
    const flameDivider = document.querySelector('.flame-divider');

    if (animationToggle && flameDivider) {
        // Toggle the class based on the initial state
        if (animationToggle.checked) {
            flameDivider.classList.add('animate');
        } else {
            flameDivider.classList.remove('animate');
        }

        // Add an event listener to toggle the class on change
        animationToggle.addEventListener('change', function () {
            if (this.checked) {
                flameDivider.classList.add('animate');
            } else {
                flameDivider.classList.remove('animate');
            }
        });
    }
});