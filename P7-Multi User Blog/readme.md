# Multi-User Blog 

**Multi-User-Blog** is a blogging platform designed to be hosted on Google
App Engine. User's can securely sign-up, login, create posts, comment on
posts, and like posts. The platform provides appropriate user permissions and
security measures.

Click here to be taken to
(https://udacity-gg.appspot.com/).

## Setup:
, and making sure
that Python 2.7x is installed.  Then install and then initialize the
Google Cloud SDK.

- Begin the setup by cloning all files to the same directory


- [install google app engine](Detailed Instructions can be found here:
[Google App Engine Documentation](https://cloud.google.com/appengine/docs/python/getting-started/creating-guestbook)


- create app in [Developer Console] You'll need to create a new Google Cloud
Platform Console project or retrieve the project ID of an existing project
from the Google Cloud Platform Console.(https://console.developers.google.com/)


- run locally In the terminal navigate to the directory where the cloned files are located
and run the following command:`dev_appserver.py app.yaml`,This will deploy your application locally. You can access it by typing
http://localhost:8080 in your browser. The terminal window will now log all
the interactions of this local server which is helpful for debugging.
For additional information visit:
[Using the Local Development Server](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server)

- browse locally via [http://localhost:8080](http://localhost:8080)
- set project `gcloud config set project PROJECT_ID`
- deploy app `gcloud app deploy`
- browse app `gcloud app browse`




## Attribution

This project was written for the Udacity Full-Stack Nanodegree

