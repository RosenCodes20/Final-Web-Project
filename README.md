# Football Team Manager

If you are a big fan of football or want to experience the feeling of being football coach you can try this.

You are a football coach and you want to make your dream football team but first login :).

After you login you are free to create schemes, leagues, players and teams.

You also have a profile that you can edit :).

### And the most important thing is to have fun 😁.

Let me tell you how to run this code.

### 1.Clone this repository
```terminal
git clone https://github.com/RosenCodes20/Final-Web-Project
```

### 2.Open the project

### 3.Create venv (if not created)

``` terminal
python -m venv venv
```

### 4.Install dependencies
```terminal
pip install -r requirements.txt
```


### 5.Setup the database in the evn file (it should be hidden)

### 6. Run the migrations

``` terminal

python manage.py migrate

```

### 7.Run the project
``` terminal

python manage.py runserver

```


# Additional functioanilities and user permittions

If you are unuathenticated user you have only get permissions and cannot post anything

After you login you are able to create scheme which will be your dream team scheme.

I choosed the most 4 popular schemes for you to try.

When you create scheme, you create League. It should be football league as Premier League, LaLiga and etc.

After that you create team from this league. For example Barcelona is from LaLiga.

And last you create player who you can see on the scheme, and edit and delete. 😊
