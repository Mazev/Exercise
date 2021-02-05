# force_user = {}
#
# command = input()
# while not command == 'Lumpawaroo':
#     token = command.split()
#
#     if token[1] == '|':
#         if not token[0] in force_user:
#             force_user[token[0]] = []
#         force_user[token[0]].append(token[2])
#
#     elif token[2] == '->':
#         for value in force_user.values():
#             if not value in force_user:
#                 force_user[token[0]].append(token[2])
#
#     command = input()
