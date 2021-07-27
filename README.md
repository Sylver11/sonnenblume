# Sonnenblume

## Dependencies
1. Python >= 3.8
2. MySQL == 8
3. [Poetry](https://github.com/python-poetry/poetry) 



## Development Setup
Add a .env file at the root of the application with the following contents:
SQLALCHEMY_DATABASE_URI=<db conn string>  
`poetry install`
Once successful you may run:  
`poetry run start`  


## Database Migrations
`poetry run alembic init alembic`
