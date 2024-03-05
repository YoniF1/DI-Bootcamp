#1-5

sentence = "Volkswagen,Toyota,Ford Motor,Honda,Chevrolet"
sentence_list = sentence.split(',')
print(f"There are {len(sentence_list)} companies in the list")

sentence_list.sort(reverse=True)
print(sentence_list)

o_companies = [company for company in sentence_list if 'o' in company]
print(o_companies)

i_companies = [company for company in sentence_list if 'i' not in company]
print(len(i_companies))

#6

company_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

company_set = set(company_list)
company_list = list(company_set)
print(company_list)

company_string = ','.join(company_list)

print(company_string)
print(f"There are {len(company_list)} companies in the list")

#7

reversed_list = []

for company in company_list:
    reversed = company[::-1]
    reversed_list.append(reversed)

reversed_list.sort()
print(reversed_list)