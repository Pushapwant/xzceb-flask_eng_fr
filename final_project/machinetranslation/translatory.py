""" 
translatory.py
Takes either english or french phrase and converts to french and english
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

"""translator_instance"""
apikey_lt = os.environ['apikey_lt']
url_lt = os.environ['url_lt']
version_lt = os.environ['version_lt']

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(
    version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator


def englishToFrench(english_text):
    """
    Translate from English to French
    Recieves english_text to be translated
    and returns frenchTransalation
    """
    translation_response = language_translator.translate(
        text=english_text, model_id='en-fr')
    translation_response

    xlate_french_Res = translation_response.get_result()
    french_translation_is = xlate_french_Res['translations'][0]['translation']
    """
    print('The translation to French is: ', french_translation_is)
    """
    return french_translation_is


def frenchToEnglish(french_text):
    """
    Translate from french_text to English
    Recieves french_text to be translated
    and returns english_translation_is
    """
    translationEngRes = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_translation_is = translationEngRes['translations'][0]['translation']
    """ 
    print('The translation to English back from French is: ', english_translation_is)
    """
    return english_translation_is


# Testing by calling the functions and  texts for the testing
# print('french_translation_is : ' ,englishToFrench('how are you today?'))
# print('english_translation_is : ' ,frenchToEnglish('Comment vas-tu aujourd\'hui'))
