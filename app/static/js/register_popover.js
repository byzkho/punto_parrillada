document.addEventListener("DOMContentLoaded", () => {
    const registerButton = document.querySelector(".navbar__link#register"); // Botón de iniciar sesión
    const popover = document.querySelector(".popover#registerPopover"); // El popover
    const closeButton = document.querySelector(".popover__close-button"); // Botón de cerrar

    // Función para mostrar el popover
    const showPopover = () => {
        // Mostrar el popover
        popover.style.display = "block";
    
        // Obtener las dimensiones del botón y ajustar el posicionamiento
        const buttonRect = registerButton.getBoundingClientRect();
        popover.style.top = `${buttonRect.bottom + window.scrollY + 10}px`;
        popover.style.left = `${buttonRect.right + window.scrollX - popover.offsetWidth}px`;
    };

    // Función para ocultar el popover
    const hidePopover = () => {
        if(popover){
            popover.style.display = "none";
        }
    };

    // Mostrar el popover al hacer clic en el botón
    registerButton?.addEventListener("click", (event) => {
        event.preventDefault();
        if (popover.style.display === "block") {
            hidePopover();
        } else {
            showPopover();
        }
    });

    // Cerrar el popover al hacer clic en el botón de cerrar
    closeButton?.addEventListener("click", hidePopover);

    // Cerrar el popover si se hace clic fuera de él
    document.addEventListener("click", (event) => {
        if (
            !popover?.contains(event.target) &&
            event.target !== registerButton
        ) {
            hidePopover();
        }
    });
});
