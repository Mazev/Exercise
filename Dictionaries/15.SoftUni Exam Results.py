results = {}
language_dict = {}
data = input()
while not data == 'exam finished':
    token = data.split('-')
    username = token[0]
    language_or_command = token[1]
    points = token [2]
    if not username in results:
        results[username] = points
    if not language_or_command in language_dict:
        language_dict[language_or_command] = []
    if username not in language_dict:
        language_dict[language_or_command].append(username)
    elif username in results:
        for key in results.keys():
            if results[key] > points:
                continue
            else:
                results[key] = points

    if language_or_command == 'bannet':
        results[username].remove([username])

    data = input()

print('Results:')
for username, points in results.items():
    print(f'{username} | {points}')
print('Submissions:')
for language_or_command, username in language_dict.items():
    print(f'{language_or_command} - {len(username)}')
