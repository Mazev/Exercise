company_dict = {}

command = input()
while not command == 'End':
    company_name, emploee_id = command.split(' -> ')
    if not company_name in company_dict:
        company_dict[company_name] = []
    if emploee_id not in company_dict:
        company_dict[company_name].append(emploee_id)


    command = input()

for company_name, emploee_id in sorted(company_dict.items(), key= lambda x: x[0]):
    print(company_name)
    for i in emploee_id:
        print(f'-- {i}')

