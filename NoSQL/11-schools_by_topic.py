#!/usr/bin/env python3
""" Finding with specific string """


def schools_by_topic(mongo_collection, topic):
    listings = mongo_collection.find({"topics": topic})
