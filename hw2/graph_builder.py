import subprocess

def get_commits_with_file(repo_path, file_hash):
    """Получить список коммитов, содержащих файл с указанным хешем."""
    cmd = ["git", "-C", repo_path, "log", "--all", "--pretty=format:%H", "--", file_hash]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout.splitlines()

def get_commit_changes(repo_path, commit_hash):
    """Получить изменения в указанном коммите."""
    cmd = ["git", "-C", repo_path, "show", "--name-status", commit_hash]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout.splitlines()

def build_dependency_graph(repo_path, file_hash):
    """Построить граф зависимостей для заданного файла."""
    commits = get_commits_with_file(repo_path, file_hash)
    if not commits:
        print(f"No commits found for file with hash: {file_hash}")
        return {}

    graph = {}
    for commit in commits:
        changes = get_commit_changes(repo_path, commit)
        print(f"Commit: {commit}\nChanges:\n{changes}")  # Отладочный вывод
        graph[commit] = changes

    if not graph:
        print("Graph is empty after processing commits.")
    return graph

