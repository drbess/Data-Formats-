import yaml
with open('profile.yml', 'r') as file:
    '''The line below converts YAML file into a Python dictionary'''
    data = yaml.safe_load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)


user['location']['city'] = 'Dallas'
with open('profile.yml', )