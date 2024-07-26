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
        // If form is valid, send data to the server
        fetch('http://localhost:8080', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`,
        })
        .then(response => response.text())
        .then(data => {
            alert(data); // Show the response from the server
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return re.test(email);
}
