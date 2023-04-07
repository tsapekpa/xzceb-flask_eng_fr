'''
Final Project
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtxt=None):
    '''
    Tranlate English to French
    '''
    if englishtxt is None:
        frenchtxt = "You need to provide text"
    else:
        translation_response=language_translator.translate(text=englishtxt, model_id='en-fr')
        translation = translation_response.get_result()
        frenchtxt = translation['translations'][0]['translation']

    return frenchtxt


def french_to_english(frenchtxt=None):
    '''
    Translate French to English
    '''
    if frenchtxt is None:
        englishtxt = "Vous devez fournir du texte"
    else:
        translation_response=language_translator.translate(text=frenchtxt, model_id='fr-en')
        translation = translation_response.get_result()
        englishtxt = translation['translations'][0]['translation']

    return englishtxt
