#!/bin/bash
#get body if res = 200
curl -sI "$1" -o response.txt && code=$(grep "HTTP" response.txt | cut -d ' ' -f2) && if [ "$code" -eq 200 ]; then curl -s "$1";fi && rm -f response.txt
