document.addEventListener('DOMContentLoaded', function () {
    // Obtener el rol del usuario desde un atributo de datos del cuerpo
    const userRole = document.querySelector('.facturations-body').dataset.userRole;

    // Determinar la URL de la API en función del rol del usuario
    const apiUrl = userRole === 'cliente' ? '/api/billings/auth/user' : '/api/billings';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const billingTableBody = document.querySelector('#my-billings');
            if (data.length === 0) {
                billingTableBody.innerHTML = '<tr><td colspan="4">No tienes facturaciones aún</td></tr>';
            } else {
                billingTableBody.innerHTML = '';
                data.forEach(billing => {
                    const row = document.createElement('tr');
                    row.className = 'table__row';

                    row.innerHTML = `
                        <td class="table__cell">${billing.id}</td>
                        <td class="table__cell">${billing.total_amount}</td>
                        <td class="table__cell">${billing.status}</td>
                        <td class="table__cell">
                            <button onclick="viewBilling(${billing.id})">Visualizar Factura</button>
                        </td>
                    `;
                    billingTableBody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching billings:', error);
        });
});

// Función para visualizar la factura
function viewBilling(billingId) {
    fetch(`/api/billings/${billingId}`)
        .then(response => response.json())
        .then(data => {
            const billingDetails = document.getElementById('billing-details');
            billingDetails.innerHTML = `
                <p><strong>Nombre del Restaurante:</strong> Mi Restaurante</p>
                <p><strong>ID de la Factura:</strong> ${data.id}</p>
                <p><strong>Total:</strong> ${data.total_amount}</p>
                <p><strong>Estado:</strong> ${data.status}</p>
                <p><strong>Dividido:</strong> ${data.split ? 'Sí' : 'No'}</p>
                ${data.shares ? `<p><strong>Participantes:</strong></p>` : ''}
                ${data.shares ? data.shares.map(share => `
                    <p>${share.full_name}: ${share.amount}</p>
                `).join('') : ''}
            `;
            document.getElementById('billing-dialog').showModal();
        })
        .catch(error => {
            console.error('Error fetching billing details:', error);
        });
}

// Cerrar el diálogo
document.getElementById('close-dialog')?.addEventListener('click', () => {
    document.getElementById('billing-dialog').close();
});