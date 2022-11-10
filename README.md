# CPSC-449-project2-practice

The implementation of User Authentification.

# Instructions

1. Set up the nginx server

    cd /etc/nginx/sites-enabled
    
    sudo vim tutorial

2. Updating the tutorial file, see tutorial-user-authentification

    sudo service nginx restart
    
3. Start User (port: 5000) and Game (port: 5100) Service.

    foreman start
    
visit http://tuffix-vm, you will see there the authentification dialog will be shown if you have not logged in.

<img width="1223" alt="image" src="https://user-images.githubusercontent.com/98377452/200998703-dbe7bab7-2e57-4200-8a45-55154ff4e5c7.png">

# Features

You will be able to register without authentification.

try http://tuffix-vm/register?username ='yourusername' & password = 'yourpassword'

You won't be able to visit other API unless you pass the authentification.

# API

See http://tuffix-vm/docs

Note: 

1. The User API won't be in this docs.

2. The username is not required to pass in to the game service. We can get the username after authentification.

API List (We are Project 2 Now):

1.  Start a new game
    
Project 2: http://tuffix-vm/startgame

Project 1: http://localhost:5000/startgame?username=jacob

2. Guess a word

Project 2: http://tuffix-vm/guess?game_id=1&word=guess

Project 1: http://localhost:5000/guess?username=jacob&game_id=1&word=mixed

3. List all game of an user

Project 2: http://tuffix-vm/allgame

Project 1: http://localhost:5000/allgame?username=jacob

4. Retrieve a game with the game_id

Project 2: http://tuffix-vm/retrievegame?game_id=1

Project 1: http://localhost:5000/retrievegame?game_id=1

