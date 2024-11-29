from gendiff.scripts.gendiff import generate_diff

from tests.conftest import fixtures_path

with open(fixtures_path("expected/tree_expected.txt"), "r", encoding="utf-8") as file:
    tree_expected = file.read()

with open(
    fixtures_path("expected/tree_plain_expected.txt"), "r", encoding="utf-8"
) as file:
    tree_plain_expected = file.read()


def test_generate_diff_tree_files_1():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.json"),
        fixtures_path("tree/tree_2.json"),
        tree_expected,
    )
    assert generate_diff(file1, file2) == expected


def test_generate_diff_tree_files_2():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.yml"),
        fixtures_path("tree/tree_2.yaml"),
        tree_expected,
    )
    assert generate_diff(file1, file2) == expected


def test_generate_diff_tree_files_3():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.json"),
        fixtures_path("tree/tree_2.yaml"),
        tree_expected,
    )
    assert generate_diff(file1, file2) == expected


def test_generate_diff_tree_files_in_plain_1():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.json"),
        fixtures_path("tree/tree_2.json"),
        tree_plain_expected,
    )
    assert generate_diff(file1, file2, "plain") == expected


def test_generate_diff_tree_files_in_plain_2():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.yml"),
        fixtures_path("tree/tree_2.yaml"),
        tree_plain_expected,
    )
    assert generate_diff(file1, file2, "plain") == expected


def test_generate_diff_tree_files_in_plain_3():
    file1, file2, expected = (
        fixtures_path("tree/tree_1.yml"),
        fixtures_path("tree/tree_2.json"),
        tree_plain_expected,
    )
    assert generate_diff(file1, file2, "plain") == expected
