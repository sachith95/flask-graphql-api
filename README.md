CREATE AN ENVIROMENT

Create a project folder and a venv folder within:
> mkdir myproject
> cd myproject
> py -3 -m venv venv

ALLOW SCRIP EXECUTION
Set-ExecutionPolicy Unrestricted -Scope Process

Activate the environment

> venv\Scripts\activate

Install Flask
pip install Flask Flask-SQLAlchemy Ariadne Flask-Cors
pip install mysqlclient