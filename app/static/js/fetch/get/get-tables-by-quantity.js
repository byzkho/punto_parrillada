document.querySelector('#quantity').addEventListener('change', function (event) {
    const quantity = event.target.value;
    const tableSelect = document.querySelector('#table');

    // Limpiar las opciones actuales
    tableSelect.innerHTML = '';

    fetch(`/tables/quantity?quantity=${quantity}`)
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                const option = document.createElement('option');
                option.disabled = true;
                option.selected = true;
                option.textContent = 'No hay mesas para esta cantidad';
                tableSelect.appendChild(option);
            } else {
                data.forEach(table => {
                    const option = document.createElement('option');
                    option.value = table.id;
                    option.textContent = `Mesa ${table.number} - ${table.seats} asientos`;
                    tableSelect.appendChild(option);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching tables:', error);
        });
});