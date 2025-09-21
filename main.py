from pyscript import document, display

def generate_message(e):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"""
Student Profile:
Name: {name}
Age: {age}
School: {school}

Notes:
{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed using a multiline string in Python via PyScript.
"""

    display(message, target="profileOutput")

