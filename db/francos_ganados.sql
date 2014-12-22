BEGIN;

CREATE TABLE francos_ganados(
	empleado int NOT NULL,
	fecha date NOT NULL,
	cant_dias int NOT NULL,
	comentario varchar(100),
	
	CONSTRAINT pk_francos_ganados
		PRIMARY KEY (empleado, fecha),
	
	CONSTRAINT fk_empleado
		FOREIGN KEY (empleado)
		REFERENCES empleado (documento)
);

COMMIT;
