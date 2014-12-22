BEGIN;

CREATE TABLE vacaciones(
	
	empleado int,
	anio int,
	cantidad int,
	
	CONSTRAINT pk_vacaciones
		PRIMARY KEY (empleado, anio),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
	
);

COMMIT;
