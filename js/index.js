let BASE_URL = 'http://localhost:5000';

let filterButtons = {
    "Todos": document.querySelector("#VerTodos"),
    "Completados": document.querySelector("#VerCompletados"),
    "Archivados": document.querySelector("#VerArchivados") 
}

let hotelContainer = document.querySelector(".hoteles-container");

let hotelTodosTemplateReference = document.querySelector(".hotel.todos.template");

let hotelCompletedTemplateReference = document.querySelector(".hotel.completado.template");

let hotelArchivedTemplateReference = document.querySelector(".hotel.archivado.template");

let hotelTemplates = {
    "Todos": hotelTodosTemplateReference.cloneNode(true),
    "Completado": hotelCompletedTemplateReference.cloneNode(true),
    "Archivado": hotelArchivedTemplateReference.cloneNode(true)
};

hotelTodosTemplateReferenceTemplateReference.remove();
hotelCompletedTemplateReference.remove();
hotelArchivedTemplateReference.remove();

function archiveHotel(event) {
    let id = event.currentTarget.id_hotel;

    let url = BASE_URL + '/api/hoteles/archived/' + id;

    fetchData(url, "DELETE", () => {
        location.reload();
    });
}

function editHotel(event) {
    let id = event.currentTarget.id_hotel;
    window.location.replace("pages/add_update_hoteles.html?id_hotel=" + id);
}

function CompletedHotel(event){
    let id = event.currentTarget.id_hotel;

    let url = BASE_URL + '/api/hoteles/completed/' + id;

    fetchData(url, "PUT", () => {
        location.reload();
    });
}

function loadHotel(hotel_status) {
    let fetch_data = {
        'Todos': {
            'URL': BASE_URL + '/api/hoteles/todos/',
            'HotelTemplatesName': 'Todos'
        },

        'Completados': {
            'URL': BASE_URL + '/api/hoteles/completed/',
            'HotelTemplatesName': 'Completados'
        },

        'Archivados': {
            'URL': BASE_URL + '/api/hoteles/archived/',
            'HotelTemplatesName': 'Archivados'
        },
    }

    if (!(hotel_status in fetch_data)){
        throw new Error(`El Parametro: ${hotel_status} no está definido!`);
    }

    fetchData(fetch_data[hotel_status].URL, "GET", (data) => {
        
        let hoteles = [];
        for (const hotel of data) {
            let newHotel = hotelTemplates[fetch_data[hotel_status].HotelTemplatesName].cloneNode(true);
            newHotel.querySelector("h3 .titulo").innerHTML = hotel.nombre;
            newHotel.querySelector(".descripcion").innerHTML = hotel.descripcion;
            newHotel.querySelector(".id_hotel").value = hotel.id;

            let archivarAction = newHotel.querySelector("#Archivar");
            let editarAction =newHotel.querySelector("#Editar");
            let completarAction =newHotel.querySelector("#Completar");

            if (archivarAction) {
                archivarAction.addEventListener("click", archiveHotel);
                archivarAction.id_hotel = hotel.id;
            }

            if (editarAction) {
                editarAction.addEventListener("click", editHotel);
                editarAction.id_hotel = hotel.id;
            }

            if (completarAction) {
                completarAction.addEventListener("click", CompletedHotel);
                completarAction.id_hotel = hotel.id;
            }

            if (pasarATodosAction) {
                pasarATodosAction.addEventListener("click", TodosHotel);
                pasarATodosAction.id_hotel = hotel.id;
            }

            hoteles.push(newHotel);
        }

        hotelContainer.replaceChildren(...hoteles);
    });
}

function setActiveFilter(event){
    for (filter in filterButtons) {
        filterButtons[filter].classList.remove("active");
    }

    event.currentTarget.classList.add("active");

    loadHotel(event.currentTarget.filterName);
}

function setFilters() {
    for (button in filterButtons){
        filterButtons[button].addEventListener("click", setActiveFilter);
        filterButtons[button].filterName = button;
    }
}

setFilters();
loadHoteles('Todos');
