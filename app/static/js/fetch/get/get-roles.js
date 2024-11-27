document.addEventListener('DOMContentLoaded', function () {
    fetch('/roles/')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('role');
            data.forEach(role => {
                const option = document.createElement('option');
                console.log(role.value)
                option.value = role.value; // El valor será el valor del rol
                option.text = role.value; // El texto mostrará el nombre del rol
                select.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching roles:', error);
        });
});