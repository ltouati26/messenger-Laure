from datetime import datetime

server_data = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}

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
    L2=[]
    for user in server_data['channels']:
        L2.append(user['name'])
    print(L2)
    groupe = input('Select a group: ')
    for gr in L2:
        if groupe == gr:
            print(server_data['messages'][])


   
else:
    print('Unknown option:', choice)



