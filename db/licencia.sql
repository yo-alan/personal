BEGIN;

CREATE TABLE licencia(
	
	id serial,
	id_empleado int NOT NULL,
	desde date NOT NULL,
	hasta date NOT NULL,
	dias_tomados int,
	tipo varchar(11) CHECK(tipo IN('18', '3', '53', '58', 'Comisión', 'Enfermedad', 'Franco', 'Otro')) NOT NULL,
	comentario text,
	
	CONSTRAINT pk_licencia
		PRIMARY KEY (id),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (id_empleado)
		REFERENCES empleado (id)
);

COMMIT;
