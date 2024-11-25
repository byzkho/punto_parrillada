document.getElementById("logout-button")?.addEventListener("click", async () => {
    try {
        const response = await fetch("/auth/logout", {
            method: "POST"
        });

        if (response.ok) {
            alert("Cierre de sesión exitoso");
            window.location.reload();
        } else {
            alert("No se pudo cerrar la sesión. Inténtalo más tarde.");
        }
    } catch (err) {
        console.error("Error en el logout:", err);
        alert("No se pudo conectar con el servidor. Inténtalo más tarde.");
    }
});