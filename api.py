import requests
import json
from string import Template

def requests_get(url):
    return json.loads(requests.get(url).text)


response = requests_get("https://aves.ninjas.cl/api/birds")[:20] 


bird_template = Template('''
<div>
    <img src="$url" alt="$alt">
    <p><strong>Nombre en Español:</strong> $name_es</p>
    <p><strong>Nombre en Inglés:</strong> $name_en</p>
</div>
''')


html_content = ''
for bird in response:
    bird_name_spanish = bird['name']['spanish']
    bird_name_english = bird['name']['english']
    bird_image_url = bird['images']['main'] 
    html_content += bird_template.substitute(url=bird_image_url, alt=bird_name_spanish, name_es=bird_name_spanish, name_en=bird_name_english) + '\n'


with open('template.html', 'r', encoding='utf-8') as file:
    template_html = file.read()


final_html = Template(template_html).substitute(body=html_content)


with open('aves_de_chile.html', 'w', encoding='utf-8') as file:
    file.write(final_html)

print("Archivo HTML generado con éxito: aves_de_chile.html")





