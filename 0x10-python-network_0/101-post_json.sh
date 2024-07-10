#!/bin/bash
# submit json data
curl -d "@$2" -H "Content-Type: application/json" -s "$1"
