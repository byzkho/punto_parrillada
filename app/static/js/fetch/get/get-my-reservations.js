document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/user/reservations')
        .then(response => response.json())
        .then(data => {
            const reservationsTableBody = document.querySelector('#my-reservations');
            if (data.length === 0) {
                reservationsTableBody.innerHTML = '<tr><td colspan="4">No tienes reservaciones</td></tr>';
            } else {
                reservationsTableBody.innerHTML = '';
                data.forEach(reservation => {
                    const row = document.createElement('tr');
                    row.className = 'table__row';

                    // Transformar la fecha y hora a un formato legible
                    const dateTime = new Date(reservation.date_time);
                    const formattedDate = dateTime.toLocaleDateString('es-ES', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                    });
                    const formattedTime = dateTime.toLocaleTimeString('es-ES', {
                        hour: '2-digit',
                        minute: '2-digit'
                    });

                    row.innerHTML = `
                        <td class="table__cell">${reservation.table.number}</td>
                        <td class="table__cell">${reservation.table.seats}</td>
                        <td class="table__cell">${reservation.table.status}</td>
                        <td class="table__cell">${formattedDate} ${formattedTime}</td>
                    `;
                    reservationsTableBody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching reservations:', error);
        });
});