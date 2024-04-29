# requirements
python 3.10
docker

# usage 
download to your local machine using git clone command, then change directory and set up postgres in docker container using the following command:
```
docker pull postgres && \
docker run --name postgresql -e POSTGRES_USER=manda -e POSTGRES_PASSWORD=mandapass -e POSTGRES_DB=mandadb \
-p 5432:5432 -d postgres
```
install requirements in virtual environment and execute script:
```
python3 main.py
```

and that's it, you can verify script has been executed going into postgresql container
```
docker exec -it postgresql psql -U manda -d mandadb 
```
and listing all tables in the database
```
\dt
```
enjoy
