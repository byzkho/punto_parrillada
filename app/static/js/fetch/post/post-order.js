document.getElementById("order-form")?.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita el envío estándar del formulario

    const session_id = document.getElementById("session_id").value;
    const items = document.getElementById("items").value.split(",").map(item => item.trim());

    const orderData = {
        session_id: parseInt(session_id, 10),
        items: items
    };

    try {
        const response = await fetch("/api/orders", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(orderData),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
            return;
        }

        alert("Orden creada exitosamente");
        document.getElementById("order-form").reset();
    } catch (error) {
        console.error("Error creating order:", error);
        alert("Ocurrió un error al crear la orden");
    }
});