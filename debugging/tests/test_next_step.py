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