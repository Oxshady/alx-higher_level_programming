#!/bin/bash
#get the length of the response
curl -sI "$1" -o response.txt && code=$(grep "HTTP" response.txt | cut -d ' ' -f2) && if [ "$code" -eq 200 ]; then curl -s "$1";fi && rm -f response.txt
