# django Scaffold

## Run Project

### 1、Sync your database for the first time:

```bash
python manage.py migrate
```

### 2、we will also create an initial user named `admin` with a password of `admin123456`.We will authenticate as that user later in our example:

```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

### 3、Install requirements
```bash
pip install -r requirements.txt
```


### 4、Run project in development environment
```bash
python manage.py runserver
```



## Features

- JWT
- OAuth2
- Pagination
- Versioning
- Filtering
- Custom Exception
- Custom Permission
- Custom Renderer
- Response
- XAdmin
- Model Permission
- Object Permission