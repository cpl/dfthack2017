#!/usr/bin/python -B
"""Primitive objects for use in the program."""


class Station(object):
    """A bus stop."""

    def __init__(self, uid, name, lat, lon, operator, group):
        """Construct a bus stop."""
        self._uid = uid
        self._name = name
        self._lat = lat
        self._lon = lon
        self._operator = operator
        self._group = group

    def __str__(self):
        """String representation of a bus stop."""
        _string = 'Station(id: {:12}, name: {:50}, lat: {:12}, lat: {:12}, operator: {:6}, group: {:20})'

        return _string.format(self._uid, self._name, self._lat, self._lon,
                              self._operator, self._group)

    def __repr__(self):
        """Just calls toDict str."""
        return str(self.toDict())

    def toDict(self):
        """A dictionary representation."""
        return {'id': self._uid, 'name': self._name, 'lat': self._lat,
                'lon': self._lon, 'operator': self._operator,
                'group': self._group}


class Route(object):
    """The route of a bus on a day."""

    def __init__(self, uid, operator, group):
        """Construct a route primitive object."""
        self._uid = uid
        self._operator = operator
        self._group = group

    def __str__(self):
        """A string representation."""
        pass

    def __repr__(self):
        """Just call toDict str."""
        pass

    def toDict(self):
        """A dictionary representation."""
        pass
