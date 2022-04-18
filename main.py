import requests as req
import json
url = "https://www.gosuslugi.ru/covid-cert/status/14d22f26-9cf2-4437-addd-51f155c63f72?lang=ru"
#url = "https://www.gosuslugi.ru/covid-cert/verify/7000000025591744?lang=ru&ck=ceb553b6ad74f2dd1e9e78e84401e13e"


def main():
    gos_id = url[url.rfind('/')+1:url.find('?')]
    print(gos_id)
    json_url = "https://www.gosuslugi.ru/api/covid-cert-checker/v3/cert/status/" + gos_id
    response = req.get(json_url)
    if response.status_code == 400:
        print("error")
    else:
        json_text = response.text
        doc = json.loads(json_text)
        cert_id = doc["certId"]
        expiration_date = doc["expiredAt"]
        valid_from_date = doc["validFrom"]
        full_name = doc["attrs"][0]['value']
        birthday_date = doc["attrs"][1]['value']
        passport = doc["attrs"][2]['value']
        print(cert_id)
        print(valid_from_date)
        print(expiration_date)
        print(full_name)
        print(birthday_date)
        print(passport)


if __name__ == "__main__":
    main()
