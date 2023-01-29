# Pawful - Everybody deserves a friend

<img src="pawful-logo.png" alt="Pawful wireframe" width="300" height="auto"> 

### Pawful will be a crowdfunding website for people who are differently able, old or from low income households. It's also open to animal shelters struggling to keep their centres alive and retirement homes looking to adopt lots of pets. A crowdfunding project can be starting pending that the pets can be homed comfortably. 
### In second phase we will partner with animal shelters to make it easier for organizations/people looking shorter term options (fostering or for small petting events) and offer easier crowdfunding for such events.

## Built With and technologies used:

- [Django Framework](https://docs.djangoproject.com/en/)
- [Fly.io](https://fly.io/docs/)
- [Insomnia] (https://docs.insomnia.rest/)

## Deployed at:
[Pawful](red-morning-8348.fly.dev)
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

- [Install requirements]
  ```bash
  pip3 install -r requirements.txt
  ```

6- Run the following to load Data base

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

7- create your superuser [admin] to access [Admin Dashboard]

```bash
python3 manage.py createsuperuser
    > enter user name
    > enter user email
    > enter password
```

8- After All is Finished run server

```bash
	python3 manage.py runserver
```

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
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

| Endpoint URL | Action         | HTTP Method | Authorisation     |
| ------------ | -------------- | ----------- | ----------------- |
| /users/      | List all users | GET         | Must be logged in |
| /users/      | Create user    | POST        | N/A               |
| /users/int      | Get user info  | GET         | Must be logged in |
| /users/      |Delete user info| Delete      | Must be logged in |
| /users/      | Update existing instance|PUT | Must be logged in |
| /project/    | Create project | POST        | Must be logged in |
| /project/    | Get project | GET         | Must be logged in |
| /project/int    | Update project detail | PUT         | Must be logged in |
| /project/int      |Delete project| Delete      | Must be logged in |
| /pledges/    | Create pledge | POST        | Must be logged in |
| /pledges/    | Get pledge | GET         | Must be logged in |
| /pledges/int      | Update existing instance|PUT | Must be logged in |
| /pledges/int      |Delete pledge| Delete      | Must be logged in |