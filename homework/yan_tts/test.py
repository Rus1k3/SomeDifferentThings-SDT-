import requests
import time

# Вставьте свой API-ключ 
key = '<ваш апи здесь>'

 
# Вставьте свой путь к файлу в бакете.
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