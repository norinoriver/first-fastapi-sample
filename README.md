# FastAPI Initializer at VSCode

1. create .venv
```
pwd 
$ `your-device-path`/fastapi-init-vscode
mkdir .venv
ls -a | grep .venv
$ .venv

```
2. let's install module by poetry 
```
poetry install
```

# Run Docker
## develop
### run
```
docker-compose -f ./dockerfiles/docker-compose-dev.yaml --env-file ./dockerfiles/.dockerenv/dev.env up
```

### into mysql
```
docker-compose -f ./dockerfiles/docker-compose-dev.yaml --env-file ./dockerfiles/.dockerenv/dev.env exec db mysql demo -u root -p
```

### into redis
```
docker-compose -f ./dockerfiles/docker-compose-dev.yaml --env-file ./dockerfiles/.dockerenv/dev.env exec redis redis-cli
```

### migrate_db
```
python -m api.migrate_db -e ./dockerfiles/.dockerenv/dev.env
```

## stg
### run stg
```
docker-compose -f docker-compose-stg.yaml --env-file ./dockerfiles/.dockerenv/stg.env up
```

### into mysql 
```
docker-compose -f ./dockerfiles/docker-compose-stg.yaml --env-file ./dockerfiles/.dockerenv/stg.env exec db mysql demo -u root -p
```

### into redis
```
docker-compose -f ./dockerfiles/docker-compose-stg.yaml --env-file ./dockerfiles/.dockerenv/stg.env exec redis redis-cli
```

## prod
### run prod
```
docker-compose -f docker-compose-prod.yaml --env-file ./dockerfiles/.dockerenv/prod.env up
```

### into mysql 
```
docker-compose -f ./dockerfiles/docker-compose-prod.yaml --env-file ./dockerfiles/.dockerenv/prod.env exec db mysql demo -u root -p
```

### into redis
```
docker-compose -f ./dockerfiles/docker-compose-prod.yaml --env-file ./dockerfiles/.dockerenv/prod.env exec redis redis-cli
```