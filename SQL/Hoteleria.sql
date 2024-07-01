create table Hoteles (
	id_hotel SERIAL PRIMARY KEY,
	nombre varchar (50) NOT NULL,
	estrellas varchar (10) NOT NULL,
	descripcion varchar (500) NOT NULL,
	mail varchar (30) NOT NULL,
	telefono varchar (20) NOT NULL,
	activo BOOLEAN NOT NULL
); 