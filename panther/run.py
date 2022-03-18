import argparse
import pathlib
import pkgutil
import sys
from logging import DEBUG, Formatter, StreamHandler, getLogger

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def _create_sample_file_at_path(
    target_dir: pathlib.Path, sample_file_name: str, dest_filename: str
):
    """Copies the contents of the sample file to the destiantion file in the target directory."""
    sample_file_contents = pkgutil.get_data(
        __name__, f"data/{sample_file_name}"
    ).decode()
    dest_file = target_dir.joinpath(dest_filename)
    logger.debug(f"Creating python file at {dest_file}")
    with open(dest_file, "w") as f:
        f.write(sample_file_contents)

    logger.debug("Successfully wrote new file")


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
        help="The type of the of the detection you would like to create [rule,scheduled-rule]",
        choices=["rule", "scheduled-rule"],
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
    print(args)
    target_dir_path = pathlib.Path(args.target_dir)
    if args.item == "rule":
        # A rule requires a python file, a rule file
        _create_sample_file_at_path(
            target_dir=target_dir_path,
            sample_file_name="sample_py.py",
            dest_filename=f"{args.file_name}.py",
        )

        _create_sample_file_at_path(
            target_dir=target_dir_path,
            sample_file_name="sample_rule.yml",
            dest_filename=f"{args.file_name}.yml",
        )
    elif args.item == "scheduled-rule":
        # A scheduled rule requires a python file, a scheduled_query and a scheduled_rule
        _create_sample_file_at_path(
            target_dir=target_dir_path,
            dest_filename=f"{args.file_name}.py",
            sample_file_name="sample_py.py",
        )

        _create_sample_file_at_path(
            target_dir=target_dir_path,
            dest_filename=f"{args.file_name}.yml",
            sample_file_name="sample_scheduled_rule.yml",
        )

        _create_sample_file_at_path(
            target_dir=target_dir_path,
            dest_filename=f"{args.file_name}_query.yml",
            sample_file_name="sample_query.yml",
        )
    else:
        raise ValueError(f"{args.item} not supported")
