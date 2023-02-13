-- FULL CREATION
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id)
VALUES (1, 2, 3, 4);

INSERT INTO second_table (name)
VALUES ("John", "Alex", "Bob", "George");

INSERT INTO second_table (score)
VALUES (10, 3, 14, 8);
