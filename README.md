# KaBuM-backend-challenge
> API REST
> [Description of challenge](https://github.com/kabum/testes-kabum/blob/master/Teste%20Back-End%201/README.md)

## Modules

- [Python](https://www.python.org/downloads/) - Programming Language,
- [Flask](https://flask-restplus.readthedocs.io/en/stable/) - The framework used,
- Blueprint - A template for generating a view of api for docummentation and tests,
- Pip - Dependency Management.

## Virtual environments (Linux)
- install [Python](https://www.python.org/downloads/)
```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
```
Install all project dependencies using:
```
$ pip install -r requirements.txt
```
Runing
```
$ python app.py
```
## Virtual environments (Windows)
- install [Python](https://www.python.org/downloads/)
```
$ pip install virtualenv
$ python -m venv venv
$ . venv\Scripts\Activate.ps1
```
Install all project dependencies using:
```
$ pip install -r requirements.txt
```
Runing
```
$ python app.py
```
# Virtual environments (Docker)
- install [Docker](https://www.docker.com/)
- dockerfile: Dockerfile in this repository

## commands docker
```
docker build --tag docker-app-kabum .   
docker run -p 2300:5000 -d docker-app-kabum   
```
**router is this case: ```http://localhost:2300/api/fretes```

# Router API

## - Server 
port=5000 \
host=0.0.0.0 (localhost) 

## - Route 
- Create user \
[Method=POST]\
[Request URL] = ```http://localhost:5000/api/fretes``` \
Mode: 
```
{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}
```

# Documentation and test environment
- [DOC] http://localhost:5000/api/doc
![image](https://user-images.githubusercontent.com/25828944/128569785-a4f6dd99-11fd-4226-b7af-18cbda599702.png)


# Tests

## - Modules
- Pytest - framework makes it easy to write small tests
- pytest-sugar - is a plugin for pytest that shows failures and errors instantly and shows a progress bar.
- httpx - is a fully featured HTTP client for Python

## - Running
```
pytest test_api.py    
```

