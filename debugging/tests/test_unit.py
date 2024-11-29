from gendiff.tree import build_diff


def test_build_diff_added():
    data1 = {}
    data2 = {"key": "value1"}
    expected = [{"key": "key", "status": "added", "value": "value1"}]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_removed():
    data1 = {"key": "value1"}
    data2 = {}
    expected = [{"key": "key", "status": "removed", "value": "value1"}]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_same():
    data1 = {"key": "value1"}
    data2 = {"key": "value1"}
    expected = [{"key": "key", "status": "same", "value": "value1"}]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_updated():
    data1 = {"key": "old_value"}
    data2 = {"key": "new_value"}
    expected = [
        {"key": "key", "status": "updated", "value": "old_value", "value2": "new_value"}
    ]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_child_updated_1_wrapped_first():
    data1 = {"key": {"wrapped_key": "wrapped_value"}}
    data2 = {"key": "new_value"}
    expected = [
        {
            "key": "key",
            "status": "updated",
            "value": {"wrapped_key": "wrapped_value"},
            "value2": "new_value",
        }
    ]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_child_updated_2_wrapped_second():
    data1 = {"key": "new_value"}
    data2 = {"key": {"wrapped_key": "wrapped_value"}}
    expected = [
        {
            "key": "key",
            "status": "updated",
            "value": "new_value",
            "value2": {"wrapped_key": "wrapped_value"},
        }
    ]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_child_updated_3_wrapped_both_different_keys():
    data1 = {"key": {"wrapped_old": "old_value"}}
    data2 = {"key": {"wrapped_new": "new_value"}}
    expected = [
        {
            "child": [
                {"key": "wrapped_new", "status": "added", "value": "new_value"},
                {"key": "wrapped_old", "status": "removed", "value": "old_value"},
            ],
            "key": "key",
            "status": "child",
        }
    ]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_child_updated_4_wrapped_both_same_keys():
    data1 = {"key": {"wrapped_key": "old_value"}}
    data2 = {"key": {"wrapped_key": "new_value"}}
    expected = [
        {
            "child": [
                {
                    "key": "wrapped_key",
                    "status": "updated",
                    "value": "old_value",
                    "value2": "new_value",
                }
            ],
            "key": "key",
            "status": "child",
        }
    ]

    result = build_diff(data1, data2)

    assert result == expected


def test_build_diff_child_same():
    data1 = {"key": {"wrapped": "value"}}
    data2 = {"key": {"wrapped": "value"}}
    expected = [
        {
            "child": [{"key": "wrapped", "status": "same", "value": "value"}],
            "key": "key",
            "status": "child",
        }
    ]
    result = build_diff(data1, data2)

    assert result == expected
