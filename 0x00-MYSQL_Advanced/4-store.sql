-- trigger that reduces the quantity of an item on insert
DELIMITER $
CREATE TRIGGER dec_quantity AFTER INSERT ON orders
    FOR EACH ROW
    BEGIN
        UPDATE items SET quantity = quantity - NEW.number
        WHERE NEW.item_name = name;
    END;$
DELIMITER ;