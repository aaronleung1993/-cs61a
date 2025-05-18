SELECT ROUND(1.0 * fa23 / fa08, 2) FROM cal WHERE source="student";

SELECT ROUND(1.0 * SUM(fa23) / SUM(fa08), 2) FROM cal WHERE type="Regular Faculty";

SELECT ROUND(1.0 * SUM(fa23) / SUM(fa08), 2) FROM cal GROUP BY type;

SELECT INSTR(type, "Faculty")

SELECT INSTR(type, "Faculty") > 0 AS Faculty, ROUND(1.0 * SUM(fa23) / SUM(fa08), 2) FROM cal WHERE Faculty=1;

SELECT ROUND(1.0 * SUM(fa23) / SUM(fa08), 2) FROM cal WHERE INSTR(type, "Faculty") > 0;

SELECT ROUND(1.0 * SUM(fa23) / SUM(fa08), 2) FROM cal WHERE type LIKE '%Faculty';
