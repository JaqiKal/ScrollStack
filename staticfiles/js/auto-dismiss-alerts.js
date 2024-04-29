/**
 * This script manages the functionality of auto-dismissing alerts.
 * 
 * Other:
 * - jshint esversion: 6, please see README.md for further details
 * 
 * Author: JaqiKal
 * Date: May 2024
 */

// jshint esversion: 6

document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 2500); // Close alert after n seconds
    });
});