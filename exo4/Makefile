NAME=exo4


DC=docker compose -p $(NAME)


GEN_DIRS=node_modules __pycache__ .pytest_cache

all:
	$(DC) up --build

clean:
	$(DC) down

fclean:
	$(DC) down --rmi all

purge:
	$(DC) down -v

purge_bdd:
	$(DC) down -v

purge_all:
	$(DC) down --rmi all -v
	docker network prune -f
	rm -rf $(GEN_DIRS)

re:
	make purge
	make all

