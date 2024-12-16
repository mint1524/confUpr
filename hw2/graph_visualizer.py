import subprocess
import re

def create_mermaid_code(graph):
    """Сгенерировать код для Mermaid."""
    nodes = []
    links = []

    for commit, changes in graph.items():
        # Извлекаем только хеш коммита, без других данных (автор, дата и т.п.)
        commit_hash = commit.split(" ")[0]
        nodes.append(f'{commit_hash}["Commit {commit_hash[:7]}"]')
        
        for change in changes:
            # Игнорируем строки с информацией об авторе, дате и других метаданных
            if not change.startswith(('commit', 'Author', 'Date')):  # Убираем строки с метаданными
                # Игнорируем строки, которые не содержат изменений
                if change.startswith(('M', 'A', 'D')):  # Modified, Added, Deleted
                    # Извлекаем имя файла, убираем лишние пробелы и символы
                    file = change.split("\t")[-1].strip()
                    # Заменяем символы, которые могут вызвать ошибку в Mermaid
                    file = re.sub(r'[<>:"/\\|?*]', '_', file)  # Заменяем неподобающие символы на '_'
                    nodes.append(f'{file}["{file}"]')
                    links.append(f'{commit_hash} --> {file}')

    nodes = "\n".join(set(nodes))  # Убираем дубли
    links = "\n".join(links)
    return f"""
graph TD
{nodes}
{links}
"""


def visualize_graph(graph, visualizer_path):
    """Визуализировать граф."""
    mermaid_code = create_mermaid_code(graph)

    with open("graph.mmd", "w") as f:
        f.write(mermaid_code)

    cmd = [visualizer_path, "-i", "graph.mmd", "-o", "graph.png"]
    subprocess.run(cmd)
    print("Graph saved to graph.png")
