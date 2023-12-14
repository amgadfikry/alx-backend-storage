-- script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.
-- create new stored procedures
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
  BEGIN
    DECLARE weighted FLOAT;
    DECLARE total FLOAT;
    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
      INTO total, weighted
      FROM corrections
      INNER JOIN projects
      ON corrections.project_id = projects.id
      INNER JOIN users ON corrections.user_id = user_id;
    UPDATE users SET average_score = total / weighted WHERE id = user_id;
  END;
$$
DELIMITER $$
