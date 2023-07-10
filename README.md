# django-register-app

## Some Django commands
```python
django-admin startproject project
django-admin startapp app 
python manage.py runserver
```

Build the Docker image and start the application:

```bash
docker-compose up
```

Run Django migrations to setup your database:

```bash
docker exec -it <your_web_container_id> python manage.py migrate
```

To access the app: http://127.0.0.1:8000/


Access the PostgreSQL container:

```bash
docker exec -it <your_postgres_container_id> bash
psql -U myuser -d mydatabase
```






![im0407202301](https://github.com/SabrinaMacaluso/django-register-app/assets/104983001/e4d6ca25-ba50-44cd-93a8-d57ad9f0e8e0)
![im0407202302](https://github.com/SabrinaMacaluso/django-register-app/assets/104983001/efc22c16-3b4e-458b-ac82-980e2549d14d)
![im0407202303](https://github.com/SabrinaMacaluso/django-register-app/assets/104983001/5bd0ba2e-79d0-4a24-b6e1-d1f1484ca175)
