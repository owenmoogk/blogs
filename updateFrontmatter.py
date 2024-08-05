import os
import re
from datetime import datetime

def convert_date(filename):
    # Extract the date part from the filename (assuming the format "apr6")
    date_str = re.search(r'([a-zA-Z]+)(\d+)', filename)
    if date_str:
        month_str, day_str = date_str.groups()
        # Convert to datetime object for formatting
        date = datetime.strptime(f"{month_str} {day_str} 2024", "%b %d %Y")
        # Format the date as "Jan 16, 2024"
        return date.strftime("%b %d, %Y")
    return None

def add_frontmatter_to_markdown(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.readlines()
            
            # Extract title from the first line starting with "##"
            title = None
            for line in content:
                if line.startswith("##"):
                    title = line.strip().lstrip("##").strip()
                    break
            
            # Convert date from filename
            date = convert_date(filename)
            
            # Prepare front matter
            if title and date:
                frontmatter = f"---\ntitle: {title}\ndate: {date}\ntags: []\n---\n"
                
                # Write back with front matter
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(frontmatter + ''.join(content))

# Specify the directory containing the markdown files
markdown_directory = "blogs"

# Add front matter to all markdown files in the directory
add_frontmatter_to_markdown(markdown_directory)
