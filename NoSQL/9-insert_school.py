#!/usr/bin/env python3
""" Inserting value to the database """


def insert_school(mongo_collection, **kwargs):
    """ Inserting and retrieving the id """

    new_id = mongo_collection.insert_one({**kwargs})
    return new_id.inserted_id
