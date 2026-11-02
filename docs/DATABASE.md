Study Place – Database Documentation

Model: CodeSnippet

File: "snippets/models.py"

Purpose:
This model stores programming code snippets and their related information in the database.

---

1. title

- Field Type: CharField
- Maximum Length: 200 characters
- Required: Yes
- Purpose: Stores the name or title of the code snippet.
- What to Enter: A short and meaningful name describing the code.
- Example: HTML Basic Structure

2. language

- Field Type: CharField
- Maximum Length: 50 characters
- Required: Yes
- Purpose: Stores the programming language used in the code.
- What to Enter: The language in which the code is written.
- Examples: HTML, CSS, JavaScript, Python, PHP.

3. description

- Field Type: TextField
- Required: No
- Purpose: Stores a short explanation of the code.
- What to Enter: Explain what the code does and why it is useful.
- Example: This code creates the basic structure of an HTML webpage.

4. code

- Field Type: TextField
- Required: Yes
- Purpose: Stores the actual source code.
- What to Enter: Write or paste the complete code snippet.
- Example:

<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>

5. category

- Field Type: CharField
- Maximum Length: 100 characters
- Required: No
- Purpose: Groups related code snippets into categories.
- What to Enter: A category describing the purpose of the code.
- Examples: Frontend, Backend, Database, Programming Basics.

6. is_favorite

- Field Type: BooleanField
- Required: No
- Default Value: False
- Purpose: Identifies whether a code snippet is marked as a favorite.
- What to Enter: True or False.
- Example: True means the user has marked the snippet as a favorite.

7. created_at

- Field Type: DateTimeField
- Automatically Generated: Yes
- Purpose: Stores the date and time when the snippet was first created.
- User Input: Not required.
- Note: Uses "auto_now_add=True".

8. updated_at

- Field Type: DateTimeField
- Automatically Generated: Yes
- Purpose: Stores the date and time of the last update.
- User Input: Not required.
- Note: Uses "auto_now=True".

---

Model Summary

Field| Data Type| Required
title| CharField| Yes
language| CharField| Yes
description| TextField| No
code| TextField| Yes
category| CharField| No
is_favorite| BooleanField| No
created_at| DateTimeField| Auto
updated_at| DateTimeField| Auto

Important Notes

1. Never store executable code as a Python file automatically. Store snippets as text.
2. Code formatting and indentation should be preserved.
3. Use the correct programming language when saving a snippet.
4. Creation and update timestamps are managed automatically.
5. Future model changes must also be documented here.

---

Last Updated: Phase 2 – Database Design

Related File: "snippets/models.py"