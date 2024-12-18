# ДЗ 3

## Описание

**Программа:** Парсер конфигурационного языка.  
**Назначение:** Преобразует входной текст на учебном языке в YAML, выявляя синтаксические ошибки.  

**Поддерживаемые конструкции:**
- **Комментарии:** `# текст`.
- **Массивы:** `{значение, значение, ...}`.
- **Словари:** `table(ключ => значение, ...)`.
- **Переменные:** `var имя значение;`.
- **Вызов переменных:** `[имя]`.

---

## Как запустить

1. Клонируйте репозиторий
   ```bash
   git clone https://github.com/mint1524/confUpr.git
   cd confUpr/hw3
   ```

3. Создайте файл конфигурации, например, `test_case_1.txt`.  
   Пример содержимого:
   ```text
   var server_name "MyServer";
   var server_ip "192.168.1.1";
   var server_ports {80, 443};

   table(
     name => [server_name],
     ip => [server_ip],
     ports => [server_ports]
   );
   ```

4. Выполните команду в терминале:
   ```bash
   python3 lingoTranslator.py < test_case_1.txt > output.yaml
   ```

3. Проверьте результат в файле `output.yaml`.  

---

## Пример результата (YAML):
```yaml
- name:
  - MyServer
  ip:
  - "192.168.1.1"
  ports:
  - - 80
    - 443
```
