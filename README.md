# Instructions

### Installation

Using pip:

`pip install pre-commit`



 Using homebrew:

`brew install pre-commit`


Using conda:

`conda install -c conda-forge pre-commit`

Check installation:
`pre-commit --version`

### Clone repository

Clone repository to your local machine:

`git clone git@github.com:uazafar/pre-commit-tutorial.git`


Run pre-commit install so that the pre-commit hooks actually run on a commit:

`pre-commit install`


### Run pre-commit

Nothing to commit at the moment, so to run in an ad-hoc way, run the following:

`pre-commit run --all-files`

Time to fix the issues! Once you are done, you can add the changed files and commit locally. When committing your work, the pre-commit checks will be performed and the commit will be successful if all checks pass. Hopefully, the pre-commit police will find no issues with your code.
