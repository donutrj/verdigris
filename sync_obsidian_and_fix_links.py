#!/usr/bin/env python3
"""
Script to sync Obsidian vault to Quartz content folder and fix Mermaid links.

This script will:
1. Delete everything from the content folder
2. Copy everything from Obsidian vault (excluding .obsidian)
3. Fix Mermaid links in Talent Trees to work with Quartz

Converts from:
<a class='internal-link is-unresolved' href='Talent List#Additives'>Additives</a>

To:
<a href='/verdigris/Characters/Talents/Talent-List#additives'>Additives</a>
"""

import re
import shutil
from pathlib import Path


def slugify_filename(filename):
    """Convert filename to Quartz URL format."""
    # Keep original case for first letter, convert spaces to hyphens
    return (
        filename.replace(" ", "-")
        .replace("&", "")
        .replace("!", "")
        .replace(",", "")
        .replace("'", "")
    )


def slugify_anchor(anchor):
    """Convert anchor text to Quartz anchor format (lowercase with hyphens)."""
    return (
        anchor.lower()
        .replace(" ", "-")
        .replace("&", "")
        .replace("!", "")
        .replace(",", "")
        .replace("'", "")
    )


def convert_mermaid_links(content):
    """Convert all Mermaid HTML links to functional format."""

    # Pattern to match the old broken links
    pattern = r"<a class=\'internal-link is-unresolved\' href=\'([^#]+)#([^\']+)\'>([^<]+)</a>"

    def replace_link(match):
        file_ref = match.group(1)  # e.g., "Talent List"
        anchor_ref = match.group(2)  # e.g., "Additives"
        display_text = match.group(3)  # e.g., "Additives"

        # Convert to Quartz URL format
        file_slug = slugify_filename(file_ref)  # "Talent-List"
        anchor_slug = slugify_anchor(anchor_ref)  # "additives"

        # Build the proper URL path with /verdigris base
        url_path = f"/verdigris/Characters/Talents/{file_slug}#{anchor_slug}"

        # Return the functional HTML link
        return f'<a href="{url_path}">{display_text}</a>'

    # Replace all matches
    converted_content = re.sub(pattern, replace_link, content)
    return converted_content


def clear_content_folder(content_path):
    """Delete everything in the content folder."""
    if content_path.exists():
        print(f"CLEARING: Deleting contents of {content_path}")
        for item in content_path.iterdir():
            if item.is_file():
                item.unlink()
                print(f"  Deleted file: {item.name}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"  Deleted folder: {item.name}")
    else:
        print(f"CREATING: Content folder doesn't exist, creating {content_path}")
        content_path.mkdir(parents=True, exist_ok=True)


def copy_obsidian_vault(obsidian_path, content_path):
    """Copy everything from Obsidian vault to content folder, excluding .obsidian."""
    if not obsidian_path.exists():
        print(f"ERROR: Obsidian vault not found at {obsidian_path}")
        return False

    print(f"COPYING: Syncing from {obsidian_path} to {content_path}")

    copied_count = 0
    for item in obsidian_path.rglob("*"):
        # Skip .obsidian folder and its contents
        if ".obsidian" in item.parts:
            continue

        # Calculate relative path from obsidian root
        relative_path = item.relative_to(obsidian_path)
        target_path = content_path / relative_path

        if item.is_file():
            # Create parent directories if they don't exist
            target_path.parent.mkdir(parents=True, exist_ok=True)
            # Copy the file
            shutil.copy2(item, target_path)
            copied_count += 1
            if copied_count <= 10:  # Show first 10 files
                print(f"  Copied: {relative_path}")
            elif copied_count == 11:
                print("  ... (more files copied)")
        elif item.is_dir():
            # Create the directory
            target_path.mkdir(parents=True, exist_ok=True)

    print(f"SUCCESS: Copied {copied_count} files from Obsidian vault")
    return True


def fix_talent_tree_links(content_path):
    """Find and fix Mermaid links in Talent Trees file."""
    talent_trees_path = content_path / "Characters" / "Talents" / "Talent Trees.md"

    if not talent_trees_path.exists():
        print(f"INFO: Talent Trees file not found at {talent_trees_path}")
        return

    try:
        # Read the file
        with open(talent_trees_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        converted_content = convert_mermaid_links(content)

        if converted_content != original_content:
            # Backup original file
            backup_path = talent_trees_path.with_suffix(
                talent_trees_path.suffix + ".backup"
            )
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(original_content)

            # Write converted content
            with open(talent_trees_path, "w", encoding="utf-8") as f:
                f.write(converted_content)

            print(f"SUCCESS: Fixed Mermaid links in {talent_trees_path}")
            print(f"BACKUP: Original saved as {backup_path}")

            # Show examples of what was changed
            original_links = re.findall(
                r"<a class=\'internal-link is-unresolved\' href=\'([^\']+)\'>([^<]+)</a>",
                original_content,
            )
            if original_links:
                print(f"EXAMPLES: Link conversions:")
                for i, (href, text) in enumerate(original_links[:3]):  # Show first 3
                    file_part, anchor_part = (
                        href.split("#", 1) if "#" in href else (href, "")
                    )
                    file_slug = slugify_filename(file_part)
                    anchor_slug = slugify_anchor(anchor_part) if anchor_part else ""
                    new_href = (
                        f"/verdigris/Characters/Talents/{file_slug}#{anchor_slug}"
                        if anchor_slug
                        else f"/verdigris/Characters/Talents/{file_slug}"
                    )
                    print(f"   {href} -> {new_href}")
                    if i >= 2:  # Only show first 3
                        break
        else:
            print(f"INFO: No broken links found in {talent_trees_path}")

    except Exception as e:
        print(f"ERROR: Error processing {talent_trees_path}: {e}")


def main():
    """Main function to sync Obsidian and fix links."""
    # Define paths
    obsidian_vault_path = Path("/home/rolland/Documents/obsidian/Verdigris")
    content_path = Path("quartz/content")

    print("=== OBSIDIAN TO QUARTZ SYNC & LINK FIXER ===")
    print(f"Source: {obsidian_vault_path}")
    print(f"Target: {content_path}")
    print()

    # Step 1: Clear content folder
    clear_content_folder(content_path)
    print()

    # Step 2: Copy from Obsidian vault
    if not copy_obsidian_vault(obsidian_vault_path, content_path):
        return
    print()

    # Step 3: Fix Mermaid links in Talent Trees
    fix_talent_tree_links(content_path)
    print()

    print("=== SYNC COMPLETE ===")
    print("Next steps:")
    print("1. Review the changes")
    print("2. Run 'git add .' to stage changes")
    print("3. Run 'git commit -m \"Sync from Obsidian and fix links\"'")
    print("4. Run 'git push origin v4' to deploy")


if __name__ == "__main__":
    main()
