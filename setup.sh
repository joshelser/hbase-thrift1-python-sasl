#!/usr/bin/env bash

# Copyright 2017 Josh Elser
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Directory to store the virtualenv in
VENV_DIR_NAME="venv"

# Switch to the directory containing this script
cd "$(dirname "$0")"

# setup suggestions taken from http://www.pindi.us/blog/automating-pip-and-virtualenv-shell-scripts

# Set up a virualenv
if [ ! -d "./${VENV_DIR_NAME}" ]; then
  virtualenv  "${VENV_DIR_NAME}"
  echo "Created virtual environment in ${VENV_DIR_NAME}"
else
  echo "Virtual environment already created"
fi

if [ ! -f "./${VENV_DIR_NAME}/updated" -o "./${VENV_DIR_NAME}/requirements.pip" -nt "./${VENV_DIR_NAME}/updated" ]; then
  # Install the dependent packages
  pip install -r requirements.pip
  touch "./${VENV_DIR_NAME}/updated"
  echo "Requirements installed."
else
  echo "Requirements already up-to-date"
fi

# Use the virtualenv
source "./${VENV_DIR_NAME}/bin/activate"
export PYTHONPATH="${PYTHONPATH}:."
