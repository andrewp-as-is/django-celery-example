#!/usr/bin/env bash
{ set +x; } 2>/dev/null

( set -x; ansible-playbook "${BASH_SOURCE[0]%/*}"/ansible-playbook.yml )
