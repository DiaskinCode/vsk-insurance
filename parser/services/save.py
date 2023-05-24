import random
from datetime import datetime, timedelta
from typing import Tuple
from xml.etree import ElementTree

import requests

from core.settings import MAIN_URL
from parser.services import login
from parser.services.helpers import xml_render, get_static_params, bool_to_str, get_conditions_save, find_in_xml


def save(
        count_days: int,
        type_of_sport: str or int,
        is_professional: str or bool,
        is_sporttime: str or bool,

        birth_insured_person: str or datetime,
        fio_insured_person: str,

        birth_policyholder: str or datetime,
        fio_policyholder: str,
        phone_policyholder: str,
        email_policyholder: str,

        promo: str,

        accident_death: bool = False,
        accident_disability: bool = False,
        timedisability_accident: bool = False
) -> Tuple[bool, dict]:
    total_data = {
        'error': None,
        'policyNumber': None,
        'policyId': None,
        'sessionId': None,
        'bpId': None,
        'amount': None
    }

    success, sessionId = login('7777777777')
    if not success:
        return False, {'error': sessionId if sessionId else 'Ошибка логина'}

    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/SavePolicy'

    date_create = datetime.today()
    date_start = date_create + timedelta(days=1)
    date_end = date_start + timedelta(days=count_days-1)

    date_create = date_create.strftime('%Y-%m-%d')
    date_start = date_start.strftime('%Y-%m-%d')
    date_end = date_end.strftime('%Y-%m-%d')

    total_condition = ''
    if accident_death:
        total_condition += get_conditions_save('accident_death', date_start=date_start, date_end=date_end)
    if accident_disability:
        total_condition += get_conditions_save('accident_disability', date_start=date_start, date_end=date_end)
    if timedisability_accident:
        total_condition += get_conditions_save('timedisability_accident', date_start=date_start, date_end=date_end)

    body = xml_render(
        template_name='parser/templates/savePolicy.xml',
        context={
            'message_id': str(random.randint(1, 999999)),
            'session_id': sessionId,
            'date_create': date_create,
            'date_start': date_start,
            'date_end': date_end,
            'birth_insured_person': birth_insured_person.strftime('%Y-%m-%d'),
            'fio_insured_person': fio_insured_person,
            'conditions': total_condition,
            'phone_policyholder': phone_policyholder,
            'email_policyholder': email_policyholder,
            'birth_policyholder': birth_policyholder.strftime('%Y-%m-%d'),
            'fio_policyholder': fio_policyholder,
            'type_of_sport': str(type_of_sport),
            'is_professional': bool_to_str(is_professional),
            'is_sporttime': bool_to_str(is_sporttime),
            'promo': promo
        }
    )

    response = requests.post(full_url, data=body, **get_static_params())
    response_xml_as_string = response.text
    if not response_xml_as_string:
        return False, {'error': 'blank VSK response'}
    response_xml = ElementTree.fromstring(response_xml_as_string)
    data_dict = {
        'amount': 'http://www.vsk.ru/schema/partners/policy',
        'bpId': 'http://www.vsk.ru/schema/partners/common',
        'sessionId': 'http://www.vsk.ru/schema/partners/common',
        'policyId': 'http://www.vsk.ru/schema/partners/model',
        'policyNumber': 'http://www.vsk.ru/schema/partners/model'
    }
    for key, value in data_dict.items():
        total_data[key] = find_in_xml(response_xml, value, key)

    addict_data = {
        'policyId': 'http://www.vsk.ru/schema/partners/model',
        'policyNumber': 'http://www.vsk.ru/schema/partners/model'
    }
    temp_xml = response_xml.find('{http://www.vsk.ru/schema/partners/policy}policy')
    for key, value in addict_data.items():
        total_data[key] = find_in_xml(temp_xml, value, key)


    if all([value for key, value in total_data.items() if key != 'error']):
        return True, total_data

    error = response_xml.find('{http://www.vsk.ru/schema/partners/common}error')
    error = error.find('{http://www.vsk.ru/schema/partners/common}errorMessage')
    return False, {'error': error.text}

