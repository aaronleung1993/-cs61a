----------
-- Dogs --
----------

CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

-- Fur
CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur UNION
  SELECT "bella"      , "short"       UNION
  SELECT "charlie"    , "long"        UNION
  SELECT "daisy"      , "long"        UNION
  SELECT "ellie"      , "short"       UNION
  SELECT "finn"       , "curly"       UNION
  SELECT "ginger"     , "short"        UNION
  SELECT "hank"       , "curly";

-- Parents of curly dogs
SELECT parent FROM parents, dogs WHERE child = name AND fur = "curly";

-- Siblings
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Grandparents
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b
    WHERE b.parent = a.child;

-- Grandogs with the same fur AS their granpups
SELECT grandog, granpup, c.fur FROM grandparents, dogs AS c, dogs AS d
  WHERE grandog = c.name AND
        granpup = d.name AND
        c.fur = d.fur;

-- Dog triples
SELECT a.name, b.name, c.name FROM dogs AS a, dogs AS b, dogs AS c
  WHERE a.name > b.name AND b.name > c.name AND a.fur = b.fur AND b.fur = c.fur;
