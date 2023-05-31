// Get the form element
const form = document.querySelector('form');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
   event.preventDefault(); // Prevent the form from submitting

   // Get the values from the username and password fields
   const username = document.getElementById('username').value;
   const password = document.getElementById('password').value;

   // Perform your login logic here
   // For demonstration purposes, we'll just log the values to the console
   console.log('Username:', username);
   console.log('Password:', password);
});
