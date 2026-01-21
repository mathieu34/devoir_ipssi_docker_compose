📘 TP Docker-compose

Les commandes :

exo 1 :

* Make re
* http://localhost:5000/api/hello
* http://localhost:3000/ : frontend

exo 2 :

* make re
* http://localhost:3000/ : frontend

\- Modifier db depuis container backend :

docker compose exec backend sh

sqlite3 /data/users.db

SELECT \* FROM users;

UPDATE users SET username='test' WHERE id=1;

