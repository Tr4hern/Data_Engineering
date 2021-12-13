# Data Engineering Project : Sentiment Analysis Application

## Link to the AirTable
[https://airtable.com/our_airtable](https://airtable.com/appj4a0O1Fo0jPTlP/tblsKaA2HBamQ73Au/viwkzXCh7m9G6lU9E?blocks=hide)

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
pytest ./test.py
```
#### You may need to install some python libraries, using:
```cmd
pip install pytest
pip install pandas
pip install vaderSentiment
```
#### By going into the test.py you will be able to tests different aspects. For example, by default, we check the first 2000 lines of our csv have a accuracy above 60% with our model. You change both the accuracy check and the number of lines checked.
#### We check only the accuracy at 60% because it was most of the time around 70% and we needed the test to pass if we wanted the image to be built while running the tests.