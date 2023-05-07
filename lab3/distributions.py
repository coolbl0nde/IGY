import re


class Serializer:

    def serialize(self, obj):

        res = {}
        # type(obj) == "<class 'bool'>"

        if isinstance(obj, (str, float, int, bool)):
            res["type"] = self.get_type_of_obj(obj)
            res["value"] = obj

        elif isinstance(obj, (tuple, list, set, frozenset, bytearray)):
            res["type"] = self.get_type_of_obj(obj)
            ser_object = []

            for value in obj:
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

        elif isinstance(obj, dict):
            res["type"] = "dict"
            ser_object = []

            for value in obj.items():
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

    def get_type_of_obj(self, obj):
        return re.search(r"\'(\w)+\'", str(type(obj)))[1]
