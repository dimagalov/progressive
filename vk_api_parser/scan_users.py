from common.tools import vk_api_authorization
import time

vk_api = vk_api_authorization()

user_ids = "297428682,215857269,282608614,209326050,300442791,247142799,294964372,292963385,19293783,245624363,270930,7184223,205387401,243556640,273252257,265870743,262859464,271305862,181460341,8380476,280340136,6778953,274999264,254585226,1873847,297902946,55126687,278774028,38537529,8079991,211225393,11527726,1211687,5592362,269793053,290697449,135454327,55325758,5902060,185246850,3883830,53450688,2128351,199378676,14119525,53083705,72637871,198977223,28531860,294233808,282672625,301419447,302027280,271138000,253289216,5194243,40434887,302954483,7039106,5436593,209991765,302262930,1874874,300532117,190868,5795119,32252121,292653561,292243967,279938622,69"
values = {
    "user_ids": user_ids,
    "fields": "followers_count,verified",
    "count": 69
}

'''
st = time.time()
users = vk_api.method("users.get", values)

print (time.time() - st)

'''

threshold = 10000
pop_users = []

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
save_amo = 300

for i in range(0, N, step):
    users = list(range(i, i + 2500))
    code_run = code % users
    resp = vk_api.method("execute", {"code": code_run})
    for user in resp:
        if 'followers_count' in user.keys() and user['followers_count'] > threshold:
            user_info = {'name': user['first_name'] + ' ' + user['last_name'], 'followers_count': user['followers_count'],
                         'id': user['id']}
            pop_users.append(user_info)

            if len(pop_users) % save_amo == 0:
                with open("dump"+str(dump_number), "w") as dump_file:
                    dump_users = pop_users[-save_amo:]
                    dump_users.sort(key=lambda user: user['followers_count'], reverse=True)
                    ids = [user['id'] for user in dump_users]
                    print(ids, file=dump_file)
                    for i, user in enumerate(dump_users):
                        print('#%d %s %s %s' % (i, format(user['followers_count'], ',d'), user['name'], 'vk.com/id' + str(user['id'])), file=dump_file)
                dump_number += 1

final_output = open('final', 'w')
print('Done:', time.time() - st, file=final_output)

pop_users.sort(key=lambda user: user['followers_count'], reverse=True)
ids = [user['id'] for user in pop_users]
print(ids, file=final_output)
print (len(pop_users), file=final_output)


for i, user in enumerate(pop_users):
    print('#%d %s %s %s' % (i, format(user['followers_count'], ',d'), user['name'], 'vk.com/id' + str(user['id'])), file=final_output)
