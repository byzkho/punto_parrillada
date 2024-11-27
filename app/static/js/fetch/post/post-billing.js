document.getElementById("billing-form")?.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita el envío estándar del formulario

    const order_id = document.getElementById("order_id").value;
    const total = document.getElementById("total").value;

    const billingData = {
        order_id: parseInt(order_id, 10),
        total: parseFloat(total)
    };

    try {
        const response = await fetch("/api/billings", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(billingData),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
            return;
        }

        alert("Factura generada exitosamente");
        document.getElementById("billing-form").reset();
    } catch (error) {
        console.error("Error generating billing:", error);
        alert("Ocurrió un error al generar la factura");
    }
});