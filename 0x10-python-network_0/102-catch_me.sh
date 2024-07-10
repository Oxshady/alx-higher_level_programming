#!/bin/bash
# can we change the bhv of server
curl -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
