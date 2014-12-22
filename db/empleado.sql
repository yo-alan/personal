BEGIN;

CREATE TABLE empleado(
	
	id serial NOT NULL,
	documento int CHECK(documento > 1000000 AND documento < 99999999) UNIQUE NOT NULL,
	nombre varchar(30) NOT NULL,
	apellido varchar(30) NOT NULL,
	fecha_nacimiento date NOT NULL,
	genero varchar(1) CHECK(genero in ('F', 'M')),
	domicilio varchar(50) NOT NULL,
	telefono varchar(20),
	fecha_ingreso date NOT NULL,
	cuil varchar(15),
	nro_legajo int UNIQUE NOT NULL,
	sit_revista text CHECK(sit_revista IN('Transitoria', 'Temporaria', 'Permanente', 'Pasantía', 'Comisión')),
	cargo text CHECK(cargo IN('Administrativo', 'Jerárquico', 'Obrero', 'Profesional', 'Servicio')),
	observaciones text,
	
	CONSTRAINT pk_empleado
		PRIMARY KEY (id)
	
);

COMMIT;
