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


def download_file(url, output_path):
    """Download file from URL to output path."""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            with open(output_path, 'wb') as f:
                f.write(data)
        return True
    except Exception as e:
        raise Exception(f"Download failed: {e}")


def sanitize_filename(name):
    """Sanitize string for use as filename."""
    # Replace invalid filename characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name


def main():
    parser = argparse.ArgumentParser(
        description='Download Figma frame images'
    )
    parser.add_argument('file_key', help='Figma file key')
    parser.add_argument('--node-ids', required=True, help='Comma-separated list of node IDs to export')
    parser.add_argument('--format', choices=['png', 'svg'], default='png', help='Export format (default: png)')
    parser.add_argument('--scale', type=int, default=2, help='Scale for PNG export (default: 2)')
    parser.add_argument('--out', default='./exports', help='Output directory (default: ./exports)')
    
    args = parser.parse_args()
    
    try:
        # Load token
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
        token = load_env_token(env_path)
        
        # Parse node IDs
        node_ids = [nid.strip() for nid in args.node_ids.split(',')]
        
        # Build API URL
        ids_param = ','.join(node_ids)
        url = f"https://api.figma.com/v1/images/{args.file_key}?ids={ids_param}&format={args.format}"
        
        if args.format == 'png':
            url += f"&scale={args.scale}"
        
        print(f"Requesting images for {len(node_ids)} node(s)...")
        print(f"Format: {args.format}, Scale: {args.scale if args.format == 'png' else 'N/A'}")
        print()
        
        # Make API request
        data = make_figma_request(url, token)
        
        # Check for errors
        if 'err' in data and data['err']:
            raise Exception(f"API Error: {data['err']}")
        
        images = data.get('images', {})
        
        if not images:
            print("No images returned from API")
            sys.exit(1)
        
        # Create output directory
        output_dir = Path(args.out)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Downloading to: {output_dir.resolve()}")
        print("-" * 80)
        
        # Download each image
        success_count = 0
        for node_id, image_url in images.items():
            if not image_url:
                print(f"✗ {node_id}: No image URL returned (node may not exist or is not exportable)")
                continue
            
            # Create filename
            safe_node_id = sanitize_filename(node_id)
            filename = f"{safe_node_id}.{args.format}"
            output_path = output_dir / filename
            
            try:
                download_file(image_url, output_path)
                file_size = output_path.stat().st_size
                print(f"✓ {node_id} → {filename} ({file_size:,} bytes)")
                success_count += 1
            except Exception as e:
                print(f"✗ {node_id}: {e}")
        
        print("-" * 80)
        print(f"Downloaded {success_count}/{len(node_ids)} images successfully")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
