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


// JavaScript to toggle animation class
document.getElementById('animation-toggle').addEventListener('change', function () {
    var flameDivider = document.querySelector('.flame-divider');
    if (this.checked) {
        flameDivider.classList.add('animate');
    } else {
        flameDivider.classList.remove('animate');
    }
});