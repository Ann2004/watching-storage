# Bank security console

This is an internal repo for employees of the "Siyaniye" bank. If you got in here by accident, you won't be able to run it because you don't have access to DB, but you can use freely this code or see how database queries are implemented. 

Bank security console is a site that can be connected to a remote database with visits and pass cards of our bank employees.

### How to install

Create a `.env` file in the project directory and add your DB host, password, port, name, user and site secret key:
```
DB_HOST=your_db_host
DB_PASSWORD=password
SECRET_KEY=your_sectret_keyview the preview side-by-side
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_user
```

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Example usage

Run from the command line:
```
python manage.py runserver 0.0.0.0:8000
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).