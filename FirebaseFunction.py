import pyrebase
import os 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#variable and setup===========
config={
"apiKey": "AIzaSyDwhw4W6-7abHmVZIIS_GCMa761jg6p5rM",
"authDomain": "maskdetection-c678a.firebaseapp.com",
"databaseURL": "https://maskdetection-c678a-default-rtdb.firebaseio.com",
"projectId": "maskdetection-c678a",
"storageBucket": "maskdetection-c678a.appspot.com",
"messagingSenderId":"649266485411",
    "appId":"1:649266485411:web:3191482d298e6839170716",
    "measurementId":"G-5GJNH8T888"
}

    
#======================================


#initializing firebase variables

firebase_storage=pyrebase.initialize_app(config)
cred=credentials.Certificate("D:\interface-bill\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
storage= firebase_storage.storage()
coll=firestore.client()

#initializing the dictionary
convictDict=dict();
# reterving the data
for doc in coll.collection('imageDetails').stream():
    #making the dictionary and sore the data in that dictionary
    convictDict[doc.id]=doc.to_dict()


#method to get string after cheking that image is verified by human
def getImgUrlAfterCheckingTrue(convictDict):
    l= list()
    #looping through nested dictionary woth help of keys
    print( convictDict.keys())
    for a in convictDict:
        print(a)
        #checking the dictionary is true
        if convictDict[a]['check'] == "True":
            l.append(convictDict[a]['imgurl'])
            # returning the imgurl
    return l


