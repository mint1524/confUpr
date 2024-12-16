import sys
import yaml
import re

class ConfigParser:
    def __init__(self):
        self.variables = {}

    def parse(self, text):
        lines = text.splitlines()
        result = []
        current_table = None  # Переменная для накопления строк таблицы
        inside_table = False

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):  # Пропуск комментариев
                continue
            if line.startswith("var"):  # Объявление переменной
                self.parse_var(line)
            elif line.startswith("table"):  # Начало таблицы
                if inside_table:  # Уже внутри таблицы
                    current_table += line
                else:
                    inside_table = True
                    current_table = line
            elif line.endswith(')') and inside_table:  # Закрытие таблицы
                current_table += line
                result.append(self.parse_table(current_table))
                inside_table = False
                current_table = None
            elif inside_table:  # Если внутри таблицы, продолжаем собирать строки
                current_table += line
            elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', line):  # Константа
                result.append(self.evaluate_variable(line))
            else:
                raise ValueError(f"Syntax error in line: {line}")
        return result

    def parse_var(self, line):
        match = re.match(r'var (\w+) (.+);', line)
        if match:
            var_name = match[1]
            var_value = match[2].strip()
            self.variables[var_name] = var_value
        else:
            raise ValueError(f"Invalid variable declaration: {line}")

    def parse_table(self, line):
        # Словарь
        match = re.match(r'table\((.*)\)', line)
        if match:
            items = match[1].strip()
            if items:  # Если внутри таблицы есть элементы
                table = {}
                key_value_pairs = self.split_items(items)
                for item in key_value_pairs:
                    key_value = item.split('=>')
                    if len(key_value) != 2:
                        raise ValueError(f"Invalid key-value pair: {item}")
                    key = key_value[0].strip()
                    value = key_value[1].strip()
                    table[key] = self.evaluate_expression(value)
                return table
            else:  # Пустая таблица
                return {}
        else:
            raise ValueError(f"Invalid table syntax: {line}")

    def split_items(self, items):
        # Метод для правильного разделения элементов таблицы на пары ключ-значение
        # учтет вложенные структуры
        result = []
        depth = 0
        current_item = []
        for char in items:
            if char == ',' and depth == 0:
                result.append(''.join(current_item).strip())
                current_item = []
            else:
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                current_item.append(char)
        if current_item:
            result.append(''.join(current_item).strip())
        return result

    def parse_array(self, line):
        # Массив
        match = re.match(r'\{(.*)\}', line)
        if match:
            items = match[1].strip().split(',')
            return [self.evaluate_expression(item.strip()) for item in items]
        else:
            raise ValueError(f"Invalid array syntax: {line}")

    def evaluate_expression(self, expr):
        # Обработка массива, выражения внутри []
        if expr.startswith("[") and expr.endswith("]"):  # Обработка массивов
            inner_expr = expr[1:-1].strip()  # Убираем квадратные скобки
            # Разбираем элементы внутри массива
            items = inner_expr.split(',')
            return [self.evaluate_expression(item.strip()) for item in items]
        elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', expr):  # Переменная
            return self.evaluate_variable(expr)
        elif expr.isdigit():  # Число
            return int(expr)
        elif expr.startswith('"') and expr.endswith('"'):  # Строка
            return expr[1:-1]
        elif expr.startswith("{") and expr.endswith("}"):  # Обработка массива в скобках
            return self.parse_array(expr)
        else:
            raise ValueError(f"Invalid expression: {expr}")

    def evaluate_variable(self, var_name):
        # Оценка значения переменной
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise ValueError(f"Undefined variable: {var_name}")

# Основная логика для преобразования и вывода
def convert_to_yaml(text):
    parser = ConfigParser()
    try:
        parsed_data = parser.parse(text)
        return yaml.dump(parsed_data, default_flow_style=False, allow_unicode=True)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Чтение конфигурации из стандартного ввода
    input_text = sys.stdin.read()
    
    # Преобразование в YAML и вывод
    output_text = convert_to_yaml(input_text)
    sys.stdout.write(output_text)
