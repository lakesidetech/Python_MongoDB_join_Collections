# Python_MongoDB_join_Collections
## Join two tables aka documents in MongoDB using Python3
* This is a sample MongoDbB in Python application intended to provide a working example of hospital data for Doctors and Hospitals presented in tables/documents. An output based on two tables (documents) using a join is generated to combine the two separate documents into one. The goal of this application is to create the documents using Python and store the data in MongoDb Compass (local) and MongoDB Atlas.
# QUICK START:
* install Python if needed
* Install MongoDB Compass and Atlas
* Test if you can see the DB in both Compass and Atlas
* pip install pymongo
* pip install DNSPYTHON
* Import PyMongo

## #connect the heatlthy DB to localhost
** myclients = pymongo.MongoClient('mongodb://localhost:27017/')
** mydb = myclients['M_healths']
## connect the heatlthy DB to MongoDB Atlas
myclients = pymongo.MongoClient('mongodb+srv://ruth:joram%401934@cluster0.efu2u.mongodb.net/M_healths?retryWrites=true&w=majority')

## input hospital table
mycol = mydb["Hospitals"]

![image](https://user-images.githubusercontent.com/17750481/112547524-e97b9500-8dcb-11eb-8b49-9360ad3d3ad0.png)
## input Doctors table
![image](https://user-images.githubusercontent.com/17750481/112547681-2182d800-8dcc-11eb-8862-6e67fb106152.png)

