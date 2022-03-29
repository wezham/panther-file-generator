import argparse
import pathlib
import pkgutil
import sys
from enum import Enum
from logging import DEBUG, Formatter, StreamHandler, getLogger
from typing import Dict, List, NamedTuple

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class FileType(Enum):
    helper_py = "sample_helper.py"
    helper_yml = "sample_helper.yml"
    query = "sample_query.yml"
    rule_yml = "sample_rule.yml"
    rule_py = "sample_rule_py.py"
    scheduled_rule = "sample_schedule_rule.yml"


class FileInformation(NamedTuple):
    extension: str
    filename_suffix: str = ""


FILE_TYPE_TO_FILE_INFORMATION: Dict[FileType, FileInformation] = {
    FileType.helper_py: FileInformation(extension="py"),
    FileType.helper_yml: FileInformation(extension="yml"),
    FileType.query: FileInformation(extension="yml", filename_suffix="_query"),
    FileType.rule_yml: FileInformation(extension="yml"),
    FileType.rule_py: FileInformation(extension="py"),
    FileType.scheduled_rule: FileInformation(extension="yml"),
}


def create_files_for_item_type(
    file_types: List[FileType], target_dir: pathlib.Path, target_filename: str
) -> None:
    """Creates"""
    for file_type in file_types:
        # Get the sample file to generate the new file
        sample_file_contents = pkgutil.get_data(
            __name__, f"data/{file_type.value}"
        ).decode()

        # Get information about the file to create
        file_information = FILE_TYPE_TO_FILE_INFORMATION[file_type]
        file_to_create = (
            f"{target_filename}{file_information.filename_suffix}."
            f"{file_information.extension}"
        )
        dest_file = target_dir.joinpath(file_to_create)

        # Write file to destination
        logger.debug(f"Creating python file at {dest_file}")
        with open(dest_file, "w") as f:
            f.write(sample_file_contents)


def main():
    parser = argparse.ArgumentParser(
        description="Generates the boilerplate files for creating panther detections in code"
    )
    parser.add_argument(
        "--target-dir",
        metavar="target directory",
        type=str,
        nargs="?",
        help="Specifies the directory you would like to create the files in",
        required=True,
    )
    parser.add_argument(
        "--item",
        metavar="item-type",
        type=str,
        nargs="?",
        help="What you would like to create [rule,scheduled-rule,helper]",
        choices=["rule", "scheduled-rule", "helper"],
        required=True,
    )

    parser.add_argument(
        "--file-name",
        metavar="file-name",
        type=str,
        nargs="?",
        help="name of the item you are creating, for example onepassword_account_access",
        required=True,
    )

    args = parser.parse_args()
    target_dir_path = pathlib.Path(args.target_dir)

    if args.item == "rule":
        files_to_create = [FileType.rule_py, FileType.rule_yml]
    elif args.item == "scheduled-rule":
        files_to_create = ([FileType.rule_py, FileType.scheduled_rule, FileType.query],)
    elif args.item == "helper":
        files_to_create = [FileType.helper_py, FileType.helper_yml]
    else:
        raise ValueError(f"{args.item} not supported")

    create_files_for_item_type(
        file_types=files_to_create,
        target_dir=target_dir_path,
        target_filename=args.file_name,
    )
