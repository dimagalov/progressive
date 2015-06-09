import vk_api

login, password = '', ''
vk = vk_api.VkApi(login, password)
vk.authorization()
tools = vk_api.VkTools(vk)

club = -22079806
posts = tools.get_all('wall.get', 1, {'owner_id': club})['items'][1:]

users = []


def is_user(link):
    return link.startswith('id')


def is_club(link):
    return link.startswith('club')


def rank_groups(groups):
    groups_info = vk.method('groups.getById', {'group_ids': ",".join(groups), 'fields': 'members_count'})
    groups_info.sort(key=lambda gr: gr['members_count'], reverse=True)
    return groups_info


def rank_users(people):
    code = """var i=0, res={}, users=%s;
    while (i < 25) {var c=API.users.get({"user_ids":users[i], "fields" : "counters"});
    res = res + c;
    i = i + 1;
    }return res;""".replace('\n', '')

    res = []
    j = 0

    to = len(people)

    while j < len(people):
        code_run = code % people[j:min(j+25, to)]
        resp = vk.method('execute', {'code': code_run})
        for user in resp:
            if 'counters' in user.keys():
                user_info = {'name': user['first_name'] + ' ' + user['last_name'], 'members_count': user['counters']['followers'],
                             'id': user['id']}
                res.append(user_info)

        j += 25

    res.sort(key=lambda user: user['members_count'], reverse=True)
    return res


def get_celeb(text):
    ans = []
    add = 1
    pos = 0

    while add:
        add = 0
        club = text.find('club', pos)
        if club != -1 and text[club - 1] == '[':
            pipe = text.find('|', club)
            ans.append(text[club:pipe])
            pos = pipe
            add = 1
    pos = 0
    add = 1
    while add:
        add = 0
        user = text.find('id', pos)
        if user != -1 and text[user - 1] == '[':
            pipe = text.find('|', user)
            ans.append(text[user:pipe])
            pos = pipe
            add = 1

    return ans

people = []
groups = []
last_post_id = posts[0]['id']

for post in posts:
    text = post['text']
    celebs = get_celeb(text)
    for celeb_id in celebs:
        if is_user(celeb_id):
            people.append(celeb_id[2:])
        elif is_club(celeb_id):
            groups.append(celeb_id[4:])

print(len(groups))

groups = list(set(groups))  # remove duplicates
ranked_groups = rank_groups(groups)
for i, gr in enumerate(ranked_groups):
    print('#%d %s %s %s' % (i, format(gr['members_count'], ',d'), gr['name'], 'vk.com/' + gr['screen_name']))

print('---------\n\n')

people = list(map(int, set(people)))  # remove duplicates
ranked_users = rank_users(people)
print(len(people), len(ranked_users))
for i, user in enumerate(ranked_users):
    print('#%d %s %s %s' % (i, format(user['members_count'], ',d'), user['name'], 'vk.com/id' + str(user['id'])))
