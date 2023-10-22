# import requests
# import ssl
# import requests

# # Set the desired TLS version
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)




# FOLDER_ID = "b121grjjgjkjkjgm2dm9dcadahghkl5hkk7lhjhasda1lklhhhghj23"
# IAM_TOKEN = "t1.9euasdelZqVx5maj4yYlZjHkpqQl5eelO3rnpWaipydsadncubjZCpdfgWlJ6RmZOMi5rl8_dJaytW-hjkhje9xbXot_N3fddfghdhfd234z9wkaKV'llk;b573Ftei38zefsdlkjl1656VmpuVy4uPjMeal5iQisaTyM2S7_zF656VmpuVy4uPjMeal5iQisaTyM2S.jqO8W5LmcyqZeopyrwVF1Sbw3p-M9YhhAOQtPyLX7RmZEmdXdKka2vVSlwSpGNyxxG77qxCrXLBUFaddd_3LAg"

# with open("rus.ogg", "rb") as f:
#     data = f.read()

# params = {
#     "topic": "general",
#     "folderId": FOLDER_ID,
#     "lang": "ru-RU"
# }

# url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"

# headers = {
#     "Authorization": f"Bearer {IAM_TOKEN}"
# }


# response = requests.post(url, params=params, headers=headers, data=data)
# decodedData = response.json()

# if "error_code" not in decodedData:
#     print(decodedData.get("result"))



import requests
import time
import json

# Вставьте свой API-ключ 

#предисловие маленькое если кто читать будет конечно
#вобщем это написано не через IAM токен а через сервисный аккаунт потому что этот токен да и в целом код из примера на сайте не рабочий из за ошибок где то в ssl
#мне было лень в этом разбираться соу я просто пошел искать рабочие решения коих особо нет и пришлось пересоздать велосипед
#короче весь код сверху в коментах не рабочий и апи ключи тоже а распознование речи от яндекс редкостная фигня как и весь яндекс клауд в целом(максимально он мне не понравился и опыт использования херовый)
#не советую его использовать и тем более платить ИМХО
#чуть не забыл, этот текст в файле output это текст песини КиШ Лесник (машины с такими то умениями точно захватит мир :) )



# Вставьте свой API-ключ 
key = '<ваш апи здесь>'

 
# Вставьте свой путь к файлу в бакете. Всё, что в ссылке стоит после знака вопроса, можно стереть — сервер всё равно это проигнорирует
filelink = '<ваша ссылка на файл здесь>'


POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"


body ={

    "config": {

        "specification": {

            "languageCode": "ru-RU"

        }

    },

    "audio": {

        "uri": filelink

    }

}



header = {'Authorization': 'Api-Key {}'.format(key)}


req = requests.post(POST, headers=header, json=body)


data = req.json()

print(data)


id = data['id']


while True:


    time.sleep(1)


    GET = "https://operation.api.cloud.yandex.net/operations/{id}"

    req = requests.get(GET.format(id=id), headers=header)

    req = req.json()


    if req['done']: break


    print("Ещё не готово")


print("Текст:")


with open("output.txt", "w", encoding="utf-8") as f:
    for chunk in req['response']['chunks']:
        text = chunk['alternatives'][0]['text']
        de_text = text.encode("utf-8").decode("utf-8")
        f.write(de_text + "\n")
