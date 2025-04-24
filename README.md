# End-to-End-Book-Recommanded-System

# Successfull Lunch On AWS
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/Book%20Recommedation%20System/1.Successfully%20lunch%20on%20aws.png)

# Successfully Trained
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/Book%20Recommedation%20System/2.Successfully%20trained.png)

# Successfully Recommended Books
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/Book%20Recommedation%20System/3.Successfully%20recommed%20book.png)

Python version 3.7

# Work Flow
1. Create Exception Handling and write code
2. Create Logger file for log and write code
3. Create Utils file and write code
4. Create Constant and write code
5. Create config.yaml and write code
6. Create entity and write code
7. Create configuration and write code
8. Stage 1 Data Ingestion
9. Training Pipeline
10. main.py

1. config.yaml update
2. entity update
3. configuration update
4. Stage 2 DataValidation
5. Update Training Pipeline
6. run Main.py

1. config.yaml update
2. entity update
3. configuration update
4. Stage 3 Data Transformed
5. update Training Pipeline
6. run main.py

1. config.yaml update
2. entity update
3. configuration update
4. Stage 4 model trainer
5. update Training Pipeline
6. run main.py

1. config.yaml update
2. entity update
3. configuration update
4. App.py update
5. run app.py

## For local Now run,
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t durgeshsingh12712/bookapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 durgeshsingh12712/bookapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push durgeshsingh12712/bookapp:latest 
```

```bash
docker rmi durgeshsingh12712/bookapp:latest
```

```bash
docker pull durgeshsingh12712/bookapp
```