import random
from typing import Tuple
from xml.etree import ElementTree

import requests

from core.settings import MAIN_URL
from parser.services.helpers import xml_render, get_static_params


def getdraft(
    policyId: str,
    policyNumber: str,
) -> Tuple[bool, str]:
    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/PolicyInPDF'

    body = xml_render(
        template_name='parser/templates/getdraftPolicy.xml',
        context={
            'message_id': str(random.randint(1, 999999)),
            'policy_id': policyId,
            'policy_number': policyNumber
        }
    )
    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text

    if not response_xml_as_string:
        return False, 'blank VSK response'
    response_xml = ElementTree.fromstring(response_xml_as_string)

    if (error := response_xml.find('{http://www.vsk.ru/schema/partners}Response')) is not None:
        return False, error.text








