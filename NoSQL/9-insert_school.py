#!/usr/bin/env python3
""" Inserting value to the database """


def insert_school(mongo_collection, **kwargs):
    """ Inserting and retrieving the id """

    new_id = mongo_collection.insertOne(**kwargs)
    return new_id
