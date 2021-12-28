import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyAOLKn2mC8T4VKjnxWxDIXuOIuTGTH-7oM",
  'authDomain': "crawl-b9744.firebaseapp.com",
  'databaseURL': "https://crawl-b9744-default-rtdb.firebaseio.com/",
  'projectId': "crawl-b9744",
  'storageBucket': "crawl-b9744.appspot.com",
  'messagingSenderId': "646693660342",
  'appId': "1:646693660342:web:eb80eceeb52e5c09562817",
  'measurementId': "G-52R7D2C25H"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
# auth = firebase.auth()
# storage = firebase.storage()


def pushDataToShopee(data):
  db.child("shopee").push(data)


def pushDataToLazada(data):
  db.child("lazada").push(data)


def pushDataToSendo(data):
  db.child("sendo").push(data)


def getDataFromShopee():
  db.child("shopee").get()