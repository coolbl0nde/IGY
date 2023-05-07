import re
import inspect
from constants import CODE_ATTRIBUTES


class Serializer:

    def serialize(self, obj):

        res = {}

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

        elif inspect.isfunction(obj):
            res["type"] = "function"
            res["value"] = self.serialize_type_function(obj)

        elif not obj:
            res["type"] = "NoneType"
            res["value"] = "Null"

        else:
            res["type"] = "object"
            res["value"] = self.serialize_type_object(obj)

        return res

    def get_type_of_obj(self, obj):
        return re.search(r"\'(\w)+\'", str(type(obj)))[1]

    def serialize_type_object(self, obj):

        res = {}
        res["__class__"] = self.serialize(obj.__class__)

        fields = {}

        for (key, value) in inspect.getmembers(obj):
            if not inspect.isfunction(value) and not inspect.ismethod(value) and not key.startswith("__"):
                fields[key] = self.serialize(value)

        res["__members__"] = fields

        return res

    def serialize_type_function(self, obj, class_object = None):

        res = {}
        arguments = {}

        res["__name__"] = obj.__name__

        if obj.__closure__:
            res["__closure__"] = self.serialize(obj.__closure__)

        else:
            res["__closure__"] = self.serialize(tuple())

        for (key, value) in inspect.getmembers(obj.__code__):
            if key in CODE_ATTRIBUTES:
                arguments[key] = self.serialize(value)

        res["__code__"] = arguments

        return res