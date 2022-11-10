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
    
visit http://tuffix-vm, you will there will be an authentification dialog.

<img width="1223" alt="image" src="https://user-images.githubusercontent.com/98377452/200998703-dbe7bab7-2e57-4200-8a45-55154ff4e5c7.png">
