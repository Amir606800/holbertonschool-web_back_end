#!/usr/bin/python3
""" uSING mONGOdB WITH PYTHON """
def list_all(mongo_collection):
    if mongo_collection.find():
        return mongo_collection.find()
    return []
