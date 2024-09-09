#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

find "$1" -type f -empty -exec file {} + | grep 'text' | awk -F: '{print $1}'
