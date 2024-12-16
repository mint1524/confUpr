# ДЗ 2

## Как запустить

1. Клонируйте репозиторий
   ```bash
   git clone https://github.com/mint1524/confUpr.git
   cd confUpr/hw2
   ```

3. Создайте гит-репозиторий, укажите данные от него в файле ```config.yaml```.  
   Пример содержимого:
   ```yaml
   visualizer_path: /usr/local/bin/mmdc
   repository_path: /Users/min7t/my_project
   target_file_hash: hello.py
   ```

4. Выполните команды в терминале:
   ```bash
   python3 main.py config.yaml
   ```

3. Проверьте результат в файле `graph.png`.  

---

## Пример результата:

![image](https://github.com/mint1524/confUpr/blob/main/hw2/graph.png)
