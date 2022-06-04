##Prerequisites
* Check python version (python --version)
* Check pip version (pip --version)
* Check django version (django-admin --version)
##The best way is to install DJANGO in separte virtual environment wrapper instead of GLOBALLY.

*Check Python version in your computer by command(python --version)
*Then create virtual environment by command (pip install virtualenv) (inside the folder where you want to create project)
*Then for each project create virtual environment by command (virtualenv any_env_name) This will create a folder inside 
 the project folder with (supplied name) any_env_name
*To activate that virtualenv cd your_virtual_env enter then scripts\activate enter
*You will see like (firstenv) E:\PYTHON\Django\FirstProject\firstenv>  which means your virtualenv is active
*Now install Django package by command (pip install django) Make sure to connected with internet
*Check Django version by command  (python -m django --version)
*To create django project use command (django-admin startproject your_project_name) This will create a folder with name 
 your_project_name and inside a folder with the same name
*To avoid one folder give command as (django-admin startproject your_project_name .  then hit enter){Recommended}
*To create app give command as (django-admin startapp your_app_name)
*To start server give command as python manage.py runserver
*To work with MySql run command ((firstenv) E:\PYTHON\Django\learning>pip install mysqlclient)

##Steps to install django in separte virtual environment(VE)
* To create virtual env wrapper (pip install virtualenvwrapper-win)
* To create virtual env (mkvirtualenv any_env_name)
* To activate this virtual env (workon your_virtual_env)
* To get list of all VE (lsvirtualenv)
* Now install django (pip install django) This will install dgango in that VE
=====================Uninstall==============================
* Globally uninstall django (pip uninstall django)
* If inside VE then first activate that VE using workon then give above command
* To remove VE (rmvirtualenv env_name)
* To remove wrapper (pip uninstall virtualenvwrapper-win)
===================================================

##Steps to install django Globally
* To install django (pip install django) This will install dgango Globally
=====================Uninstall==============================
* Globally uninstall django (pip uninstall django)
===================================================
# To create project (django-admin startproject your_project_name)
# To create project (django-admin startproject your_project_name .) this will no create one extra directory withproject name
# To run that project (py manage.py runserver)
# If you want to run on any other port number than (py manage.py runserver 5555)
# To create app (py manage.py startapp your_app_name)

#ORM
==========================================
* Query set allow us to interact with our database and perform curd operations
* ORM(object relational mapper) used to create schema of table from python class and object, 
  If we use ORM than we don't need to worry about which database we are using it may be oracle mysql postgress etc.
  Django ORM will convert it automatically in their format.
* Every class inside a model.py corresponds to a table in DB
* Use command (py manage.py makemigrations) to create migration files for the table in migration folder of the created apps
* Use command (py manage.py sqlmigrate your_app_name migration_file_name ex: oooo1) to display the SQL statement for 
  the migration
* Use command (py manage.py migrate) to create the tables in DB
* Use command (py manage.py showmigrations) to display all the migrations and its status
* Whenever we need to change any column or add, delete column than do that changes in model.py file inside the respective class. 
  Then use commands (py manage.py makemigrations) it will create new migration file in migration folder based on new changes.
  Then use command (py manage.py migrate) to update the tables in DB
* To see table in sqlite install https://nightlies.sqlitebrowser.org/latest/ (DB.Browser.for.SQLite-win64.msi)

#Admin
=========================================================
To access admin pannel we have to create superadmin
* Use command (py manage.py createsuperuser) to create super user
	Username: admin
	Email address: admin@gmail.com
	Password: admin@123

#from below path you can see all models and form of django which is created by default and follow the same
C:\Users\Dharmendra\Envs\learn\Lib\site-packages\django\contrib\auth\forms.py





 

































