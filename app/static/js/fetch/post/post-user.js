document.getElementById("user-form")?.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita el envío estándar del formulario

    const full_name = document.getElementById("full_name").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;
    const role = document.getElementById("role").value;

    const userData = {
        full_name: full_name,
        username: username,
        password: password,
        email: email,
        role: role
    };

    try {
        const response = await fetch("/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
            return;
        }

        alert("Usuario creado exitosamente");
        document.getElementById("user-form").reset();
    } catch (error) {
        console.error("Error creating user:", error);
        alert("Ocurrió un error al crear el usuario");
    }
});