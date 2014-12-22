CREATE OR REPLACE FUNCTION delete_cascade() RETURNS TRIGGER AS $$

BEGIN
	
	DELETE FROM licencia WHERE empleado = OLD.documento;
	DELETE FROM hijo WHERE empleado = OLD.documento;
	DELETE FROM vacaciones WHERE empleado = OLD.documento;
	DELETE FROM francos_ganados WHERE empleado = OLD.documento;
	DELETE FROM observaciones WHERE empleado = OLD.documento;
	
	RETURN OLD;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER eliminar_cascade BEFORE DELETE ON empleado FOR EACH ROW EXECUTE PROCEDURE delete_cascade();



CREATE OR REPLACE FUNCTION crear_observaciones() RETURNS TRIGGER AS $$

BEGIN
	
	INSERT INTO observaciones (empleado, comentario) VALUES(NEW.documento, '');
	
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER crear_observacion AFTER INSERT ON empleado FOR EACH ROW EXECUTE PROCEDURE crear_observaciones();
