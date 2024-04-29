/**
 * This script manages the functionality of toggling the recent 
 * activity button in book-list.html.
 * 
 * Other:
 * - jshint esversion: 6, please see README.md for further details
 * 
 * Author: JaqiKal
 * Date: May 2024
 */

// jshint esversion: 6

document.addEventListener('DOMContentLoaded', function () {
    var collapseButton = document.querySelector('.btn-link');
    var collapseContent = document.getElementById('recentActivity');

    collapseButton.addEventListener('click', function () {
        var isCollapsed = collapseContent.classList.contains('show');
        collapseContent.classList.toggle('show', !isCollapsed);
    });
});