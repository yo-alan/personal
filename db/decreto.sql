BEGIN;

CREATE TABLE decreto(
	empleado int,
	nro_decreto int,
	fecha date NOT NULL,
	nombre_cargo varchar(50) NOT NULL,
	
	CONSTRAINT pk_decreto
		PRIMARY KEY (empleado, nro_decreto),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
	
);

COMMIT;
