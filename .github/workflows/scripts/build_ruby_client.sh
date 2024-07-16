#!/bin/bash

# This script expects all <app_label>-api.json files to exist in the plugins root directory.
# It produces a <app_label>-ruby-client.tar file in the plugins root directory.

# WARNING: DO NOT EDIT!
#
# This file was generated by plugin_template, and is managed by it. Please use
# './plugin-template --github pulp_npm' to update this file.
#
# For more info visit https://github.com/pulp/plugin_template

set -mveuo pipefail

# make sure this script runs at the repo root
cd "$(dirname "$(realpath -e "$0")")"/../../..

pushd ../pulp-openapi-generator
rm -rf "pulp_npm-client"

# We need to copy that over to be visible in the container.
#cp "../pulp_npm/npm-api.json" .
#./gen-client.sh "npm-api.json" "npm" ruby "pulp_npm"

# -------------
# The generator still needs to have it called api.json at this time...
cp "../pulp_npm/api.json" .
./gen-client.sh "api.json" "npm" ruby "pulp_npm"
# -------------

pushd pulp_npm-client
gem build pulp_npm_client
tar cvf "../../pulp_npm/npm-ruby-client.tar" "./pulp_npm_client-"*".gem"
popd
popd