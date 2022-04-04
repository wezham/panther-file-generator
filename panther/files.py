import pathlib
import pkgutil
from enum import Enum
from logging import getLogger
from typing import Callable, Dict, List, NamedTuple, Optional

from panther.file_content_modifiers import (
    global_helper_yaml,
    query_yaml,
    rule_yaml,
    scheduled_rule_yaml,
)

logger = getLogger(__name__)

class FileType(Enum):
    helper_py = "sample_helper.py"
    helper_yml = "sample_helper.yml"
    query = "sample_query.yml"
    rule_yml = "sample_rule.yml"
    rule_py = "sample_rule_py.py"
    scheduled_rule = "sample_scheduled_rule.yml"


class FileInformation(NamedTuple):
    extension: str
    filename_suffix: str = ""
    file_contents_modifier: Optional[Callable[[dict, str], dict]] = None


FILE_TYPE_TO_FILE_INFORMATION: Dict[FileType, FileInformation] = {
    FileType.helper_py: FileInformation(extension="py"),
    FileType.rule_py: FileInformation(extension="py"),
    FileType.helper_yml: FileInformation(
        extension="yml", file_contents_modifier=global_helper_yaml
    ),
    FileType.query: FileInformation(
        extension="yml",
        filename_suffix="_query",
        file_contents_modifier=query_yaml,
    ),
    FileType.rule_yml: FileInformation(
        extension="yml", file_contents_modifier=rule_yaml
    ),
    FileType.scheduled_rule: FileInformation(
        extension="yml", file_contents_modifier=scheduled_rule_yaml
    ),
}


def create_files_for_item_type(
    file_types: List[FileType], target_dir: pathlib.Path, target_filename: str
) -> None:
    """Creates skeleton files in the specified directory inferring names from the target filename"""
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
        file_contents = (
            file_information.file_contents_modifier(
                sample_file_contents, target_filename
            )
            if file_information.file_contents_modifier
            else sample_file_contents
        )

        # Write file to destination
        logger.debug(f"Writing {target_dir}/{dest_file}")
        with open(dest_file, "w") as f:
            f.write(file_contents)
