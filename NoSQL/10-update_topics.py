#!/usr/bin/env python3
""" Updateing the Document """


def update_topics(mongo_collection, name, topics):
    """ Updating the documents with update_one """

    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result
