import random
from typing import Tuple
from xml.etree import ElementTree

import requests

from core.settings import MAIN_URL
from parser.services.helpers import xml_render, get_static_params


def buy(
        bpId: str,
        sessionId: str,
        policyId: str,
        policyNumber: str,
        amount: str
) -> Tuple[bool, str]:
    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/BuyPolicy'

    body = xml_render(
        template_name='parser/templates/buyPolicy.xml',
        context={
            'message_id': str(random.randint(1, 999999)),
            'bp_id': bpId,
            'session_id': sessionId,
            'policy_id': policyId,
            'policy_number': policyNumber,
            'amount': amount
        }
    )

    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text
    if not response_xml_as_string:
        return False, 'blank VSK response'
    response_xml = ElementTree.fromstring(response_xml_as_string)

    if (url := response_xml.find('{http://www.vsk.ru/schema/partners/policy}formUrl')) is not None:
        return True, url.text
    return False, 'unexcepted error'

