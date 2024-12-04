def introspection_info(obj):
    introspection_dict = {}

    introspection_dict['class'] = type(obj).__name__

    attributes = {attr: getattr(obj, attr) for attr in dir(obj)
                  if not callable(getattr(obj, attr)) and not attr.startswith('_')}
    introspection_dict['attributes'] = attributes

    methods = [method for method in dir(obj)
               if callable(getattr(obj, method)) and not method.startswith('_')]
    introspection_dict['methods'] = methods

    introspection_dict['module'] = obj.__module__

    return introspection_dict


class SomeClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"


example_instance = SomeClass(42)
result = introspection_info(example_instance)

print(result)






