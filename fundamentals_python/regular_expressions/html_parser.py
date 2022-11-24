import re

single_line_input = input()
title_pattern_without_ignored_symbols = r'(\<title\>)(.+?)(\<\/title\>)'
content_pattern_without_ignored_symbols = r'(\<body\>)(.+?)(\<\/body\>)'
extracted_title = re.findall(title_pattern_without_ignored_symbols, single_line_input)
extracted_content = re.findall(content_pattern_without_ignored_symbols, single_line_input)
title = extracted_title[0][1]
extracted_title = re.sub(r'[ ]+', ' ', re.sub(r'\\n', '', re.sub(r'<[^>]*>', '', title)))
content = extracted_content[0][1]
extracted_content = re.sub(r'[ ]+', ' ', re.sub(r'\\n', '', re.sub(r'<[^>]*>', '', content)))

print(f"Title: {extracted_title}")
print(f"Content: {extracted_content}")

