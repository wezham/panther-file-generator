from tempfile import TemporaryDirectory

from panther.run import FileType
from panther.run import create_files_for_item_type


@pytest.mark.parameterize(
    "files_to_create",
    [
        [FileType.helper_py, FileType.helper_yml, FileType.query],
        [FileType.rule_yml],
        [
            FileType.helper_py,
            FileType.helper_yml,
            FileType.query,
            FileType.rule_yml,
            FileType.rule_py,
            FileType.scheduled_rule,
        ],
    ],
)
def test_create_files_for_item_type(files_to_create):
    with TemporaryDirectory() as tmpdir:
        create_files_for_item_type(
            file_types=files_to_create, target_dir=tmpdir, target_filename="testing_it"
        )


