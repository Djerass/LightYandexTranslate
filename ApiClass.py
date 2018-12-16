import requests
import json




class yandexTranslateApi:
    def __init__(self,token):
        self.__token=token
        self.__get_directions_url="https://translate.yandex.net/api/v1.5/tr.json/getLangs?key="
        self.__direct_translate_url="https://translate.yandex.net/api/v1.5/tr.json/translate?key="

    
    def update_token(self,new_token):
        self.__token=new_token    


    # Get all translation direction for language in language code 
    # Return a tuple because Api don`t return status code in answer
    def get_directions_code(self,language_code):
        """
        language_codes are here:
        https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/
        """
        url=self.__get_directions_url+self.__token+"&ui={0}".format(language_code)
        result=requests.get(url)
        resultJson=result.json()
        if result.status_code==200:
            return (result.status_code,resultJson['langs'])
        else:
            return (result.status_code,resultJson)

    
    
    def direct_traslate(self,from_language_code,to_language_code,text_to_translate):
        url=self.__direct_translate_url+self.__token+"&lang={0}-{1}".format(from_language_code,to_language_code)
        return self.__translate(url,text_to_translate)

    
    def auto_detect_translate(self,to_language_code,text_to_translate):
        url=self.__direct_translate_url+self.__token+"&lang={0}".format(to_language_code)   
        return self.__translate(url,text_to_translate)
    
    
    #Translate text direct or auto detect via url
    def __translate(self,url,text_to_translate):
        requst_body={'text':text_to_translate}
        result=requests.post(url,data=requst_body)
        return result.json()
    


        

if __name__=="__main__":
    translator=yandexTranslateApi("trnsl.1.1.20181112T101031Z.997b88b88f15e476.14ffd53b805ceb2c0c03b77b6c8f0afb79a2585c")
   # print(translator.get_directions_code('ru'))
    print(translator.direct_traslate("ru","uk","Привет мир!"))
    print(translator.auto_detect_translate('az','Привет мир!'))

