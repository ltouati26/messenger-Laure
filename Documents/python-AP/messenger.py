from datetime import datetime
import json

def load_server_data_from_file():
    with open('storage.json', 'r') as f:
        return json.load(f)


server_data = load_server_data_from_file()

def serialisation():
    with open('storage.json', 'w') as f:
        json.dump(server_data, f, indent=4)


print('=== Messenger ===')
print('x. Leave / y.utilisateurs/ z.groupes/ ')
choice = input('Select an option: ')
if choice == 'x':
    print('Bye!')

elif choice == 'y':
    L=[]
    for user in server_data['users']:
        L.append(user['name'])
    print(L)

elif choice =='z':
    for chanel in server_data['channels']:
        print(chanel['name'])
    groupe = input('Select a group: ')
    for gr in server_data['channels']:
        if gr['name'] == groupe:
            for message in server_data['messages']:
                if message['channel'] == gr['id']:
                    print(message['content'])

    
 
else:
    print('Unknown option:', choice)







