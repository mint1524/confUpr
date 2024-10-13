# Практика 3

## Задача 1

```
local groups = ["ИКБО-" + std.asciiUpper(i) + "-23" for i in std.range(1, 24)];

local students = [
  { age: 19, group: "ИКБО-4-23", name: "Иванов И.И." },
  { age: 18, group: "ИКБО-5-23", name: "Петров П.П." },
  { age: 18, group: "ИКБО-5-23", name: "Сидоров С.С." },
  { age: 18, group: "ИКБО-62-23", name: "Кузин Д.М." }  // добавлен 4-й студент
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление"
}
```

## Задача 2

```
let List = https://prelude.dhall-lang.org/List/package.dhall

let groups =
      List.generate
        24
        (\(i : Natural) -> "ИКБО-" ++ Natural/show (i + 1) ++ "-23")

let Student = { age : Natural, group : Text, name : Text }

let students : List Student =
      [ { age = 19, group = "ИКБО-4-23", name = "Иванов И.И." }
      , { age = 18, group = "ИКБО-5-23", name = "Петров П.П." }
      , { age = 18, group = "ИКБО-5-23", name = "Сидоров С.С." }
      , { age = 18, group = "ИКБО-62-23", name = "Кузин Д.М." }
      ]

in  { groups = groups
    , students = students
    , subject = "Конфигурационное управление"
    }
```

## Задача 3

Пример БНФ:

```
E = '0' | '1' | E '0' | E '1'
```

Код на Python:

```
BNF = '''
E = 0 | 1 | E 0 | E 1
'''
```
![image](https://github.com/mint1524/confUpr/blob/main/prak3/kal3.1.png)

## Задача 4

Пример БНФ:

```
E = '' | '(' E ')' | '{' E '}' | E E
```

Код на Python:

```
BNF = '''
E = | ( E ) | { E } | E E
'''
```
![image](https://github.com/mint1524/confUpr/blob/main/prak3/kal3.2.png)

## Задача 5

Пример БНФ:

```
E  = T | E '|' T                   // Операция "ИЛИ"
T  = F | T '&' F                   // Операция "И"
F  = 'x' | 'y' | '~' G | G         // Переменные, отрицание и скобки
G  = '(' E ')' | 'x' | 'y'         // Скобки и переменные без вложенных отрицаний
```

Код на Python:

```
BNF = '''
E = T | E '|' T
T = F | T '&' F
F = x | y | ~ G | G
G = ( E ) | x | y
'''
```
![image](https://github.com/mint1524/confUpr/blob/main/prak3/kal3.3.png)
