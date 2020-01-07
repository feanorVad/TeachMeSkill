#1. Написать программу, которая будет выводить первый и последний элемент списка:
#['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:',
# 'Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:','ID #:',
# 'Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone',
# 'Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:',
# 'Diagnosis 2:','Procedure:']

#2. Написать программу, которая будет выводить предпоследний элемент списка:


lst = ['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:',
'Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:', 'ID #:',
 'Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone',
 'Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:',
'Diagnosis 2:','Procedure:']
print('result as list: ', lst[:1]+lst[len(lst)-1:])
print('result as elements: ', lst[:1], '  ', lst[len(lst)-1:])
print('last element', lst[len(lst)-1])