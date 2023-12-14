-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
-- create new procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
  BEGIN
    DECLARE average DOUBLE;
    select sum(score) / count(user_id) INTO average from corrections where corrections.user_id = user_id;
    UPDATE users SET average_score = average WHERE id = user_id;
  END;
$$
DELIMITER ;
