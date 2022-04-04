from panther.file_content_modifiers import filename_to_query_name, filename_to_rule_name, filename_to_python_file


def test_filename_to_query_name():
    assert filename_to_query_name('aws_iam_secret_access') == "Query.Aws.Iam.Secret.Access"

def test_filename_to_rule_name():
    assert filename_to_rule_name('aws_iam_secret_access') == "Rule.Aws.Iam.Secret.Access"

def test_filename_to_python_file():
    assert filename_to_python_file('aws_iam_secret_access') == "aws_iam_secret_access.py"