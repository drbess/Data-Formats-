import json
with open('profile.json', 'r') as file:
    data = json.load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)


user = ['location']['city'] = 'Dallas'
with open('profile_update.json', 'w') as file:
    json.dump(data, file, indent=4)