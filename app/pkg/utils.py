"""Cool idea, but I don't want waste more time,
for realise this correct, because I use 2 metaclass."""

# from abc import ABCMeta

#
# class StaticMeta(type):
#     """Metaclass which cast all methods to staticmethod."""
#     def __new__(cls, name, bases, attrs):
#         static_attrs = {}
#         for attr_name, attr_value in attrs.items():
#             if callable(attr_value):
#                 static_attrs[attr_name] = staticmethod(attr_value)
#             else:
#                 static_attrs[attr_name] = attr_value
#         return super().__new__(cls, name, bases, static_attrs)
