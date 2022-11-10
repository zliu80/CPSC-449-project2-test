# CPSC-449-project2-practice

The implementation of User Authentification and Game Service.

# Split into two services.

user.py is for User Service, database userdb file in var/primary/mount/

game.py is for Game Service, database gamedb file in var/primary/mount/

# Instructions

1. Set up the nginx server

        cd /etc/nginx/sites-enabled
    
        sudo vim tutorial

2. Updating the tutorial file, see tutorial-user-authentification, this file is under the root.
       
        server{
            listen 80;
            listen [::]:80;
            server_name tuffix-vm;

            location / {
                    auth_request /auth;
                    auth_request_set $auth_cookie $upstream_http_set_cookie;
                    auth_request_set $auth_status $upstream_status;
                    proxy_pass http://localhost:5100;
            }

            location = /auth {
                    internal;
                    proxy_pass http://localhost:5000;
                    proxy_pass_request_body off;
                    proxy_set_header Content-Length "";
                    proxy_set_header X-Original-URI $request_uri;
                    proxy_set_header X-Original-Remote-Addr $remote_addr;
                    proxy_set_header X-Original-Host $host;
            }

            location ~ ^/(login|login_required|logged-in|logout)$ {
                    proxy_pass http://localhost:5000;
                    proxy_set_header X-Original-URI $request_uri;
                    proxy_set_header X-Original-Remote-Addr $remote_addr;
                    proxy_set_header X-Original-Host $host;
            }

            location = /css/skeleton.css {
                    proxy_pass http://localhost:5000;
            }
        }

    After updating tutorial, restart nginx

        sudo service nginx restart
    
3. Start User (port: 5000) and Game (port: 5100) Service.

        foreman start
    
visit http://tuffix-vm, you will see the authentification dialog if you have not logged in.

<img width="1223" alt="image" src="https://user-images.githubusercontent.com/98377452/200998703-dbe7bab7-2e57-4200-8a45-55154ff4e5c7.png">

# User API

There are only two API. 1). auth 2). register

In order to visit the game service, you must pass the authentification (all game API require auth).

However, you will be able to register without authentification.

try http://tuffix-vm/register?username ='yourusername' & password = 'yourpassword'

# Game API

See http://tuffix-vm/docs

Note: 

1. The User API won't be in this docs.

2. The username is not required to pass in to the game service. We can get the username after authentification.

API List (We are Project 2 Now):

1.  Start a new game
    
Project 2: 

    http://tuffix-vm/startgame

Project 1: 

    http://localhost:5000/startgame?username=jacob

2. Guess a word

Project 2: 

    http://tuffix-vm/guess?game_id=1&word=guess

Project 1: 

    http://localhost:5000/guess?username=jacob&game_id=1&word=mixed

3. List all game of the current user

Project 2: 

    http://tuffix-vm/allgame

Project 1: 

    http://localhost:5000/allgame?username=jacob

4. Retrieve a game with the game_id

Project 2: 

    http://tuffix-vm/retrievegame?game_id=1

Project 1: 

    http://localhost:5000/retrievegame?game_id=1


