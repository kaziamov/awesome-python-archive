# Деббагинг на примере 2 проекта


```python
# test_e2e.py

from gendiff.scripts.gendiff import generate_diff


def test_diff_1():
    path1 = './fixtures/tree/tree_1.json'
    path2 = './fixtures/tree/tree_2.json'
    expected = open('./fixtures/expected/tree_expected.txt').read()
    assert generate_diff(path1, path2) == expected
```

```python
# test_unit.py

from gendiff.tree import build_diff


def test_build_diff_added():
    data1 = {}
    data2 = {'key': 'value1'}
    expected = [{'key': 'key', 'status': 'added', 'value': 'value1'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_removed():
    data1 = {'key': 'value1'}
    data2 = {}
    expected = [{'key': 'key', 'status': 'removed', 'value': 'value1'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_same():
    data1 = {'key': 'value1'}
    data2 = {'key': 'value1'}
    expected = [{'key': 'key', 'status': 'same', 'value': 'value1'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_updated():
    data1 = {'key': 'old_value'}
    data2 = {'key': 'new_value'}
    expected = [{'key': 'key', 'status': 'updated', 'value': 'old_value', 'value2': 'new_value'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_wrapped_1():
    data1 = {'key': {'wrapped_key': 'wrapped_value'}}
    data2 = {'key': 'new_value'}
    expected = [{'key': 'key', 'status': 'updated', 'value': {'wrapped_key': 'wrapped_value'}, 'value2': 'new_value'}]

    assert build_diff(data1, data2) == expected


def test_build_diff_wrapped_2():
    data1 = {'key': 'new_value'}
    data2 = {'key': {'wrapped_key': 'wrapped_value'}}
    expected = [{'key': 'key', 'status': 'updated', 'value': 'new_value', 'value2': {'wrapped_key': 'wrapped_value'}}]

    assert build_diff(data1, data2) == expected


def test_build_diff_child_updated_1():
    data1 = {'key': {'wrapped_old': 'old_value'}}
    data2 = {'key': {'wrapped_new': 'new_value'}}
    expected = [{'child': [{'key': 'wrapped_new', 'status': 'added', 'value': 'new_value'},
        {'key': 'wrapped_old', 'status': 'removed', 'value': 'old_value'}], 'key': 'key', 'status': 'child'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_child_updated_2():
    data1 = {'key': {'wrapped_key': 'old_value'}}
    data2 = {'key': {'wrapped_key': 'new_value'}}
    expected = [{'child': [{'key': 'wrapped_key', 'status': 'updated', 'value': 'old_value', 'value2': 'new_value'}],
        'key': 'key', 'status': 'child'}]
    assert build_diff(data1, data2) == expected


def test_build_diff_child_same():
    data1 = {'key': {'wrapped': 'value'}}
    data2 = {'key': {'wrapped': 'value'}}
    expected = [{'child': [{'key': 'wrapped', 'status': 'same', 'value': 'value'}], 'key': 'key', 'status': 'child'}]
    assert build_diff(data1, data2) == expected
```

```python
# test_formatting.py

from gendiff import generate_diff


def test_plain_bugfix():
    # E         - Property 'common.setting2' was removed
    # E         ?                                ^^^^^
    # E         + Property 'common.setting2' was added
    # E         ?                                ^^^
    file1 = "./fixtures/tree/tree_1.json"
    file2 = "./fixtures/tree/tree_2.json"

    expected = open("./fixtures/expected/tree_plain_expected.txt").read()

    assert generate_diff(file1, file2, 'plain') == expected




```


