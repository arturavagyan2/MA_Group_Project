with open('setup.py', 'r', encoding='utf-8') as file:
    content = file.read()

clean_content = content.encode('utf-8', 'ignore').decode('utf-8')

with open('setup.py', 'w', encoding='utf-8') as file:
    file.write(clean_content)
