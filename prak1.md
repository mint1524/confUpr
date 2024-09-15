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

