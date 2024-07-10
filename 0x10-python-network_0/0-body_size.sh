#!/bin/bash
#get the length of the response
curl -sI "$1" -o response.txt && grep "Content-Length" response.txt | cut -d ':' -f2 | cut -d ' ' -f2 && rm -f response.txt
