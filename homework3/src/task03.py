# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(func(item) for func in self.functions)]


# found_bugs: lambda, isinstance(changed arguments):

# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
# print(positive_even.apply(range(100)))  # should return only even numbers from 0 to 99


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """

    def keyword_filter_func(closure_key, closure_value):
        # function with bugs:
        # return value[key] == value -> should be added checking existence of key in input_data
        # should be added closure parameters (key and value)
        return (
            lambda input_data: closure_key in input_data
            and input_data[closure_key] == closure_value
        )

    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(keyword_filter_func(key, value))

    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    {"0"},
    {"name": "polly"},
]

# print(make_filter(name='polly', type='bird').apply(sample_data)) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
