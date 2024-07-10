#!/bin/bash
#get the length of the response
if [ $# -lt 1 ]; then
	exit 1
fi
curl -sI $1 -o response.txt
cat response.txt | grep "Content-Length" | cut -d ':' -f2 | cut -d " " -f2
rm -f response.txt
