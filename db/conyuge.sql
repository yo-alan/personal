BEGIN;

CREATE TABLE conyuge(
	documento int CHECK (documento > 1000000 AND documento < 99999999),
	empleado int NOT NULL,
	nombre varchar(20) NOT NULL,
	apellido varchar(20) NOT NULL,
	fecha_nacimiento date NOT NULL,
	
	CONSTRAINT pk_conyuge
		PRIMARY KEY (documento),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
);

COMMIT;
