#!/bin/bash

for file in *.c *.js *.py; do
  if [ -f "$file" ]; then
    first_line=$(head -n 1 "$file")
    if [[ $file == *.c && $first_line == *"/*"* || \
          $file == *.js && $first_line == *"//"* || \
          $file == *.py && $first_line == *"#"* ]]; then
      echo "Comment found in $file"
    else
      echo "No comment in $file"
    fi
  fi
done
