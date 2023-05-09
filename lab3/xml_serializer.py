from distributions import Serializer, Deserializer


class XMLSerializer:

    def __init__(self):
        self.ser = Serializer()
        self.des = Deserializer()

    def convert(self, value):

        if isinstance(value, (int, float, bool)):
            return f"<{type(value).__name__}>{str(value)}</{type(value).__name__}>"

        elif isinstance(value, str):
            value = value.replace('"', "&quot;").replace("'", "&apos;").replace("<", "&lt").replace(">", "&gt").replace("&", "&amp")
            return f"<str>{value}</str>"

        elif isinstance(value, list):
            value = "".join([self.convert(val) for val in value])
            return f"<list>{value}</list>"

        elif isinstance(value, dict):
            value = "".join([f"{self.convert(key)}{self.convert(val)}" for (key, val) in value.items()])
            return f"<dict>{value}</dict>"

        elif not value:
            return "<NoneType>None</NoneType>"

    def dumps(self, obj):
        return self.convert(self.ser.serialize(obj))

    def dump(self, obj, f):
        f.write(self.dumps(obj))