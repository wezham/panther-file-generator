import pathlib
from tempfile import TemporaryDirectory

import pytest

from panther.run import FileType, create_files_for_item_type


def test_create_files_for_item_type_successfully_creates_files():
    files_to_create = [FileType.helper_py, FileType.helper_yml, FileType.query]

    with TemporaryDirectory() as tmpdir:
        path_to_files = pathlib.Path(tmpdir)
        create_files_for_item_type(
            file_types=files_to_create,
            target_dir=path_to_files,
            target_filename="testing_it",
        )

        assert path_to_files.joinpath("testing_it.py").exists()
        assert path_to_files.joinpath("testing_it.yml").exists()
        assert path_to_files.joinpath("testing_it_query.yml").exists()


def test_create_files_for_item_type_creates_no_files_if_errors():
    files_to_create = [FileType.helper_py, "bad argument"]

    with TemporaryDirectory() as tmpdir:
        path_to_files = pathlib.Path(tmpdir)
        with pytest.raises(Exception):
            create_files_for_item_type(
                file_types=files_to_create,
                target_dir=path_to_files,
                target_filename="testing_it",
            )

        assert not path_to_files.joinpath("testing_it.py").exists()
