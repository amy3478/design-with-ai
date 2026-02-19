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


def rgba_to_hex(color):
    """Convert RGBA color object to hex string."""
    r = int(color.get('r', 0) * 255)
    g = int(color.get('g', 0) * 255)
    b = int(color.get('b', 0) * 255)
    a = color.get('a', 1)
    
    if a < 1:
        return f"#{r:02x}{g:02x}{b:02x} (opacity: {a:.2f})"
    return f"#{r:02x}{g:02x}{b:02x}"


def extract_fills(fills):
    """Extract color information from fills."""
    colors = []
    if not fills:
        return colors
    
    for fill in fills:
        if fill.get('type') == 'SOLID' and fill.get('visible', True):
            color = fill.get('color')
            if color:
                colors.append(rgba_to_hex(color))
    return colors


def extract_text_style(style):
    """Extract text style information."""
    info = {}
    if 'fontFamily' in style:
        info['font'] = style['fontFamily']
    if 'fontSize' in style:
        info['size'] = f"{style['fontSize']}px"
    if 'fontWeight' in style:
        info['weight'] = style['fontWeight']
    if 'lineHeightPx' in style:
        info['line_height'] = f"{style['lineHeightPx']}px"
    if 'letterSpacing' in style:
        info['letter_spacing'] = style['letterSpacing']
    if 'textAlignHorizontal' in style:
        info['align'] = style['textAlignHorizontal']
    return info


def extract_effects(effects):
    """Extract effect information."""
    effect_list = []
    if not effects:
        return effect_list
    
    for effect in effects:
        if effect.get('visible', True):
            effect_type = effect.get('type', 'UNKNOWN')
            effect_info = {'type': effect_type}
            
            if 'color' in effect:
                effect_info['color'] = rgba_to_hex(effect['color'])
            if 'radius' in effect:
                effect_info['radius'] = effect['radius']
            if 'offset' in effect:
                offset = effect['offset']
                effect_info['offset'] = f"x:{offset.get('x', 0)}, y:{offset.get('y', 0)}"
            
            effect_list.append(effect_info)
    
    return effect_list


def find_nodes_with_styles(node, colors, text_styles, effects_list):
    """Recursively find nodes with styling information."""
    # Extract fills (colors)
    if 'fills' in node:
        node_colors = extract_fills(node['fills'])
        for color in node_colors:
            if color not in colors:
                colors.append(color)
    
    # Extract text styles
    if 'style' in node and node.get('type') in ['TEXT']:
        text_info = extract_text_style(node['style'])
        if text_info:
            text_info['name'] = node.get('name', 'Unnamed')
            # Check if similar style already exists
            if text_info not in text_styles:
                text_styles.append(text_info)
    
    # Extract effects
    if 'effects' in node:
        node_effects = extract_effects(node['effects'])
        for effect in node_effects:
            if effect not in effects_list:
                effects_list.append(effect)
    
    # Recurse through children
    if 'children' in node:
        for child in node['children']:
            find_nodes_with_styles(child, colors, text_styles, effects_list)


def main():
    parser = argparse.ArgumentParser(
        description='Extract colors, text styles, and effects from Figma file'
    )
    parser.add_argument('file_key', help='Figma file key')
    
    args = parser.parse_args()
    
    try:
        # Load token
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
        token = load_env_token(env_path)
        
        # Get file data
        url = f"https://api.figma.com/v1/files/{args.file_key}"
        data = make_figma_request(url, token)
        
        # Get styles metadata
        styles_url = f"https://api.figma.com/v1/files/{args.file_key}/styles"
        styles_data = make_figma_request(styles_url, token)
        
        # Extract styles from document
        colors = []
        text_styles = []
        effects_list = []
        
        document = data.get('document')
        if document:
            find_nodes_with_styles(document, colors, text_styles, effects_list)
        
        # Print results
        print("=" * 80)
        print(f"STYLES FROM: {data.get('name', 'Unknown')}")
        print(f"Key: {args.file_key}")
        print("=" * 80)
        print()
        
        # Print colors
        print("COLORS:")
        print("-" * 80)
        if colors:
            for i, color in enumerate(colors, 1):
                print(f"  {i}. {color}")
        else:
            print("  No colors found")
        print()
        
        # Print text styles
        print("TEXT STYLES:")
        print("-" * 80)
        if text_styles:
            for i, style in enumerate(text_styles, 1):
                print(f"  {i}. {style.get('name', 'Unnamed')}")
                for key, value in style.items():
                    if key != 'name':
                        print(f"     {key}: {value}")
                print()
        else:
            print("  No text styles found")
        print()
        
        # Print effects
        print("EFFECTS:")
        print("-" * 80)
        if effects_list:
            for i, effect in enumerate(effects_list, 1):
                print(f"  {i}. Type: {effect.get('type')}")
                for key, value in effect.items():
                    if key != 'type':
                        print(f"     {key}: {value}")
                print()
        else:
            print("  No effects found")
        print()
        
        # Print published styles metadata
        print("PUBLISHED STYLES:")
        print("-" * 80)
        meta = styles_data.get('meta', {})
        if meta.get('styles'):
            for style_id, style_meta in meta['styles'].items():
                print(f"  • {style_meta.get('name', 'Unnamed')}")
                print(f"    Type: {style_meta.get('style_type', 'N/A')}")
                print(f"    Description: {style_meta.get('description', 'N/A')}")
                print()
        else:
            print("  No published styles found")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
