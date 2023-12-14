-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers 
-- that computes and store the average weighted score for all students.
-- create new stored procedures
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
  BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE weighted FLOAT;
    DECLARE total FLOAT;
    DECLARE cur_user INT;
    DECLARE cur1 CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN cur1;
    user_loop: LOOP
      FETCH cur1 INTO cur_user;
      IF done THEN
        LEAVE user_loop;
      END IF;
      SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
      INTO total, weighted
      FROM corrections
      INNER JOIN projects
      ON corrections.project_id = projects.id
      INNER JOIN users ON corrections.user_id = cur_user;
      UPDATE users SET average_score = total / weighted WHERE id = cur_user;
    END LOOP;
    CLOSE cur1;
  END;
$$
DELIMITER $$
