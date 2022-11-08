companies_info = {}
command = input()
while command != 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in companies_info.keys():
        companies_info[company_name] = []
    if employee_id not in companies_info[company_name]:
        companies_info[company_name].append(employee_id)
    command = input()
for company in companies_info.keys():
    print(company)
    for id in companies_info[company]:
        print(f'-- {id}')



