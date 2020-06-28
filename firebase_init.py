
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('aibigdata-ntut-107598064-firebase.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'aibigdata-ntut-107598064.appspot.com'})


class storage_proxy():
    def __init__(self):
        pass
    
    def upload(self, model):
        bucket = storage.bucket()
        blob = bucket.blob('bus/' + str(model['timestamp']) + '.jpg')
        blob.upload_from_string(model['image'])
        blob.make_public()
        print('--------------------')
        print('storage url: ' + blob.public_url)
        return blob.public_url
    
        
