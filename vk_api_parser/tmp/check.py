import vk_api

app_id, login, password = 2895443, "emilchess@mail.ru", "Emilka1996"
vk = vk_api.VkApi(login=login, password=password, app_id=app_id)
print (vk.authorization())