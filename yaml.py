import yaml
with open('profile.yml', 'r') as file:
    data = yaml.safe_load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)


user['location']['city'] = 'Dallas'
with open('profile.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)


def safe_load(file):
    return None
