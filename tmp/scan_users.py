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

code = """var i=0, x=0, res={}, users=%s;
while (i<25) {var c=API.users.get({"user_ids":users.slice(x, x+100), "fields" : "followers_count", "count": 100});
if (c@.response.length)res = res + c;
i=i+1; x=x+100;
}return res;""".replace('\n', '')

N = 1000000000
step = 2500

st = time.time()
save_amo = 30

import os.path
from time import gmtime, strftime

def get_date():
    return strftime("%Y-%m-%d %H:%M:%S")

def get_last_dump():
    for i in range(100):
        if not os.path.exists('dump'+str(i)):
            return i

def dump(data, fout):
    for i, user in enumerate(data):
        print('#%d %s %s' % (i, format(user['followers_count'], ',d'), 'vk.com/id' + str(user['id'])), file=fout)

start = 14682500
dump_number = get_last_dump()

for i in range(start, N, step):
    users = list(range(i, i + 2500))
    code_run = code % users
    resp = vk_api.method("execute", {"code": code_run})

    for user in resp:
        if 'followers_count' in user.keys() and user['followers_count'] > threshold:
            user_info = {'name': user['first_name'] + ' ' + user['last_name'], 'followers_count': user['followers_count'],
                         'id': user['id']}
            pop_users.append(user_info)
            print('yep, new user!')
            if len(pop_users) % save_amo == 0:
                with open("dump"+str(dump_number), "w") as dump_file:
                    dump_users = pop_users[-save_amo:]
                    dump_users.sort(key=lambda user: user['followers_count'], reverse=True)
                    ids = [user['id'] for user in dump_users]

                    with open('dump_history', 'a') as dump_history:
                        print(get_date(), dump_number, i+2500, file=dump_history)

                    print(ids, file=dump_file)
                    dump(dump_users, dump_file)
                dump_number += 1

final_dump = open('final_dump', 'w')
print('Done:', time.time() - st, file=final_dump)

pop_users.sort(key=lambda user: user['followers_count'], reverse=True)
ids = [user['id'] for user in pop_users]
print(ids, file=final_dump)
print (len(pop_users), file=final_dump)
dump(pop_users, final_dump)