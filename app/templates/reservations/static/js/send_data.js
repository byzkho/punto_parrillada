form = document.querySelector('#reservation-form');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(form);
    const data = {};
    for (const [key, value] of formData.entries()) {
        console.log(key)
        console.log(value)
        data[key] = value;
    }
    console.log(data)
    fetch('/reservations', {
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