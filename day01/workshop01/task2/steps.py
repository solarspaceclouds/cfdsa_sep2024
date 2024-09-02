# # image name: stackupiss/northwind-app:v1

# The application consists of the following 2 parts
# a. myapp – this is a Node based web application. It connects to a database;
# the database configuration is as follows
docker volume create data-vol
# i. DB_HOST is the database server
# ii. DB_USER is root
# iii. DB_PASSWORD is changeit
# Use the image stackupiss/northwind-app:v1
# b. mydb – this is the database that your application will be using. Use the
# following image stackupiss/northwind-db:v1
# c. Deploy the 2 containers inside a network called mynet.

docker run -d --mount type=volume,source=db-vol,target=/var/lib/mysql -e MYYSQL_ROOT_PASSWORD=abc123 mysql:8

# Port bind myapp to port 8080; however, mydb should not be accessible
# from within the mynet subnet
# Don’t forget to set the DB_HOST environment variable to the Node
# application (myapp) container.

DB_HOST=myapp 


# d. In order to preserve the database when mydb is deleted, you should create
# a volume for mydb and mount the volume to /var/lib/mysql path.Docker Workshop
# Duration: 120 mins
# Containers for Deploying and Scaling Apps
# e. Deploy your application and access it with the Docker host IP address
# Create a file called steps.txt and record the Docker commands you used to
# deploy this application


docker volume create data-vol
docker network create mynet 
docker run -d --name=mydb --network=mynet --mount type=volume,source=data-vol,target=/var/lib/mysql stackupiss/northwind-db:v1

docker run -d -p 8000-9000:3000 --network=mynet \
    -e DB_HOST=mydb \
    -e DB_USER=root \
    -e DB_PASSWORD=changeit \
    stackupiss/northwind-app:v1

# is assigned localhost:8000 or 127.0.0.1:8000
# or use hostname -I to  get can use this IP address to access Docker containers from another device on the same network. e.g. 172.19.0.1 