# WARNING: DO NOT EDIT!
#
# This file was generated by plugin_template, and is managed by it. Please use
# './plugin-template --github pulp_npm' to update this file.
#
# For more info visit https://github.com/pulp/plugin_template

import os
from github import Github

g = Github(os.environ.get("GITHUB_TOKEN"))
repo = g.get_repo("pulp/pulp_npm")

GH_ISSUES = os.environ.get("GH_ISSUES")

for issue in GH_ISSUES.split(","):
    issue = repo.get_issue(int(issue))
    if issue.state != "closed":
        print(f"Closing issue: {issue.number}")
        issue.edit(state="closed")
