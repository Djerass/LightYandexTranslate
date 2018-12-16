import requests
import json




class yandexTranslateApi:
    def __init__(self,token):
        self.__token=token
        self.__get_directions_url="https://translate.yandex.net/api/v1.5/tr.json/getLangs?key="
        self.__direct_translate_url="https://translate.yandex.net/api/v1.5/tr.json/translate?key="
        self.__detect_language_url="https://translate.yandex.net/api/v1.5/tr.json/detect?key="
    
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
    

    def detect_language(self,text_to_detect,*args_lagnage_codes):
        url=self.__detect_language_url+self.__token
        if len(args_lagnage_codes)!=0:
            hint="&hint="
            for language_code in args_lagnage_codes:
                hint+="{0},".format(language_code)
            hint=hint[0:-1]
            url+=hint     
        request_body={'text':text_to_detect}
        result=requests.post(url,data=request_body)
        return result.json()

        

if __name__=="__main__":
    translator=yandexTranslateApi("token")
    print(translator.get_directions_code('ru'))
    print(translator.direct_traslate("ru","uk","Привет мир!"))
    print(translator.auto_detect_translate('az','Привет мир!'))
    print(translator.detect_language("Hello world"))

