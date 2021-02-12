# **Expensis project**
Expensis is open-source project created to control Your finances.  
This repository is server part - created using Python and Django.  
It consists of multiple REST API endpoints. It is divided into 5 applications - each with its own documentation:
* **expenses** - managing expenses, [*docs*](https://github.com/PKapski/Expensis-server/tree/development/expenses#expenses)
* **stats** - fetching data to analyze expenses, [*docs*](https://github.com/PKapski/Expensis-server/tree/development/stats#stats)
* **authentication** - used for user authentication, [*docs*](https://github.com/PKapski/Expensis-server/tree/development/authentication#authentication)
* **users** - managing user account, [*docs*](https://github.com/PKapski/Expensis-server/tree/development/users#users)
* **commons** - fetching static data like: income ranges, age ranges and categories, [*docs*](https://github.com/PKapski/Expensis-server/tree/development/commons#commons)

Expensis consists of two clients:
* Web application created with Angular, [*link*](https://github.com/PKapski/Expensis-web-client)
* Mobile application created using Android Studio and Kotlin language, [*link*](https://github.com/PKapski/Expensis-mobile)

## Setting up project

**1. Clone the repository**  
`git clone https://github.com/PKapski/Expensis-server.git`

**2. Create your own virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```
**3. Install your requirements**  
`pip install -r requirements.txt`

**4. Config PostgreSQL database**  
Install Postgres, create database.  
Insert your database info into *MainExpensis/config/database_config.py* file.

**5. Apply migrations to Your database**  
`python manage.py migrate`

**6. Create a new superuser**  
`python manage.py createsuperuser`

**7. Run server**  
`python manage.py runserver`  
If You would like to run server on another ip/port, set it in *MainExpensis/config/host_config.py* and run it like:  
`python manage.py runserver <ip>:<port>`