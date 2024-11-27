document.getElementById("login-form")?.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita el envío estándar del formulario

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    // Validación básica antes de enviar la solicitud
    if (!username || !password) {
        alert("Por favor, completa todos los campos.");
        return;
    }

    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            alert("Inicio de sesión exitoso");
            window.location.reload();
        } else {
            // Manejo de errores del servidor
            const error = await response.json();

            if (error.detail && Array.isArray(error.detail)) {
                // Si `detail` es una lista de errores (por ejemplo, de FastAPI)
                const errorMessages = error.detail.map(e => e.msg).join("\n");
                alert(`Errores:\n${errorMessages}`);
            } else if (error.detail) {
                // Si `detail` es un mensaje simple
                alert(error.detail);
            } else {
                alert("Ocurrió un error desconocido.");
            }
        }
    } catch (err) {
        console.error("Error en el login:", err);
        alert("No se pudo conectar con el servidor. Inténtalo más tarde.");
    }
});
