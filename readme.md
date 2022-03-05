# Data Engineering Project : Sentiment Analysis Application

## Link to the AirTable
### Trello link : https://trello.com/b/HUO4qf0t/dataengineering

## Run the docker image

#### To run our image, you will have to open a terminal and run this command line:
```cmd
docker run -p 5000:5000 trahern/app:data_engineering_web
```

#### If this command line doesn't work, try to login using the following line:
```cmd
docker login
```

#### Then you will have to go to your [localhost](http://localhost:5000) to get on the webapp.

## Building the container locally
#### I you prefer to have the project built locally, you can use:
```cmd
docker build -t "data-engineering-project" .
```

#### It will run the tests and create the web app on the [localhost](http://localhost:5000)
Then you'll juste have to run the command line :
```cmd
docker run -p 5000:5000 data-engineering-project
```

#### Or you can clone the [git](https://github.com/Tr4hern/Data_Engineering), go to the place where you saved it using your terminal and do:
```cmd
docker-compose up
```

## Running the tests alone

#### If you want to only run the tests, you may need to get the project locally (check the previous part).
When you have it, go to the place where you saved (you need to be in the "work" directory) it using your terminal and run the command line:
```cmd
pytest ./unit_tests.py
pytest ./integration_tests.py
pytest ./functionnal_tests.py
pytest ./end-to-end_tests.py
```
#### You may need to install some python libraries, using:
```cmd
pip install -r requirements.txt
```
#### For the different localhost, we have :
- #### localhost:5000 for the app
- #### localhost:9090 for prometheus
- #### localhost:8010 for the metrics of prometheus
- #### localhost:3000 for grafana

#### The different metrics to monitor on grafana are :
- ####  for cpu usage
- ####  for memory usage
- ####  for disk space usage
- ####  for response time
- ####  for requests count
- ####  for exceptions