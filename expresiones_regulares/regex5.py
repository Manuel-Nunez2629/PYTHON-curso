import re 

example = "Este es un ejemplo de una pagina web: https://www.example.com y tambien puedes visitar https://www.example.org  https://nanuproject.com"

pattern = 'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern,example)

print(result)