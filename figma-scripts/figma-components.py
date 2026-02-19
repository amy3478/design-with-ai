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


def find_node_by_id(node, target_id):
    """Recursively find a node by its ID."""
    if node.get('id') == target_id:
        return node
    
    if 'children' in node:
        for child in node['children']:
            result = find_node_by_id(child, target_id)
            if result:
                return result
    
    return None


def find_page_for_node(document, node_id):
    """Find which page contains a given node."""
    if 'children' in document:
        for page in document['children']:
            if page.get('type') == 'CANVAS':
                result = find_node_by_id(page, node_id)
                if result:
                    return page.get('name', 'Unknown Page')
    return 'Unknown Page'


def main():
    parser = argparse.ArgumentParser(
        description='List components from Figma file'
    )
    parser.add_argument('file_key', help='Figma file key')
    
    args = parser.parse_args()
    
    try:
        # Load token
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
        token = load_env_token(env_path)
        
        # Get components
        url = f"https://api.figma.com/v1/files/{args.file_key}/components"
        components_data = make_figma_request(url, token)
        
        # Get file data to find pages
        file_url = f"https://api.figma.com/v1/files/{args.file_key}"
        file_data = make_figma_request(file_url, token)
        
        document = file_data.get('document')
        
        # Extract components
        meta = components_data.get('meta', {})
        components = meta.get('components', {})
        
        print("=" * 80)
        print(f"COMPONENTS FROM: {file_data.get('name', 'Unknown')}")
        print(f"Key: {args.file_key}")
        print(f"Total Components: {len(components)}")
        print("=" * 80)
        print()
        
        if not components:
            print("No components found in this file")
            return
        
        # Print each component (API returns a list)
        if isinstance(components, list):
            comp_iter = enumerate(components, 1)
        else:
            comp_iter = ((i, v) for i, (k, v) in enumerate(components.items(), 1))
        for i, comp_data in comp_iter:
            name = comp_data.get('name', 'Unnamed')
            description = comp_data.get('description', '')
            node_id = comp_data.get('node_id', '')
            containing_frame = comp_data.get('containing_frame', {})
            
            # Try to find the page
            page_name = 'Unknown Page'
            if document:
                page_name = find_page_for_node(document, node_id)
            
            # If we have containing_frame info, use that
            if containing_frame and 'pageName' in containing_frame:
                page_name = containing_frame['pageName']
            
            print(f"{i}. {name}")
            print(f"   ID: {node_id}")
            print(f"   Node ID: {node_id}")
            print(f"   Page: {page_name}")
            
            if description:
                print(f"   Description: {description}")
            
            if containing_frame:
                frame_name = containing_frame.get('name', 'N/A')
                if frame_name and frame_name != 'N/A':
                    print(f"   Containing Frame: {frame_name}")
            
            print()
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
