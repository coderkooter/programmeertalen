class Item:
    def __init__(self, name, points, weight, volume):
        self._name = name
        self._points = points
        self._weight = weight
        self._volume = volume

    def get_points(self):
        return self._points

    def get_weight(self):
        return self._weight

    def get_name(self):
        return self._name

    def get_volume(self):
        return self._volume
