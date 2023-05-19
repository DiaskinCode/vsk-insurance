import random
import xml.etree.ElementTree as ET

import requests
from core.settings import MAIN_URL

from parser.services.helpers import xml_render, get_static_params


def buy_service(context):
    context['id'] = str(random.randint(1, 9999))

    body = xml_render(
        template_name='parser/templates/buyPolicy.xml',
        context=context)

    response = requests.post(
        url=f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/BuyPolicy',
        data=body,
        **get_static_params())

    response_xml_as_string = response.text
    print(response_xml_as_string)
    responseXml = ET.fromstring(response_xml_as_string)
    url = responseXml.find('{http://www.vsk.ru/schema/partners/policy}formUrl')
    return url.text
