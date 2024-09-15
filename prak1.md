# Практика 1

## Задача 1

```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/kal1.png)

## Задача 2

```
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -5
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/kal2.png)

## Задача 3

```
a = input()
print("+", ''.join(['-' for i in range(len(a) + 2)]), "+", sep='')
print(f"| {a} |")
print("+", ''.join(['-' for i in range(len(a) + 2)]), "+", sep='')
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal3.png)

## Задача 4

```
#!/bin/bash

file="$1"
grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file" | sort -u
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal4.png)

## Задача 5

```
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
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal5.png)

## Задача 6

```
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
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal6.png)

## Задача 7

```
#!/bin/bash

directory=$1

declare -A file_hashes

while IFS= read -r -d '' file; do
	hash=$(sha256sum "$file" | awk '{ print $1 }')
	file_hashes["$hash"]+="file"$'\n'
done < <(find "$directory" -type f -print0)

found_duplicates=false

for hash in "${!file_hashes[@]}"; do
	files="${file_hashes[$hash]}"
	files_count=$(echo -e "files" | wc -l)


	if [[ $files_count -gt 1 ]]; then
		found_duplicates=true
		echo "Dupes found:"
		echo -e "$files"
	fi
done

if ! $found_duplicates; then
	echo "No dupes."
	exit 1
fi
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal7.png)

## Задача 8

```
#!/bin/bash

directory="$1"
extension="$2"

shopt -s nullglob
files=("$directory"/*."$extension")

archive_name="${directory%/}.tar"

tar -cvf "$archive_name" -C "$directory" ./*."$extension"

echo "Архив '$archive_name' успешно создан."
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal8.png)

## Задача 9

```
#!/bin/bash

input_file="$1"
output_file="$2"

if [ ! -f "$input_file" ]; then
	echo "Ошибка: '$input_file' не найден."
	exit 1
fi

sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Заменено в файле: '$output_file'"
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal9.png)

## Задача 10

```
#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

find "$1" -type f -empty -exec file {} + | grep 'text' | awk -F: '{print $1}'
```
![image](https://github.com/mint1524/confUpr/blob/main/prak1/pics/kal10.png)


