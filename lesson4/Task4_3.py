# 3: Программа в качестве аргументов принимает 10 разных строк, необходимо сосчитать
# количество наиболее частво встречаемых в переданных строках символов.

def find_max(st):
    d = dict()
    for i in range(0, len(st)):
        d[st[i]] = st.count(st[i])
    final_dict = {k: v for k, v in d.items() if v == max(d.values())}
    return final_dict


lst = ['1234567890hdn34750375jdfngn', '+++test++++', 'Hello, world', 'test        test',' We will use the date class of the datetime module to accomplish this task.',
     'r r r r q', 'Aabb', 'If you need to get the current date and time, you can use datetime class of the datetime module.',
     'интресно, а что будет если язык сменить ьььььь','русские А : ааааааа, латинские A: aaaa']
for i in range(0, len(lst)):
    res = find_max(lst[i])
    print('At string :', lst[i], ' most popular characters are ', list(res.keys()), ' number is ', list(res.values())[0])






