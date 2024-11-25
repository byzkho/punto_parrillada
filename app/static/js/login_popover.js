const loginButton = document.getElementById("login");
const loginDialog = document.getElementById("login-dialog");
const closeDialogButton = document.getElementById("close-dialog");

// Abrir el diálogo al hacer clic en el botón
loginButton?.addEventListener("click", () => {
    loginDialog.showModal(); // Abre el diálogo
});

// Cerrar el diálogo al hacer clic en el botón de cierre
closeDialogButton?.addEventListener("click", () => {
    loginDialog.close(); // Cierra el diálogo
});