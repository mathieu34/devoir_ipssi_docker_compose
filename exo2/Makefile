NAME=exo1

all:
	docker compose up --build

clean:
	docker compose down

fclean:
	docker compose down --rmi all --volumes --remove-orphans

re: fclean all

purge:
	docker volume rm ipssi_docker_3_sqlite_data || true


