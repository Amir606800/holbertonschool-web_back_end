#!/usr/bin/env python3
""" Updateing the Document """


def update_topics(mongo_collection, name, topics):
    """ Updating the documents with update_one """

    mongo_collection.update_one({"name": name}, {$set: {"topics": topics}})
