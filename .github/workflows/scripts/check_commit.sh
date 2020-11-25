#!/bin/bash

# WARNING: DO NOT EDIT!
#
# This file was generated by plugin_template, and is managed by it. Please use
# './plugin-template --github pulp_npm' to update this file.
#
# For more info visit https://github.com/pulp/plugin_template

# make sure this script runs at the repo root
cd "$(dirname "$(realpath -e "$0")")"/../../..

set -euv

echo ::group::REQUESTS
pip3 install requests
echo ::endgroup::

for sha in $(curl $GITHUB_CONTEXT | jq '.[].sha' | sed 's/"//g')
do
  python3 .ci/scripts/validate_commit_message.py $sha
  VALUE=$?
  if [ "$VALUE" -gt 0 ]; then
    exit $VALUE
  fi
done
