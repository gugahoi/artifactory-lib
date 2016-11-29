#!/usr/bin/env bash

set -eu

cat << EOF
steps:
  - label: 'Testing :python:'
    command: 'python -m unittest discover'
    agents:
      queue: 'voyager'
    env:
      BUILDKITE_DOCKER: true
EOF

# deploy only if it's a tag
if [[ -n "${BUILDKITE_TAG:-}" ]]; then
  cat << EOF
  - label: 'Deploying to PyPi'
    command: ./deploy.sh
    agents:
      queue: 'voyager'
EOF
fi
