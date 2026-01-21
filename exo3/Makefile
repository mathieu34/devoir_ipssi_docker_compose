NAME=exo3


DC=docker compose -p $(NAME)


all:
	$(DC) up --build

clean:
	$(DC) down

fclean:
	$(DC) down --rmi all

purge:
	$(DC) down -v

re:
	make purge
	make all




