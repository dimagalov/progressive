# -*- coding: utf-8 -*-

__author__ = 'emil.guseynov'

from common.tools import vk_api_authorization
import time

vk_api = vk_api_authorization()
'''
st = time.time()
users = vk_api.method("users.get", values)

print (time.time() - st)

'''

threshold = 10000
pop_users = []

def write(users, f):
    for i, user in enumerate(pop_users):
        print('#%d %s %s %s' % (i, format(user['followers_count'], ',d'),str(user["cl"]), "vk.com/id"), file=f)

code = """var i=0, x=0, res={}, users=%s;
while (i<10) {var c=API.users.get({"user_ids":users.slice(x, x+100), "fields" : "followers_count", "count": 100});
if (c@.response.length)
    res = res + c;
i=i+1; x=x+100;
}return res;""".replace('\n', '')

N = 1000000000
step = 2500

st = time.time()
dump_number = 0
save_amo = 30

start = 0

for i in range(start, N, step):
    users = list(range(i, i + 2500))
    code_run = code % users
    resp = vk_api.method("execute", {"code": code_run})
    for user in resp:
        if 'followers_count' in user.keys() and user['followers_count'] > threshold:
            user_info = {'cl': user['first_name'] + ' ' + user['last_name'], 'followers_count': user['followers_count'],
                         'id': user['id']}
            pop_users.append(user_info)

            if len(pop_users) % save_amo == 0:
                with open("dump"+str(dump_number), "w") as dump_file:
                    dump_users = pop_users[-save_amo:]
                    dump_users.sort(key=lambda user: user['followers_count'], reverse=True)
                    ids = [user['id'] for user in dump_users]
                    print(ids, file=dump_file)
                    write(dump_users, dump_file)
                dump_number += 1
    print('users scanned:', start + i + 2500)

final_output = open('final_dump', 'w')
print('Done:', time.time() - st, file=final_output)

pop_users.sort(key=lambda user: user['followers_count'], reverse=True)
ids = [user['id'] for user in pop_users]
print(ids, file=final_output)
print (len(pop_users), file=final_output)
write(pop_users, f)
