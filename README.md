# About 

This tool does the job of:

1. Creating collections of files you will need when creating a rule, scheduled rule or helper file
2. Linking those files were necessary. For example, it links a scheduled rule and scheduled query

An example is provided below

```
$ panther-generate helper ./global_helpers --file-name accounts                                                                ░▒▓ ✔ │ panther Py │ at 14:27:18 ▓▒░
2022-04-04 14:27:20,566 - panther.files - DEBUG - Writing /Users/testuser/content/global_helpers/accounts.py
2022-04-04 14:27:20,566 - panther.files - DEBUG - Writing /Users/testuser/content/global_helpers/accounts.yml
```

And `accounts.yml` will contain:

```yaml
Filename: accounts.py
```

# Usage

```
usage: panther-generate TARGET_DIR [rule,scheduled-rule,helper] FILE_NAME

Generates the boilerplate files for creating panther detections in code

positional arguments:
  item-type             What you would like to create [rule,scheduled-rule,helper]
  target directory      Specifies the directory you would like to create the files in

optional arguments:
  -h, --help            show this help message and exit
  --file-name [file-name]
                        Name of the item you are creating. For example onepassword_account_access
```

# Installation

1. `git clone`
2. `cd` into package
3. `pip install .`

# Contributing 

TBC