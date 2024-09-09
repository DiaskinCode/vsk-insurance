import random
from datetime import datetime, timedelta
from typing import Tuple
from xml.etree import ElementTree

import requests

from parser.services.helpers import xml_render, get_static_params, bool_to_str, get_conditions_calculate
from core.settings import MAIN_URL


def calculate(
        count_days: int,
        type_of_sport: str or int,
        is_professional: str or bool,
        is_sporttime: str or bool,
        promo: str,

        accident_death: bool = False,
        accident_disability: bool = False,
        timedisability_accident: bool = False
) -> Tuple[bool, str]:

    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/CalculatePolicy'

    total_condition = ''
    if accident_death:
        total_condition += get_conditions_calculate('accident_death')
    if accident_disability:
        total_condition += get_conditions_calculate('accident_disability')
    if timedisability_accident:
        total_condition += get_conditions_calculate('timedisability_accident')

    date_start = datetime.today()
    date_end = date_start + timedelta(days=count_days-1)

    body = xml_render(
        template_name='parser/templates/calculatePolicy.xml',
        context={
            'message_id': str(random.randint(1, 999999)),
            'date_start': str(date_start.strftime('%Y-%m-%d')),
            'date_end': str(date_end.strftime('%Y-%m-%d')),
            'conditions': total_condition,
            'type_of_sport': str(type_of_sport),
            'is_professional': bool_to_str(is_professional),
            'is_sporttime': bool_to_str(is_sporttime),
            'promo': promo
        }
    )

    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text
    response_xml = ElementTree.fromstring(response_xml_as_string)
    amount = response_xml.find('{http://www.vsk.ru/schema/partners/policy}amount')
    if amount is not None:
        return True, amount.text

    error = response_xml.find('{http://www.vsk.ru/schema/partners/common}error')
    error = error.find('{http://www.vsk.ru/schema/partners/common}errorMessage')
    return False, error.text
