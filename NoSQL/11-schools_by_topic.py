#!/usr/bin/env python3
""" Finding with specific string """


def schools_by_topic(mongo_collection, topic):
    """ Listing the founded things """

    listings = mongo_collection.find({"topics": topic})
    return list(listings)
