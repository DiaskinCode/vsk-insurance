import base64
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
            'id': str(random.randint(1, 999999)),
            'policyId': policyId,
            'policyNumber': policyNumber
        }
    )
    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text

    if not response_xml_as_string:
        return False, 'blank VSK response'
    response_xml = ElementTree.fromstring(response_xml_as_string)
    if (policy := response_xml.find('{http://www.vsk.ru/schema/partners/policy}policyInPDF')) is not None:
        return True, policy.text
