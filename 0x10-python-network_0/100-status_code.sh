#!/bin/bash
# status code of resp
curl -sI "$1" -o response.txt && grep "HTTP" response.txt | cut -d ' ' -f2 | cut -d ' ' -f2 && rm -f response.txt
