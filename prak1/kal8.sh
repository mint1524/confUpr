#!/bin/bash

directory="$1"
extension="$2"

shopt -s nullglob
files=("$directory"/*."$extension")

archive_name="${directory%/}.tar"

tar -cvf "$archive_name" -C "$directory" ./*."$extension"

echo "Архив '$archive_name' успешно создан."
