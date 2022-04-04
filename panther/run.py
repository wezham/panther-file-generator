import argparse
import pathlib

from panther.files import FileType, create_files_for_item_type


def main():
    parser = argparse.ArgumentParser(
        description="Generates the boilerplate files for creating panther detections in code",
        usage="panther-generate TARGET_DIR [rule,scheduled-rule,helper] FILE_NAME"
    )
    parser.add_argument(
        dest="target_dir",
        metavar="target directory",
        type=str,
        nargs="?",
        help="Specifies the directory you would like to create the files in",
        default=pathlib.Path().cwd()
    )
    parser.add_argument(
        dest="item",
        metavar="item-type",
        type=str,
        nargs="?",
        help="What you would like to create [rule,scheduled-rule,helper]",
        choices=["rule", "scheduled-rule", "helper"],
    )

    parser.add_argument(
        "--file-name",
        metavar="file-name",
        type=str,
        nargs="?",
        help="Name of the item you are creating. For example onepassword_account_access",
        required=True,
    )

    args = parser.parse_args()
    target_dir_path = pathlib.Path(args.target_dir)

    if args.item == "rule":
        files_to_create = [FileType.rule_py, FileType.rule_yml]
    elif args.item == "scheduled-rule":
        files_to_create = [FileType.rule_py, FileType.scheduled_rule, FileType.query]
    elif args.item == "helper":
        files_to_create = [FileType.helper_py, FileType.helper_yml]
    else:
        raise ValueError(f"{args.item} not supported")

    create_files_for_item_type(
        file_types=files_to_create,
        target_dir=target_dir_path,
        target_filename=args.file_name,
    )
