import re


def compile_patterns():
    patterns_and_replacements = [
        # replace single and double quotes
        (re.compile(r'''("|')(.+)\1''', re.DOTALL), r'«\2»'),
        # replace hyphen on short dash between numbers
        (re.compile(r'(\d+)‐(\d+)'), r'\1&ndash;\2'),
        # replace simple hyphen on non breaking hyphen between number and word
        (re.compile(r'(\d+)‐(\w+)'), r'\1&#8209;\2'),
        # remove extra spaces and extra new lines
        (re.compile(r'(\r\n|\n|\s){1}\1+'), r'\1'),
        # add non-breaking space between
        (re.compile(r'(\w{1,2}) (\w{3,})'), r'\1&nbsp;\2'),
        # replace hyphen on dash between spaces
        (re.compile(r'\s-\s'), r' — ')
    ]
    return patterns_and_replacements

def format_text(formatted_text):
    patterns_and_replacements = compile_patterns()
    for pattern, replacement in patterns_and_replacements:
        formatted_text = re.sub(pattern, replacement, formatted_text)
    return formatted_text
