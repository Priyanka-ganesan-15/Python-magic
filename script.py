class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __iter__(self):
        return iter(self.value)

    def __call__(self, *args, **kwargs):
        return f"MyClass instance called with arguments: {args}, {kwargs}"

# Example usage:
obj = MyClass([1, 2, 3])
print(str(obj))            # MyClass with value [1, 2, 3]
print(repr(obj))           # MyClass([1, 2, 3])
print(len(obj))            # 3
print(obj[1])              # 2
obj[1] = 42
print(obj[1])              # 42
del obj[1]
print(list(obj))           # [1, 42]
print(obj())               # MyClass instance called with arguments: (), {}
