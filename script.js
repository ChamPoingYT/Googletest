document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Clear previous error messages
    document.getElementById('emailError').style.display = 'none';
    document.getElementById('passwordError').style.display = 'none';

    // Get form values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    let valid = true;

    // Validate email
    if (!validateEmail(email)) {
        document.getElementById('emailError').innerText = 'Veuillez entrer une adresse e-mail valide.';
        document.getElementById('emailError').style.display = 'block';
        valid = false;
    }

    // Validate password
    if (password.length < 6) {
        document.getElementById('passwordError').innerText = 'Le mot de passe doit comporter au moins 6 caractères.';
        document.getElementById('passwordError').style.display = 'block';
        valid = false;
    }

    if (valid) {
        // If form is valid, submit the form or do something else
        this.submit(); // Submit the form
    }
});

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return re.test(email);
}
}
