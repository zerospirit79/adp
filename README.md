# altlinux package diff
Comparing packages in different branches
Requires:
* python3-base
* python3-module-requests

```markdown
# AltLinux Package Diff CLI

This CLI tool compares package lists between different AltLinux branches.

## Usage

```bash
$ python3 -m adp <branch1> <branch2>
```

**Example:**

```bash
$ python3 -m adp sisyphus p10
```

This will compare the package lists of `sisyphus` and `p10` branches and print the diff in JSON format.
