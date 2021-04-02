"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Generator, Union

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def generate_values(
    tree_values: Union[str, list, tuple, dict, set, int, bool]
) -> Generator[Union[str, int, bool], None, None]:
    for tree_value in tree_values:
        if isinstance(tree_value, (str, int, bool)):
            yield tree_value
        elif isinstance(tree_value, dict):
            yield from generate_values(tree_value.values())
        else:
            yield from generate_values(tree_value)


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    for value in generate_values(tree.values()):
        if value == element and type(value) == type(element):
            counter += 1
    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
