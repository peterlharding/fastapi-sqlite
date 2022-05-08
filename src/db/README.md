To setup the database:

```
% sqlite3 new.sqlite
SQLite version 3.37.0 2021-12-09 01:34:53
Enter ".help" for usage hints.
sqlite> .read user.sql
sqlite> .read address.sql
sqlite> .read address_data.sql
sqlite> .quit

% cp new .sqlite ../../database.sqlite
```

