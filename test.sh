#!/bin/bash

#pattern "^\+[0-9]{12}$"},

echo "---------------------------------------"
echo "greedy test"

#echo "test 1" 
#curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["510-555-5556"]}' http://127.0.0.1:8080/greed/ 

echo "test 2" 
curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["510-555-5556", "412-555-5555", "412-555-5554", "412-555-5553", "412-555-5552", "412-555-5551"]}' http://127.0.0.1:8080/greed/ 

#echo "test 3" 
#curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["510-555-5556", "412-555-5555", "412-555-5554", "412-555-5553, "412-555-5552", "412-555-5551", "412-555-444"]}' http://127.0.0.1:8080/greed/ 
