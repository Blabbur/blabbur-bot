#!/bin/bash

# Execute within venv!!!!

echo "Fetching"
python3 -m sgqlc.introspection http://localhost:3200/ schema.json

echo "Generating"
sgqlc-codegen schema.json src/schema.py

rm schema.json echo "Done!"

