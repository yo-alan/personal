BEGIN;

CREATE TABLE hijo(
	documento int CHECK (documento > 1000000 AND documento < 99999999),
	empleado int NOT NULL,
	nombre varchar(20) NOT NULL,
	apellido varchar(20) NOT NULL,
	fecha_nacimiento date NOT NULL,
	escolarizado boolean DEFAULT FALSE,
	
	CONSTRAINT pk_hijo
		PRIMARY KEY (documento),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
);

COMMIT;
