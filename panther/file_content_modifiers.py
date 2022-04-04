import yaml


def filename_to_query_name(filename: str) -> str:
    """Converts filename into query name converting snake case convention to query convention"""
    return f"Query.{'.'.join((w.capitalize() for w in filename.split('_')))}"


def filename_to_rule_name(filename: str) -> str:
    """Converts filename into query name converting snake case convention to query convention"""
    return f"Rule.{'.'.join((w.capitalize() for w in filename.split('_')))}"


def filename_to_python_file(filename: str) -> str:
    return f"{filename}.py"


def yaml_handler(func):
    """Decorator which handles loading and dumping yaml for callers who read file contents as a
    string."""

    def handler(file_contents: str, target_filename: str):
        """Handles loading and dumping yaml files for the caller."""
        file_as_yaml = yaml.safe_load(file_contents)
        result = func(file_as_yaml, target_filename)
        return yaml.dump(result)

    return handler

@yaml_handler
def global_helper_yaml(file_yaml: dict, target_filename: str) -> dict:
    """Modifies the yaml to link your yaml file to your python file."""
    file_yaml["Filename"] = filename_to_python_file(target_filename)
    file_yaml["GlobalID"] = target_filename
    return file_yaml


@yaml_handler
def query_yaml(file_yaml: dict, target_filename: str) -> dict:
    """Modifies the query yaml file"""

    file_yaml["QueryName"] = filename_to_query_name(target_filename)

    return file_yaml


@yaml_handler
def rule_yaml(file_yaml: dict, target_filename: str) -> dict:
    """Modifies rule yaml."""

    file_yaml["Filename"] = filename_to_python_file(target_filename)
    file_yaml["RuleID"] = filename_to_rule_name(target_filename)
    return file_yaml


@yaml_handler
def scheduled_rule_yaml(file_yaml: dict, target_filename: str) -> dict:
    """Modifies the scheduled rule yaml file."""

    file_yaml["Filename"] = filename_to_python_file(target_filename)
    file_yaml["RuleID"] = filename_to_rule_name(target_filename)
    file_yaml["ScheduledQueries"] = [filename_to_query_name(target_filename)]

    return file_yaml
