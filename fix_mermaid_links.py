#!/usr/bin/env python3
"""
Script to convert broken Mermaid HTML links to functional web links in Quartz.

Converts from:
<a class='internal-link is-unresolved' href='Talent List#Additives'>Additives</a>

To:
<a href='/Characters/Talents/Talent-List#additives'>Additives</a>
"""

import re
import sys
from pathlib import Path

def slugify_filename(filename):
    """Convert filename to Quartz URL format."""
    return filename.lower().replace(' ', '-').replace('&', '').replace('!', '').replace(',', '').replace("'", '')

def slugify_anchor(anchor):
    """Convert anchor text to Quartz anchor format."""
    return anchor.lower().replace(' ', '-').replace('&', '').replace('!', '').replace(',', '').replace("'", '')

def convert_mermaid_links(content):
    """Convert all Mermaid HTML links to functional format."""
    
    # Pattern to match the old broken links
    pattern = r'<a class=\'internal-link is-unresolved\' href=\'([^#]+)#([^\']+)\'>([^<]+)</a>'
    
    def replace_link(match):
        file_ref = match.group(1)  # e.g., "Talent List"
        anchor_ref = match.group(2)  # e.g., "Additives"
        display_text = match.group(3)  # e.g., "Additives"
        
        # Convert to Quartz URL format
        file_slug = slugify_filename(file_ref)
        anchor_slug = slugify_anchor(anchor_ref)
        
        # Build the proper URL path
        url_path = f"/Characters/Talents/{file_slug}#{anchor_slug}"
        
        # Return the functional HTML link
        return f'<a href="{url_path}">{display_text}</a>'
    
    # Replace all matches
    converted_content = re.sub(pattern, replace_link, content)
    return converted_content

def process_file(file_path):
    """Process a single file to convert its Mermaid links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        converted_content = convert_mermaid_links(content)
        
        if converted_content != original_content:
            # Backup original file
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write converted content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(converted_content)
            
            print(f"SUCCESS: Converted {file_path}")
            print(f"BACKUP: Backup saved as {backup_path}")
            
            # Show a few examples of what was changed
            original_links = re.findall(r'<a class=\'internal-link is-unresolved\' href=\'([^\']+)\'>([^<]+)</a>', original_content)
            if original_links:
                print(f"EXAMPLES: Examples of conversions:")
                for i, (href, text) in enumerate(original_links[:3]):  # Show first 3
                    file_part, anchor_part = href.split('#', 1) if '#' in href else (href, '')
                    file_slug = slugify_filename(file_part)
                    anchor_slug = slugify_anchor(anchor_part) if anchor_part else ''
                    new_href = f"/Characters/Talents/{file_slug}#{anchor_slug}" if anchor_slug else f"/Characters/Talents/{file_slug}"
                    print(f"   {href} -> {new_href}")
                    if i >= 2:  # Only show first 3
                        break
        else:
            print(f"INFO: No changes needed in {file_path}")
            
    except Exception as e:
        print(f"ERROR: Error processing {file_path}: {e}")

def main():
    """Main function to process files."""
    if len(sys.argv) > 1:
        # Process specific files provided as arguments
        for file_arg in sys.argv[1:]:
            file_path = Path(file_arg)
            if file_path.exists():
                process_file(file_path)
            else:
                print(f"ERROR: File not found: {file_path}")
    else:
        # Default: process Talent Trees.md
        default_file = Path("quartz/content/Characters/Talents/Talent Trees.md")
        if default_file.exists():
            process_file(default_file)
        else:
            print(f"ERROR: Default file not found: {default_file}")
            print("Usage: python fix_mermaid_links.py [file1] [file2] ...")
            print("Or run from the project root to process the default Talent Trees.md file")

if __name__ == "__main__":
    main()
