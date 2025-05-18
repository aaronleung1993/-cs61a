
-- Parents
create table parents as
  select "a" as parent, "b" as child union
  select "a"          , "c"          union
  select "d"          , "h"          union
  select "f"          , "a"          union
  select "f"          , "d"          union
  select "f"          , "g"          union
  select "e"          , "f";
