#!/bin/bash

command_name="$1"
command_path="./$command_name"

if [ ! -f "$command_path" ]; then
	echo "File '$command_path' not found."
	exit 1
fi

sudo chmod +x "$command_name"
sudo cp "$command_path" /usr/local/bin/

if [ $? -ne 0 ]; then
	echo "Can't copy file."
	exit 1
fi

sudo chmod 775 /usr/local/bin/"$command_name"

if [ $? -ne 0 ]; then
	echo "Can't set the rules for '$command_name'."
	exit 1
fi

echo "File '$command_name' registrated successfully."
