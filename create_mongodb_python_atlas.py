#!/usr/bin/env python
# coding: utf-8

# In[91]:


pip install pymongo


# In[92]:


pip install DNSPYTHON


# In[93]:


import pymongo
#connect the heatlthy DB to localhost
myclients = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclients['M_healths']


# In[94]:


#connect the heatlthy DB to MongoDB Atlas
myclients = pymongo.MongoClient('mongodb+srv://ruth:joram%401934@cluster0.efu2u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


mydb = myclients["M_healths"]

mycol = mydb["Hospitals"]


my_Hospitals_list = [
  { "Hospital_ID": 10, "Hospital_name": "Mama Lucy","Bed_Count":1000,"address": "Mwai Kibaki Rd st 6752"},
  { "Hospital_ID": 20, "Hospital_name": "KNH","Bed_Count":10000,"address": "Kenyatta Avenue 21"},
  { "Hospital_ID": 30, "Hospital_name": "Jaramogi","Bed_Count":5000,"address": "Oginga Odingas Street 345"},
  { "Hospital_ID": 40, "Hospital_name": "Omboo County","Bed_Count":3000,"address": "Migori Town Horuba Est"},
  { "Hospital_ID": 41, "Hospital_name": "Chiromo Lane Medical Center","Bed_Count":2500,"address": "Chiromo Rd Muthithi Rd Westlands"},
  { "Hospital_ID": 50, "Hospital_name": "Coptic Church Hoispital","Bed_Count":1300,"address": "Ngong Rd Off Kindaruma"},
  { "Hospital_ID": 60, "Hospital_name": "Nairobi Hospice","Bed_Count":1200,"Inside KNH": "Nairobi One way 798"},
  { "Hospital_ID": 70, "Hospital_name": "St. Mary's Hosp","Bed_Count":60,"address": "Otiende Yellow Garden 2"},
  { "Hospital_ID": 80, "Hospital_name": "Alfarooq Hosp","Bed_Count":150,"address": "Behind KCB Park Lane 380"},
  { "Hospital_ID": 90, "Hospital_name": "Lamu Sub-County","Bed_Count":2000,"address": "Lamu Central st 854"},
  { "Hospital_ID": 91, "Hospital_name": "Kilifi Sub-County","Bed_Count":1600,"address": "Kilifi Main Road 789"},
  { "Hospital_ID": 92, "Hospital_name": "ACK Maseno Hospice","Bed_Count":100,"address":"Kisumu Sideway 1633"}
]

x = mycol.insert_many(my_Hospitals_list)




# In[95]:


#connect the heatlthy DB to MongoDB Atlas
myclients = pymongo.MongoClient('mongodb+srv://ruth:joram%401934@cluster0.efu2u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = myclients["M_healths"]
mycol2 = mydb["Doctors"]
my_Doctors_list = [
  { "Doctor_ID": 101, "Doctor_name": "Lucy","Hospital_ID": 92,"Date_joined":"2016-02-02","Salary":100000,"Experience":5},
  { "Doctor_ID": 201, "Doctor_name": "Ruth","Hospital_ID": 91,"Date_joined":"2016-02-02","Salary":160000,"Experience":3},
  { "Doctor_ID": 301, "Doctor_name": "Jane","Hospital_ID": 90,"Date_joined":"2016-02-02","Salary":50000,"Experience":4},
  { "Doctor_ID": 401, "Doctor_name": "Habil","Hospital_ID": 90,"Date_joined":"2016-02-02","Salary":30000,"Experience":3},
  { "Doctor_ID": 401, "Doctor_name": "Thomas","Hospital_ID": 10,"Date_joined":"2016-02-02","Salary":25000,"Experience":13},
  { "Doctor_ID": 501, "Doctor_name": "Trump","Hospital_ID": 20,"Date_joined":"2016-02-02","Salary":13000,"Experience":23},
  { "Doctor_ID": 601, "Doctor_name": "Waki","Hospital_ID": 30,"Date_joined":"2016-02-02","Salary":12000,"Experience":15},
  { "Doctor_ID": 701, "Doctor_name": "Joseph","Hospital_ID": 40,"Date_joined":"2016-02-02","Salary":60000,"Experience":1},
  { "Doctor_ID": 801, "Doctor_name": "Martin","Hospital_ID": 50,"Date_joined":"2016-02-02","Salary":15000,"Experience":12},
  { "Doctor_ID": 901, "Doctor_name": "Kandis","Hospital_ID": 60,"Date_joined":"2016-02-02","Salary":20000,"Experience":10},
  { "Doctor_ID": 911, "Doctor_name": "Jerry","Hospital_ID": 70,"Date_joined":"2016-02-02","Salary":16000,"Experience":7},
  { "Doctor_ID": 921, "Doctor_name": "Liz","Hospital_ID": 80,"Date_joined":"2016-02-02","Salary":10000,"Experience":10},
  { "Doctor_ID": 702, "Doctor_name": "Maria","Hospital_ID": 40,"Date_joined":"2016-02-02","Salary":67000,"Experience":10},
  { "Doctor_ID": 802, "Doctor_name": "Marion","Hospital_ID": 50,"Date_joined":"2016-02-02","Salary":14000,"Experience":9},
  { "Doctor_ID": 902, "Doctor_name": "Caleb","Hospital_ID": 60,"Date_joined":"2016-02-02","Salary":24000,"Experience":11},
  { "Doctor_ID": 912, "Doctor_name": "Tom","Hospital_ID": 70,"Date_joined":"2016-02-02","Salary":17000,"Experience":7},
  { "Doctor_ID": 913, "Doctor_name": "Joel","Hospital_ID": 80,"Date_joined":"2016-02-02","Salary":18000,"Experience":7}  
]

y = mycol2.insert_many(my_Doctors_list)


# In[96]:


mydb=myclients.get_database('M_healths')
records=mydb.Hospitals
records.count_documents({})


# In[97]:


mydb=myclients.get_database('M_healths')
records=mydb.Doctors
records.count_documents({})


# In[98]:


aggre_results=mycol2.aggregate([
    { "$group": 
     {"_id":"Hospital_ID",
     "Total Salary":{"$sum":"$Salary"}
      }}
])
for i in aggre_results:
    print(i)


# In[99]:


###total amount of salaries


# In[100]:


### average amount of salaries
aggre_results=mycol2.aggregate([
    { "$group": 
     {"_id":"Hospital_ID",
     "Average Salary":{"$avg":"$Salary"}
      }}
])
for i in aggre_results:
    print(i)


# In[101]:


mydb=myclients.get_database('M_healths')
#records=mydb.Hospitals

mycol2=mydb['Doctors']

join_in = mycol.aggregate([
{
    "$lookup":{
         "from":"Doctors",
         "localField": "Hospital_ID",
         "foreignField": "Hospital_ID",
         "as": "Hospital_docs"
       }
  }
])
#print results line by line
for floodgates in join_in: 
    print(list(join_in))
    


# In[102]:


cur=mycol2.find_one(
    {"hospital_id":{"$gt":90}}
)


# In[103]:


cur=mycol2.find_one()
print(cur)


# In[110]:


import pymongo
conn = pymongo.MongoClient()
mydb = conn.M_healths #M_Healths is my database
#mycol2 is the hospial collection
cur = mycol.find()  
cur #loop thru the cursor object
for doc in cur:
  print(doc)  # or do something with the document


# In[105]:


#find method returns a cursor - <pymongo.cursor.Cursor object at 0x000002369FD90C10>

myCursor = mydb.mycols2.find()

print(myCursor)


# In[ ]:




