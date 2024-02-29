# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = {}
for k, v in users.items():
    if k == '景太郎':
        active_users[k] = v
print("this is our active users =", active_users)
