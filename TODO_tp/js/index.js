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

