# NYC-property-sales-etl


## How To Use

To clone and run this project, you'll need the prerequisties installed on your computer. From your command line:

```bash
#Clone / create project repository:
$ cd myproject

#Type git clone, and then paste the URL you copied in Step 2.
$ git clone https://github.com/JoshuaAcosta/NYC-property-sales-etl.git

#Install from Pipfile, if there is one:
$ pipenv install

#activate the Pipenv shell:
$ pipenv shell

#set up env variables in .env file
FLASK_APP=api
FLASK_ENV=development
DATABASE_URL= ADD YOUR DATABASE PATH HERE
SECRET_KEY= ADD YOUR SECRET KEY

#run etl scripts
$ cd etl
$ python extract_data.py
$ python load_data.py
$ python transform_data.py

```