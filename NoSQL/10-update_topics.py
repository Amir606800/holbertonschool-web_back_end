#!/usr/bin/env python3
""" Updateing the Document """


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one({"name": name}, {$set: {"topics": topics}})
