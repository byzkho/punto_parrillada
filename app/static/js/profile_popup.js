const profileButton = document.getElementById("profile");
const profileDialog = document.getElementById("profile-dialog");
const closeProfileDialogButton = document.getElementById("close-dialog");

// Abrir el diálogo al hacer clic en el botón
profileButton?.addEventListener("click", () => {
    profileDialog.showModal(); // Abre el diálogo
});

// Cerrar el diálogo al hacer clic en el botón de cierre
closeProfileDialogButton?.addEventListener("click", () => {
    profileDialog.close(); // Cierra el diálogo
});