include config/$(or $(STAGE),dev)/.env
export


server:
	docker compose up -d --build server