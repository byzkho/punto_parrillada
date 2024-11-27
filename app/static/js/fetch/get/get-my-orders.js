document.addEventListener('DOMContentLoaded', function () {
    // Obtener el rol del usuario desde un atributo de datos del cuerpo
    const userRole = document.querySelector('.orders-body').dataset.userRole;

    // Determinar la URL de la API en función del rol del usuario
    const apiUrl = userRole === 'cliente' ? '/api/orders/auth/user' : '/api/orders';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const orderTableBody = document.querySelector('#my-orders');
            if (data.length === 0) {
                orderTableBody.innerHTML = '<tr><td colspan="3">No tienes órdenes aún</td></tr>';
            } else {
                orderTableBody.innerHTML = '';
                data.forEach(order => {
                    const row = document.createElement('tr');
                    row.className = 'table__row';

                    // Crear el contenido del diálogo de productos
                    const productsDialogId = `products-dialog-${order.id}`;
                    const productsDialogBackdropId = `products-dialog-backdrop-${order.id}`;
                    const productsDialog = document.createElement('dialog');
                    productsDialog.id = productsDialogId;
                    productsDialog.className = 'dialog';
                    productsDialog.innerHTML = `
                        <h2>Productos de la Orden ${order.id}</h2>
                        <ul>
                            ${order.order_items.map(item => `<li>${item.product}</li>`).join('')}
                        </ul>
                        <button id="close-dialog-${order.id}">Cerrar</button>
                    `;
                    document.body.appendChild(productsDialog);

                    // Crear el fondo borroso y medio negro transparente
                    const productsDialogBackdrop = document.createElement('div');
                    productsDialogBackdrop.id = productsDialogBackdropId;
                    productsDialogBackdrop.className = 'dialog-backdrop';
                    document.body.appendChild(productsDialogBackdrop);

                    // Agregar evento para cerrar el diálogo y el fondo
                    document.getElementById(`close-dialog-${order.id}`).addEventListener('click', () => {
                        productsDialog.close();
                        productsDialogBackdrop.style.display = 'none';
                    });

                    // Crear el botón de cambio de estado en función del rol del usuario
                    let actionButton = '';
                    if (userRole === 'mesero') {
                        actionButton = `<button onclick="changeOrderStatus(${order.id}, 'preparing')">Cambiar estado a preparando</button>`;
                    } else if (userRole === 'cocinero') {
                        actionButton = `<button onclick="changeOrderStatus(${order.id}, 'prepared')">Cambiar estado a preparado</button>`;
                    }

                    row.innerHTML = `
                        <td class="table__cell">${order.id}</td>
                        <td class="table__cell">
                            <button onclick="document.getElementById('${productsDialogBackdropId}').style.display = 'block'; document.getElementById('${productsDialogId}').showModal()">Ver Productos</button>
                        </td>
                        <td class="table__cell">${order.status}</td>
                        <td class="table__cell">${actionButton}</td>
                    `;
                    orderTableBody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching orders:', error);
        });
});

// Función para cambiar el estado de la orden
function changeOrderStatus(orderId, status) {
    const url = `/api/orders/${orderId}/${status}`;
    fetch(url, {
        method: 'POST',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al cambiar el estado de la orden');
        }
        return response.json();
    })
    .then(data => {
        alert(`Estado de la orden ${orderId} cambiado a ${status}`);
        location.reload(); // Recargar la página para actualizar el estado de las órdenes
    })
    .catch(error => {
        console.error('Error changing order status:', error);
        alert('Ocurrió un error al cambiar el estado de la orden');
    });
}