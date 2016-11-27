# Udacity Full Stack: Linux Server Config
This README contains instructions to set up a new Linux server instance to deploy flask applications. 

project url http://ec2-35-162-237-210.us-west-2.compute.amazonaws.com/

Developed by "yasser al-barbary"


.. ssh into new dev environment as root

-- install Software/Packages

- finger "sduo apt-get install finger"
- Apache2 "sduo apt-get install Apache2"
- mod_wsgi "sduo apt-get install mod_wsgi"
- pip "sduo apt-get install pip"
- virtualenv "sduo apt-get install virtualenv"
- Flask "sduo apt-get install Flask"
- git "sduo apt-get install git"
- PostgreSQL "sduo apt-get install PostgreSQL"
- python-psycopg2 "sduo pip install python-psycopg2"

- libpq-dev "sduo pip install libpq-dev"
- sqlalchemy "sudo pip install sqlalchemy"
- Flask-SQLAlchemy "sduo pip install Flask-SQLAlchemy"
- flask-seasurf "sduo pip install flask-seasurf"
- httplib2 "sduo pip install httplib2"
- requests	"sudo pip install requests"
- google-api-python-client "sduo pip install google-api-python-client"
- fail2ban "sduo pip install fail2ban"
- mailutils "sduo pip install mailutils"
- nagios "sduo pip install nagios"
- oauth2client "sudo pip install oauth2client"
		

## First User Setup

1. Create new development environment through provided Udacity page
2. Create new user "grader"

		adduser grader

3. in /etc/sudoers.d add a file called "grader" 

		cd /etc/sudoers.
		sudo nano grader

type the line in the file "grader" to add sudo priviliges to user grader:

		grader ALL=(ALL) NOPASSWD:ALL
	
4. The instance is set to disallow password logins, and grader does not yet have a public key on the server, so the grader cannot yet log in. 
	we must first generate public key to allow user grader to login

		ssh-keygen

5. Logged in as root on the server,create folder ".ssh" and add permissions for user grader at the folder, run

		mkdir /home/grader/.ssh
		chown grader /home/grader/.ssh
		chgrp grader /home/grader/.ssh

6. Next create the file /home/grader/.ssh/authorized_keys containing the contents of udacityGrader.pub. 
	Set ownership and permissions on the new file and folder and then copy the file content from the root user to the grade user :
	
		cp /root/.ssh/authorized_keys /home/grader/.ssh/
		chown grader /home/grader/.ssh/authorized_keys
		chgrp grader /home/grader/.ssh/authorized_keys
		chmod 644 /home/grader/.ssh/authorized_keys
		chmod 700 /home/grader/.ssh

7. Disallow remote root login and set ssh to a non-default port: change two lines in /etc/ssh/sshd_config to read

		Port 2200
		PermitRootLogin no
	
8. Then restart ssh service,run

		sudo service ssh restart

9. Log out of root and ssh in as grader, using the new port 2200.

### All following commands are run as grader
The default instance is configured with a hostname which does not match the actual public URL. This will cause the error 
"sudo: unable to resolve host ip-xx-xx-xx-xxx" 
to be printed every time you run a command.
 Configuring the server with the correct hostname will correct this problem. 
 Set the server's hostname by editing the file /etc/hostname and replacing the current name with the server's public URL, 
 in this case "ec2-35-162-237-210.us-west-2.compute.amazonaws.com".

## Update installed packages with user grader

	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get autoremove
	
## Set timezone and set up time synchronization

		sudo dpkg-reconfigure tzdata

Select "None of the Above" and then "UTC".
Next, install and configure ntp for network time synchronization. Run

		sudo apt-get install ntp
	
The default ntp servers are sufficient, otherwise we could edit /etc/ntp.conf to add or remove servers. 
The ntp daemon is started during the installation process. If changes are made to /etc/ntp.conf, reload ntpd by running

		sudo service ntp reload

## Configure ufw firewall
Lock down all ports except those we'll actually use by running

		sudo ufw default deny incoming
		sudo ufw default allow outgoing
		sudo ufw allow 2200/tcp
		sudo ufw allow 80/tcp
		sudo ufw allow 123/udp
		sudo ufw enable


Test the apache2 install by visiting the server IP in a browser.
 An Apache default page should appear. With default settings, 
 apache will serve content from /var/www/html for any request it receives. 
 If the server needs to serve different content based on the address by which it is accessed, 
 additional <VirtualHost> directives must be added to the conf files in the /etc/apache2/sites_enabled directory. 
Next, install the tools that enable apache to work with python.

		sudo apt-get install python-setuptools libapache2-mod-wsgi

## cogifure  Flask 
		
		sudo apt-get install libapache2-mod-wsgi python-dev
		sudo a2enmod wsgi 
		cd /var/www
		sudo mkdir "FlaskApp"---or your app name any name
		cd "FlaskApp"---or your app name any name
		sudo mkdir FlaskApp
		cd FlaskApp
		sudo mkdir static templates
		sudo a2dissite 000-default
		sudo nano __init__.py 
		
			--Add following logic to the file:

				from flask import Flask
				app = Flask(__name__)
				@app.route("/")
				def hello():
					return "Hello, I love Digital Ocean!"
				if __name__ == "__main__":
					app.run()
		
		sudo virtualenv venv
		source venv/bin/activate 
		sudo python __init__.py
		deactivate
		
		sudo nano /etc/apache2/sites-available/FlaskApp
		sudo nano /etc/apache2/sites-available/FlaskApp.conf
		
			--Add the following lines of code to the file to configure the virtual host. 
			Be sure to change the ServerName to your domain or cloud server's IP address:

				<VirtualHost *:80>
						ServerName mywebsite.com
						ServerAdmin admin@mywebsite.com
						WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
						<Directory /var/www/FlaskApp/FlaskApp/>
							Order allow,deny
							Allow from all
						</Directory>
						Alias /static /var/www/FlaskApp/FlaskApp/static
						<Directory /var/www/FlaskApp/FlaskApp/static/>
							Order allow,deny
							Allow from all
						</Directory>
						ErrorLog ${APACHE_LOG_DIR}/error.log
						LogLevel warn
						CustomLog ${APACHE_LOG_DIR}/access.log combined
				</VirtualHost>

				
		sudo a2ensite FlaskApp
		cd /var/www/FlaskApp
		sudo nano flaskapp.wsgi 
		
			--Add the following lines of code to the flaskapp.wsgi file:

				#!/usr/bin/python
				import sys
				import logging
				logging.basicConfig(stream=sys.stderr)
				sys.path.insert(0,"/var/www/FlaskApp/")

				from FlaskApp import app as application
				application.secret_key = 'Add your secret key'

		sudo service apache2 restart 


## Install and configure PostgreSQL

		sudo apt-get install postgresql postgresql-contrib
	
Set a password for the newly created postgres linux user to access the postgres database. First, open a postgres prompt as the postgres user by running

		sudo -u postgres psql postgres
	
then type

		\password postgres
	
and enter a new password twice. Then exit the postgres prompt by typing

		\q

Create a new postgres user called catalog and a new database, also called catalog, by running

		sudo -u postgres createuser -P --interactive
		sudo -u postgres createdb -O catalog catalog
	
In the first command, the -P flag will immediately prompt for a password for the new user, and --interactive will ask questions about the rights granted to the new user. Answer 'n' to all of these since the catalog user only needs to access a single database, and it's already been created. In the second command, -O creates the new db with owner catalog. Next, lock down the new db.

		sudo -u postgres psql catalog
		REVOKE ALL ON SCHEMA public FROM public;
		GRANT ALL ON SCHEMA public TO catalog;
		\q

		

## Clone the Catalog app repo

		git clone https://github.com/yasser888/udacity_catalog.git

Move the entire contents of the new folder into the /var/www/FlaskApp/FlaskApp directory created earlier, and delete the now-empty folder. Hide the .git repository from public view by creating a new .htaccess file in the same directory, with the contents

		RedirectMatch 404 /\.git

Since the client\_secrets.json file should not be in the public repo, copy its contents into a new file of the same name in /var/www/FlaskApp, then provide absolute links to it in the catalog.py app. This directory is not web-accessible, so client\_secrets.json is protected from public view. Now all files are in place, and some edits are required.

## Modify catalog app to use PostgreSQL
In the catalog app files, replace all instances of

		engine = create_engine('sqlite:///catalog.db')

with 

		engine = create_engine('postgresql://catalog:Your_PASSWORD@localhost/catalog')

Rename the main application.py app file to \_\_init\_\_.py.

## Start the app

		sudo service apache2 restart
		
## Update OAuth2 settings
Visit the console of any third-party auth providers and update the authorized addresses to include the new hostname.

## Open the new hostname in a web browser
For my catalog app, visit [Udacious Musical Instruments](http://ec2-35-162-237-210.us-west-2.compute.amazonaws.com/).

## Resources
In addition to the pages linked above, thanks are due to the following authors of extremely helpful resources:

* [Keenan Payne](http://blog.udacity.com/2015/03/step-by-step-guide-install-lamp-linux-apache-mysql-python-ubuntu.html)
* [allan](https://discussions.udacity.com/t/markedly-underwhelming-and-potentially-wrong-resource-list-for-p5/8587)
* [stueken](https://github.com/stueken/FSND-P5_Linux-Server-Configuration)
* [kirkbrunson](https://discussions.udacity.com/t/project-5-resources/28343)
* [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [github](https://github.com/Scienxe/udacity-linux)







