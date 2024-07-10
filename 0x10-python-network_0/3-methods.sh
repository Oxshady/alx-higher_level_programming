#!/bin/bash
#all av methods
curl -sI -X OPTIONS "$1" -o res.txt && grep -i "Allow:" res.txt | cut -d ":" -f2-
