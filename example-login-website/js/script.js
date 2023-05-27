const form = document.querySelector('form');
const loginBtn = document.querySelector('#login-btn');

form.addEventListener('submit', e => {
    e.preventDefault();

    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;

    if (username === 'admin' && password === 'password') {
        window.alert('Login successful!');
        window.location.href = 'dashboard.html'; // redirect to dashboard
    } else {
        window.alert('Invalid username or password.');
    }
});
