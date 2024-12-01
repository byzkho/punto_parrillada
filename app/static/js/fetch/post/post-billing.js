document.getElementById("billing-form")?.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita el envío estándar del formulario

    const order_id = document.getElementById("order_id").value;
    const total_amount = document.getElementById("total_amount").value;
    const split = document.getElementById("split").checked;

    const shares = [];
    if (split) {
        const shareInputs = document.querySelectorAll("#shares-container .form__group");
        shareInputs.forEach((group, index) => {
            const name = group.querySelector(`#share_${index + 1}_name`).value;
            const amount = group.querySelector(`#share_${index + 1}_amount`).value;
            if (name && amount) {
                shares.push({
                    full_name: name,
                    amount: parseFloat(amount)
                });
            }
        });
    }

    const billingData = {
        order_id: parseInt(order_id, 10),
        total_amount: parseFloat(total_amount),
        split: split,
        shares: shares.length > 0 ? shares : null
    };

    try {
        console.log(billingData); // Para depuración
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
        document.getElementById("split-fields").style.display = "none"; // Ocultar los campos de división de factura
    } catch (error) {
        console.error("Error generating billing:", error);
        alert("Ocurrió un error al generar la factura");
    }
});

// Mostrar y ocultar los campos de división de factura
document.getElementById("split")?.addEventListener("change", (event) => {
    const splitFields = document.getElementById("split-fields");
    if (event.target.checked) {
        splitFields.style.display = "block";
    } else {
        splitFields.style.display = "none";
    }
});

// Generar dinámicamente los campos de los participantes según la cantidad ingresada
document.getElementById("num_accompaniments")?.addEventListener("input", () => {
    const numAccompaniments = parseInt(document.getElementById("num_accompaniments").value, 10);
    const sharesContainer = document.getElementById("shares-container");
    sharesContainer.innerHTML = ''; // Limpiar los campos existentes

    for (let i = 1; i <= numAccompaniments; i++) {
        const newShareGroup = document.createElement("div");
        newShareGroup.className = "form__group";
        newShareGroup.innerHTML = `
            <label class="form__label" for="share_${i}_name">Nombre del participante ${i}:</label>
            <input class="form__input" type="text" id="share_${i}_name" name="full_name">
            <label class="form__label" for="share_${i}_amount">Monto del participante ${i}:</label>
            <input class="form__input" type="number" id="share_${i}_amount" name="amount">
        `;
        sharesContainer.appendChild(newShareGroup);
    }
});