// Get the form and the submit button
const form = document.querySelector('form');
const submitBtn = form.querySelector('input[type="submit"]');

// Adding an event listener to the form submit event
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form submission
  
  // Get user input values
  const firstName = form.querySelector('#first-name').value;
  const email = form.querySelector('#email').value;
  const password = form.querySelector('#password').value;
  
  // Validate user input
  if (firstName.trim() === '' || email.trim() === '' || password.trim() === '') {
    alert('Please fill in all fields'); // Show error message
  } else if (!isValidEmail(email)) {
    alert('Please enter a valid email address'); // Show error message
  } else {
    // Submit the form
    form.submit();
  }
});

// Function to validate email address
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
