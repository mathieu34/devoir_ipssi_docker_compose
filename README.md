📘 TP Docker-compose



Les commandes :



exo 1 :



* make all
* http://localhost:5000/api/hello
* http://localhost:3000/ : frontend



exo 2 :



* make all
* http://localhost:3000 : frontend


- Modifier db depuis container backend :
docker compose exec backend sh
sqlite3 /data/users.db
SELECT * FROM users;
UPDATE users SET username='test' WHERE id=1;



- Verif depuis container : 
docker compose exec backend sh
sqlite3 /data/users.db
SELECT * FROM users;






exo3 :



* make all
* http://localhost:5000/users : backend 
* http://localhost:3000/ : frontend 



exo4 : 

* http://localhost:5000/health
* http://localhost:5000/users












