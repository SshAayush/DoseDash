document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('form');
  const fname = document.getElementById('fname');
  const lname = document.getElementById('lname');
  const username = document.getElementById('username');
  const email = document.getElementById('email');
  const password = document.getElementById('password');
  const c_password = document.getElementById('c_password');
  const errorElements = document.querySelectorAll('.error');
 
  form.addEventListener('submit', function (event) {
     let isValid = true;
 
     // Clear previous error messages
     errorElements.forEach(function (error) {
       error.textContent = '';
     });
 
     // Validate first name
     if (fname.value.trim() === '') {
       isValid = false;
       fname.nextElementSibling.textContent = 'First name is required.';
     }
 
     // Validate last name
     if (lname.value.trim() === '') {
       isValid = false;
       lname.nextElementSibling.textContent = 'Last name is required.';
     }
 
     // Validate username
     if (username.value.trim() === '') {
       isValid = false;
       username.nextElementSibling.textContent = 'Username is required.';
     }
 
     // Validate email
     const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
     if (!emailRegex.test(email.value)) {
       isValid = false;
       email.nextElementSibling.textContent = 'Please enter a valid email address.';
     }
 
     // Validate password
     if (password.value.trim() === '') {
       isValid = false;
       password.nextElementSibling.textContent = 'Password is required.';
     }
 
     // Validate confirm password
     if (c_password.value.trim() === '') {
       isValid = false;
       c_password.nextElementSibling.textContent = 'Confirm password is required.';
     } else if (password.value !== c_password.value) {
       isValid = false;
       c_password.nextElementSibling.textContent = 'Passwords do not match.';
     }
 
     if (!isValid) {
       event.preventDefault(); // Prevent form submission
     }
  });
 });
 