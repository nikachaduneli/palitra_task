from pymongo import MongoClient
from django.conf import settings
from django.forms.models import model_to_dict

def get_mongo_client():
    """Get a MongoDB client using settings."""
    client = MongoClient(
        host=settings.MONGO_DB['HOST'],
        port=settings.MONGO_DB['PORT']
    )
    return client

def get_mongo_db():
    """Get the MongoDB database instance."""
    client = get_mongo_client()
    return client[settings.MONGO_DB['NAME']]



def sync_to_mongo(instance, collection_name, serializer_class):
    db = get_mongo_db()
    collection = db[collection_name]
    data = serializer_class(instance).data
    collection.update_one({"id": instance.id}, {"$set": data}, upsert=True)

def delete_from_mongo(instance, collection_name):
    db = get_mongo_db()
    collection = db[collection_name]
    collection.delete_one({"id": instance.id})
