-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS reduce_quantity;
DELIMITER $$

-- Create the trigger
CREATE TRIGGER reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
