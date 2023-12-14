# 0x00-MySQL_Advanced

### Requirements
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### tasks

#### 0-uniq_users.sql
Write a SQL script that creates a table users following these requirements:
- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database
Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application

#### 1-country_users.sql
Write a SQL script that creates a table users following these requirements:
- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
- If the table already exists, your script should not fail
- Your script can be executed on any database

#### 2-fans.sql
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
Requirements:
- Import this table dump: metal_bands.sql.zip
- Column names must be: origin and nb_fans
- Your script can be executed on any database
Context: Calculate/compute something is always power intensive… better to distribute the load!

#### 3-glam_rock.sql
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
Requirements:
- Import this table dump: metal_bands.sql.zip
- Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
- You should use attributes formed and split for computing the lifespan
- Your script can be executed on any database

#### 4-store.sql
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
Quantity in the table items can be negative.
Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

#### 5-valid_email.sql
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

#### 6-bonus.sql
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
Requirements:
- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction
Context: Write code in SQL is a nice level up!

#### 7-average_score.sql
Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
Requirements:
- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

#### 8-index_my_names.sql
Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.
Requirements:
- Import this table dump: names.sql.zip
- Only the first letter of name must be indexed
Context: Index is not the solution for any performance issue, but well used, it’s really powerful!

#### 9-index_name_score.sql
Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
Requirements:
- Import this table dump: names.sql.zip
- Only the first letter of name AND score must be indexed

#### 10-div.sql
Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
Requirements:
- You must create a function
- The function SafeDiv takes 2 arguments:
-- a, INT
-- b, INT
- And returns a / b or 0 if b == 0

#### 11-need_meeting.sql
Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
Requirements:
- The view need_meeting should return all students name when:
- They score are under (strict) to 80
- AND no last_meeting date OR more than a month