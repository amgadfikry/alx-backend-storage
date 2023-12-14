-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
-- create new procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
  BEGIN
    DECLARE average INT;
    DECLARE num INT;
    SELECT SUM(score), COUNT(user_id) INTO average, num FROM corrections WHERE user_id = user_id;
    UPDATE users SET average_score = average / num WHERE id = user_id;
  END;
$$
DELIMITER ;
