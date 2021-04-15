import pyperclip, re


# Create a phone regex.


phone_regex = re.compile(r'''(

    (\d{3}|\(\d{3}\))?
    (\s|-|\.)
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s|-|\.)
    (\s*(ext|x|ext.)\s*(\d{2, 5}))?
    )''', re.VERBOSE)


# Create a email regex.


email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)


# Find matches in clipboard.


text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])


#  Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("\nCopied to clipboard:\n")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")
