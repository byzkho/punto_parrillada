document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/reservations')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('session_id');
            data.forEach(reservation => {
                const option = document.createElement('option');
                option.value = reservation.id; // El valor será el id de la reservación
                option.text = `Mesa ${reservation.table.number} - ${reservation.user.full_name}`; // El texto mostrará detalles adicionales
                select.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching reservations:', error);
        });
});