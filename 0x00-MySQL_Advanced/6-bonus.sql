-- stored procedure to add bonus to students
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name)
        THEN
            INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END$$

DELIMITER ;