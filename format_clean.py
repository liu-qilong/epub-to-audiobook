import re
import sys

# get the file path from command line arguments
file_path = sys.argv[1]

with open(file_path, 'r') as file:
    content = file.read()

# remove fenced code block
modified_content = re.sub(r':::.*?:::', '', content, flags=re.DOTALL)

# remove div block
modified_content = re.sub(r'<div>.*?</div>', '', modified_content, flags=re.DOTALL)

# remove content list
modified_content = re.sub(r'^.* kindle-.*$', '', modified_content, flags=re.MULTILINE)

# remove pattern [^\[text\]^](link)
modified_content = re.sub(r'\[\^\\\[[^\]]+\]\^\]\([^)]*\)', '', modified_content, flags=re.DOTALL)

# remove pattern [text](link)
modified_content = re.sub(r'\[[^]]*\]\([^)]*\)', '', modified_content, flags=re.DOTALL)

# remove pattern [text]{link}
modified_content = re.sub(r'\[[^]]*\]{[^}]*}', '', modified_content, flags=re.DOTALL)

# remove pattern {link}
modified_content = re.sub(r'{[^}]*}', '', modified_content, flags=re.DOTALL)

# remove pattern [^\[text\]^]
modified_content = re.sub(r'\[\^\\\[[^\]]+\]\^\]', '', modified_content, flags=re.DOTALL)

# output
with open(file_path, 'w') as file:
    file.write(modified_content)