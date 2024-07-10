let BASE_URL = 'http://localhost:5000';

let filterButtons = {
    "Todos": document.querySelector("#VerTodos"),
    "Completados": document.querySelector("#VerCompletados"),
    "Archivados": document.querySelector("#VerArchivados")
}

let hotelTableBody = document.querySelector("#hotelTableBody");

function createHotel(event) {
    event.preventDefault();
    let data = {
        'nombre': document.querySelector('#text').value,
        'estrellas': document.querySelector('#Estrellas').value,
        'descripcion': document.querySelector('#mensaje').value,
        'mail': document.querySelector('#email').value,
        'telefono': document.querySelector('#number').value
    };

    let url = BASE_URL + '/api/hoteles/create/';
    fetchData(url, "POST", () => {
        loadHotels();
    }, data);
}

function archiveHotel(id) {
    let url = BASE_URL + '/api/hoteles/archive/' + id;

    fetchData(url, "DELETE", () => {
        loadHotels();
    });
}

function editHotel(id) {
    let formData = new FormData(event.currentTarget.form);
    let data = Object.fromEntries(formData.entries());

    let url = BASE_URL + '/api/hoteles/update/' + id;

    fetchData(url, "PUT", () => {
        loadHotels();
    }, data);
}

function loadHotels(filter = 'todos') {
    let url = BASE_URL + '/api/hoteles/' + filter;
    fetchData(url, "GET", (data) => {
        hotelTableBody.innerHTML = '';
        data.forEach(hotel => {
            let row = document.createElement('tr');
            row.innerHTML = `
                <td>${hotel.nombre}</td>
                <td>${hotel.estrellas}</td>
                <td>${hotel.telefono}</td>
                <td>${hotel.mail}</td>
                <td>${hotel.descripcion}</td>
                <td>
                    <button id="edit-${hotel.id_hotel}" class="edit-btn">Editar</button>
                    <button id="archive-${hotel.id_hotel}" class="archive-btn">Archivar</button>
                </td>
            `;
            hotelTableBody.appendChild(row);

            document.querySelector(`#edit-${hotel.id_hotel}`).addEventListener("click", () => editHotel(hotel.id_hotel));
            document.querySelector(`#archive-${hotel.id_hotel}`).addEventListener("click", () => archiveHotel(hotel.id_hotel));
        });
    });
}

document.querySelector("#formContac").addEventListener("submit", createHotel);

document.querySelector("#VerTodos").addEventListener("click", () => loadHotels('todos'));
document.querySelector("#VerCompletados").addEventListener("click", () => loadHotels('completed'));
document.querySelector("#VerArchivados").addEventListener("click", () => loadHotels('archived'));

loadHotels();

function fetchData(url, method, onSuccess, data) {
    let options = {
        method: method,
        headers: { 'Content-Type': 'application/json' }
    };
    if (data) {
        options.body = JSON.stringify(data);
    }

    fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (onSuccess) onSuccess(data);
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
}

document.querySelector("#formContac").addEventListener("submit", createHotel);

for (let [key, button] of Object.entries(filterButtons)) {
    button.addEventListener("click", () => {
        let url;
        switch (key) {
            case "Completados":
                url = BASE_URL + '/api/hoteles/completed/';
                break;
            case "Archivados":
                url = BASE_URL + '/api/hoteles/archived/';
                break;
            case "Todos":
                url = BASE_URL + '/api/hoteles/todos/';
                break;
            default:
                return;
        }

        fetchData(url, "GET", (data) => {
            hotelTableBody.innerHTML = ''; // Clear the table body first
            data.forEach(hotel => {
                let row = document.createElement('tr');
                row.innerHTML = `
                    <td>${hotel.nombre}</td>
                    <td>${hotel.estrellas}</td>
                    <td>${hotel.telefono}</td>
                    <td>${hotel.mail}</td>
                    <td>${hotel.descripcion}</td>
                    <td>
                        <button id="edit-${hotel.id_hotel}" class="edit-btn">Editar</button>
                        <button id="archive-${hotel.id_hotel}" class="archive-btn">Archivar</button>
                    </td>
                `;
                hotelTableBody.appendChild(row);

                document.querySelector(`#edit-${hotel.id_hotel}`).addEventListener("click", () => editHotel(hotel.id_hotel));
                document.querySelector(`#archive-${hotel.id_hotel}`).addEventListener("click", () => archiveHotel(hotel.id_hotel));
            });
        });
    });
}

