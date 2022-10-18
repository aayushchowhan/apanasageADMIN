import firebase_admin
from firebase_admin import credentials , storage

cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'appnasage-app.appspot.com'})
def insertFile(colletion,id):
    from tkinter import filedialog as fd
    filename = fd.askopenfilename()
    bucket = storage.bucket()
    blob = bucket.blob(colletion+'/'+id+'/'+filename.split('/')[-1])
    blob.upload_from_filename(filename)
    blob.make_public()
    return blob.public_url 