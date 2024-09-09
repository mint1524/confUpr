#!/bin/bash

input_file="$1"
output_file="$2"

if [ ! -f "$input_file" ]; then
	echo "Ошибка: '$input_file' не найден."
	exit 1
fi

sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Заменено в файле: '$output_file'"
