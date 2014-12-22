BEGIN;

CREATE TABLE observaciones(
	empleado int,
	comentario text,
	
	CONSTRAINT pk_observaciones
		PRIMARY KEY (empleado, comentario),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
);

COMMIT;
