/* Create & Drop */
CREATE TABLE squares(n UNIQUE, n_squared);

/* Insert */
INSERT INTO squares VALUES (2, 4);
INSERT INTO squares SELECT n+1, n_squared + 2 * n + 1 FROM squares;

/* Update */
INSERT INTO squares VALUES (4, 0), (5, 0), (6, 0);
UPDATE squares SET n_squared=n * n WHERE n_squared = 0;
SELECT * FROM squares;

/* Delete */
DELETE FROM squares WHERE n < 4;
SELECT * FROM squares;
