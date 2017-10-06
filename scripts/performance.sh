#!/usr/bin/env bash

echo "perform ${WEBHOOK_URL}"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

curl -w "@${DIR}/curl-format.txt" -o /dev/null -X POST -v -d "{\"entry\":[],\"object\":\"page\"}" -H "Content-Type: application/json" -s "${WEBHOOK_URL}"
