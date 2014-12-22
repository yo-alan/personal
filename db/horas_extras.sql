BEGIN;

CREATE TABLE horas_extras(
	empleado int NOT NULL,
	fecha date NOT NULL,
	horas int,
	comentario varchar(100),
	
	CONSTRAINT pk_horas_extras
		PRIMARY KEY (empleado, fecha),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
);

COMMIT;
