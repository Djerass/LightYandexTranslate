import requests
import json




class yandexTranslateApi:
    def __init__(self,token):
        self.__token=token
        self.__get_directions_url="https://translate.yandex.net/api/v1.5/tr.json/getLangs?key="
    

    def update_token(self,new_token):
        self.__token=new_token    


    #Get all translation direction for language in language code 
    def get_directions_code(self,language_code):
        """
        language_codes are here:
        https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/
        """
        url=self.__get_directions_url+self.__token+"&ui={0}".format(language_code)
        result=requests.get(url)
        resultJson=result.json()
        if result.status_code==200:
            return resultJson['langs']
        else:
            return resultJson

    
        

if __name__=="__main__":
    translator=yandexTranslateApi("token")
    print(translator.get_directions_code.__doc__)
