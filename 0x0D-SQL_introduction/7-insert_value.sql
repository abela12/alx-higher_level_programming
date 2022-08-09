-- inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server
-- New row:
--     id = 89
--     name = Best School
-- The database name will be passed as an argument of the mysql command

INSERT INTO `first_table` (`id`, `name`) VALUES(89, 'Best School');-- displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
-- The database name will be passed as an argument of the mysql command

SELECT COUNT(*) FROM first_table WHERE id=89;
