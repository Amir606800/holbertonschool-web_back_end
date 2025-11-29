#!/usr/bin/env python3
""" uSING mONGOdB WITH PYTHON """


def list_all(mongo_collection):
    """ checking the collection status """

    if mongo_collection.find():
        return mongo_collection.find()
    return []
