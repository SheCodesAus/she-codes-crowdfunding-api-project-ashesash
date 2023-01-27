# Pawful - Everybody deserves a friend

<img src="pawful-logo.png" alt="Pawful wireframe" width="300" height="auto"> 

### Pawful will be a crowdfunding website for people who are differently able, old or from low income households. It's also open to animal shelters struggling to keep their centres alive and retirement homes looking to adopt lots of pets. A crowdfunding project can be starting pending that the pets can be homed comfortably. 
### In second phase we will partner with animal shelters to make it easier for organizations/people looking shorter term options (fostering or for small petting events) and offer easier crowdfunding for such events.

## Built With:

- [Django Framwork](https://docs.djangoproject.com/en/)
- [MySqlClient Database](https://pypi.org/project/mysqlclient/)
- [Soft UI Design System](https://github.com/app-generator/django-soft-ui-design)
- [HTML, CSS, JS, Bootstrap....](https://www.w3.org/)

## Installation and Run project:

1- Download or Clone the project

2- Install python on your machine

- [Download from here](https://www.python.org/downloads/windows/)
- [check your version]

  ```bash
  python --version
  ```

  \*\* must be v.3 or up

- [install and upgrade pip]

  ````bash
  python3 -m pip install --upgrade pip

3- run your mysql server and create new Schema in your DBMS with name "crowdfunding" or change the name at (setting.py) and set your DB Server information [ host name and password ]

4- Open the project in vs Code

5- In a Terminal window run the following >>

- [install VirtualEnvironment]
  ```bash
  pip3 install virtualenv
  ```
- [Create and Activate VirtualEnvironment]

  ```bash
  virtualenv venv
  ```

  for win

  ```bash
  venv\Scripts\activate
  ```

  for mac/linux

  ```bash 
  source .venv/bin/activate
  ```

- [Install requirments]
  ```bash
  pip3 install -r requirements.txt
  ```
- [Install mysqlClient]
  ```bash
  pip3 install mysqlclient
  ```

6- Set These Values in "setting.by" file to test Verification using email

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'MANKRA42TEAM@gmail.com'  
EMAIL_HOST_PASSWORD = 'Mankra12345*'
EMAIL_PORT = 587

\*\* or you can add your [gmail] but insure that the account security not activated :D

7- put the 'index.py' file to this path '.venv/Lib/site-packages/django/templatetags/'

8- go to this path '.venv/Lib/site-packages/django/conf/global_settings.py'

- search for [PASSWORD_HASHERS] list
- add this 'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher' in the first of this list

9- Run the following to load Data base

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

10- create your superuser [admin] to access [Admin Dashboard]

```bash
python3 manage.py createsuperuser
    > enter user name
    > enter user email
    > enter password
```

11- After All is Finished run server

```bash
	python3 manage.py runserver
```

\*\* take the link (http://127.0.0.1:8000/) and put it on your browser
</br></br>

<ins>User Account (crowfund starter)</ins>
- username
- password
- email address
- organisation (optional)

<ins>Organisation Account</ins>
- organisation
- password
- email

<ins>User Account (pledger)</ins>
- username
- password
- email address
- funds pledged to

<ins>Fund/Project</ins>
- project name 
- owner
- description
- images
- goal amount
- date until funds can be given
- project updates
- when project was created
- on going fundraiser (optional)
- ability to return funds if fundraiser fails

<ins>Pledges</ins>
- amount
- project to be pledged to
- pledger
- anonymous/not
- comment
- ability to withdraw a pledge

<ins>Database Schema</ins>
</br>
 <img src="pawfuldatabase.png" alt="Pawful database schema" width="700" height="auto"> 
 </br>
 </br>

<ins>Wireframe</ins>
</br>
 <img src="pawfulwireframe.png" alt="Pawful wireframe" width="700" height="auto"> 
 </br>
 </br>
 
 <ins>Colour palette</ins>
 </br>
 <img src="pawfulcolours.png" alt="Pawful Colour Scheme" width="700" height="auto"> 
 
<ins>API Specifications</ins>

