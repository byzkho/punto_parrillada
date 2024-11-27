document.addEventListener('DOMContentLoaded', function () {
    fetch('/tables')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#all-tables');
            if (data.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="4">No hay mesas aún</td></tr>';
            } else {
                tableBody.innerHTML = '';
                data.forEach(table => {
                    const row = document.createElement('tr');
                    row.className = 'table__row';

                    row.innerHTML = `
                        <td class="table__cell">${table.id}</td>
                        <td class="table__cell">${table.number}</td>
                        <td class="table__cell">${table.status}</td>
                        <td class="table__cell">${table.seats}</td>
                    `;
                    tableBody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching tables:', error);
        });
});