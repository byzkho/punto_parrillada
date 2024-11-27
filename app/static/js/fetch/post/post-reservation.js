const form = document.querySelector('#reservation-form');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(form);
    const data = {};
    for (const [key, value] of formData.entries()) {
        data[key] = value;
    }

    // Combina los valores de los campos de fecha y hora
    const date = formData.get('date');
    const time = formData.get('time');
    if (date && time) {
        data['date_time'] = `${date}T${time}`;
    }

    // Elimina los campos de fecha y hora individuales
    delete data['date'];
    delete data['time'];

    console.log(data);

    fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert('Reservación creada exitosamente');
                form.reset();
            }
        })
        .catch(error => {
            console.error('Error creating reservation:', error);
            alert('Ocurrió un error al crear la reservación');
        });
});