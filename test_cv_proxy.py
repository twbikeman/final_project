from cv_proxy import cv_proxy
import firebase_init
from firebase_init import storage_proxy

storage_proxy = storage_proxy()
cv_proxy = cv_proxy()

model = cv_proxy.getpicture()
storage_proxy.upload(model)

