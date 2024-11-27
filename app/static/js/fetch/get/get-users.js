document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/users')
        .then(response => response.json())
        .then(data => {
            const userTableBody = document.querySelector('#all-users');
            if (data.length === 0) {
                userTableBody.innerHTML = '<tr><td colspan="5">No hay usuarios aún</td></tr>';
            } else {
                userTableBody.innerHTML = '';
                data.forEach(user => {
                    const row = document.createElement('tr');
                    row.className = 'table__row';

                    row.innerHTML = `
                        <td class="table__cell">${user.id}</td>
                        <td class="table__cell">${user.full_name}</td>
                        <td class="table__cell">${user.username}</td>
                        <td class="table__cell">${user.email}</td>
                        <td class="table__cell">${user.role}</td>
                    `;
                    userTableBody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching users:', error);
        });
});