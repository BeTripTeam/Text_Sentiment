import re
from langdetect import detect, lang_detect_exception


def is_en(text):
    cyril2 = re.findall(u"[\u0400-\u0500]+", text)
    return len(cyril2) == 0


def detect_lang(text):
    try:
        return detect(text)
    except lang_detect_exception.LangDetectException as e:
        return 'unknown'
