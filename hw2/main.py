import yaml
import os
import sys
from graph_builder import build_dependency_graph
from graph_visualizer import visualize_graph

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main(config_path):
    config = load_config(config_path)

    repo_path = config['repository_path']
    target_hash = config['target_file_hash']
    visualizer_path = config['visualizer_path']

    if not os.path.exists(repo_path):
        print(f"Repository path does not exist: {repo_path}")
        sys.exit(1)

    graph = build_dependency_graph(repo_path, target_hash)

    visualize_graph(graph, visualizer_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    main(config_path)
