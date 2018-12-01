class Dictionary(dict):
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            self[key] = value if not isinstance(value, dict) else Dictionary(value)

    def get(self, key, default_value = None):
        if isinstance(key, (list, tuple)):
            for sub_key in key:
                if sub_key in self:
                    return self[sub_key]
            return default_value
        else:
            return self[key] if key in self else default_value

def get(dictionary, key, default_value):
    if isinstance(key, (list, tuple)):
        for sub_key in key:
            if sub_key in dictionary:
                return dictionary[sub_key]
        return default_value
    else:
        return dictionary[key] if key in dictionary else default_value


def testcase():
    dictionary = {
        test1': {
            'test2': 123,
            'test3': 234
        }
    }
    dictionary = Dictionary(dictionary)
    print(dictionary)
    print(dictionary.get(['reee', 'test1']).get(['test1', 'test2'], 233))

if __name__ == '__main__':
    testcase()
