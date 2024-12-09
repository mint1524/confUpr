# Практика 6

```bash
make dress
```

```
Putting on shirt.
Putting on pullover.
Putting on jacket.
Putting on underpants.
Putting on trousers.
Putting on socks.
Putting on shoes.
All done. Let's go outside!
```

### Задача 1

```python
import json

# Чтение данных из файла
with open('civgraph.json', 'r') as f:
    civgraph = json.load(f)

# Функция для генерации Makefile
def generate_makefile(graph, filename="Makefile"):
    with open(filename, "w") as f:
        for task, deps in graph.items():
            if deps:  # Если есть зависимости
                deps_line = " ".join(deps)
                f.write(f"{task}: {deps_line}\n")
                f.write(f"\t@echo \"{task} completed.\"\n")
            else:
                f.write(f"{task}:\n")
                f.write(f"\t@echo \"{task} completed.\"\n")

if __name__ == "__main__":
    generate_makefile(civgraph)
    print("Makefile generated.")
```

```makefile
pottery:
	@echo "pottery completed."

irrigation: pottery
	@echo "irrigation completed."

writing: pottery
	@echo "writing completed."

animal_husbandry:
	@echo "animal_husbandry completed."

archery: animal_husbandry
	@echo "archery completed."

mining:
	@echo "mining completed."

masonry: mining
	@echo "masonry completed."

bronze_working: mining
	@echo "bronze_working completed."

the_wheel: mining
	@echo "the_wheel completed."

apprenticeship: mining currency horseback_riding
	@echo "apprenticeship completed."

sailing:
	@echo "sailing completed."

celestial_navigation: sailing astrology
	@echo "celestial_navigation completed."

shipbuilding: sailing
	@echo "shipbuilding completed."

astrology:
	@echo "astrology completed."

drama_poetry: astrology irrigation masonry early_empire mysticism
	@echo "drama_poetry completed."
```

Этот файл будет продолжаться для всех целей из `civgraph.json`.

### Задача 2

```makefile
.PHONY: all clean

pottery:
	@if [ ! -f .pottery.done ]; then echo "pottery completed." > .pottery.done; fi

irrigation: pottery
	@if [ ! -f .irrigation.done ]; then echo "irrigation completed." > .irrigation.done; fi

writing: pottery
	@if [ ! -f .writing.done ]; then echo "writing completed." > .writing.done; fi

# Пример для других задач...
```

### Задача 3

```makefile
clean:
	rm -f .*.done
```

### Задача 4

```makefile
CC = gcc
TARGET = prog
SOURCES = prog.c data.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(SOURCES) -o $(TARGET)

archive: all
	dir /B > files.lst
	7z a distr.zip *.*

clean:
	rm -f $(TARGET) files.lst distr.zip
```
