import random

from xml.etree import ElementTree

import requests

from core.settings import MAIN_URL
from parser.services.helpers import xml_render, get_static_params


def login(phone: str):
    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/CalculatePolicy'

    body = xml_render(template_name='parser/templates/login.xml',
                      context={'phone': phone, 'id': str(random.randint(1, 9999))})

    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text
    response_xml = ElementTree.fromstring(response_xml_as_string)
    session_id = response_xml.find('{http://www.vsk.ru/schema/partners/common}sessionId')
    return session_id.text
