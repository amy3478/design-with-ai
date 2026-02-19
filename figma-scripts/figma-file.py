#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


def load_env_token(env_path):
    """Load FIGMA_ACCESS_TOKEN from .env file."""
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        if key == 'FIGMA_ACCESS_TOKEN':
                            return value
        raise ValueError("FIGMA_ACCESS_TOKEN not found in .env file")
    except FileNotFoundError:
        raise FileNotFoundError(f".env file not found at {env_path}")


def make_figma_request(url, token):
    """Make authenticated request to Figma API."""
    headers = {
        'X-Figma-Token': token
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8', errors='replace'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        raise Exception(f"HTTP {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"URL Error: {e.reason}")


def print_tree(node, indent=0, show_type=True):
    """Recursively print node tree."""
    prefix = "  " * indent
    node_id = node.get('id', 'N/A')
    node_type = node.get('type', 'UNKNOWN')
    node_name = node.get('name', 'Unnamed')
    
    if show_type:
        print(f"{prefix}├─ [{node_type}] {node_name} (id: {node_id})")
    else:
        print(f"{prefix}├─ {node_name} (id: {node_id})")
    
    # Print children if they exist
    if 'children' in node:
        for child in node['children']:
            print_tree(child, indent + 1, show_type)


def main():
    parser = argparse.ArgumentParser(
        description='Get Figma file structure and print tree of pages, frames, and layers'
    )
    parser.add_argument('file_key', help='Figma file key')
    parser.add_argument('--depth', type=int, default=2, help='Depth of tree to fetch (default: 2)')
    
    args = parser.parse_args()
    
    try:
        # Load token
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
        token = load_env_token(env_path)
        
        # Make API request
        url = f"https://api.figma.com/v1/files/{args.file_key}?depth={args.depth}"
        data = make_figma_request(url, token)
        
        # Print file information
        print("=" * 80)
        print(f"FILE: {data.get('name', 'Unknown')}")
        print(f"Key: {args.file_key}")
        print(f"Last Modified: {data.get('lastModified', 'N/A')}")
        print(f"Version: {data.get('version', 'N/A')}")
        print("=" * 80)
        print()
        
        # Print document tree
        document = data.get('document')
        if document:
            print("DOCUMENT STRUCTURE:")
            print()
            print_tree(document)
        else:
            print("No document data found")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
