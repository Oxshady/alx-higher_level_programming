#!/bin/bash
# status code of resp
curl -w "%{http_code}" -sI "$1" -o /dev/null
