import os, json

base_url = 'https://landregistry.github.io/llc-release-notices/releases/'

output = []

files = {'maintain': 'index.json', 'search': 'search.json'}

def create_output(service):
  output = []

  for file_object in os.scandir(f'releases/{service}'):
    filename = file_object.name
    if filename.endswith('.pdf'):
      link = f'{base_url}{service}/{filename}'.replace(' ', '%20')
      output.append({"name": filename.replace('.pdf', ''), "link": link})

    with open(files[service], 'w') as outputfile:
      json.dump(output, outputfile)

create_output('maintain')
create_output('search')