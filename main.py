#!/usr/bin/python -B
"""DOCSTRING."""

import db
import utility
import pprint

if __name__ == '__main__':

    db = db.Database()

    stops = db.select_all_from('STOPS')
    stations = []
    for stop in stops:
        stations.append(utility.Station(stop[0], stop[1], stop[2],
                                        stop[3], stop[4], stop[5]))

    pprint.pprint(stations)
