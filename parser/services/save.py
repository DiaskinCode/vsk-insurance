import random
from datetime import datetime, timedelta
from typing import Tuple, Union, Dict
from xml.etree import ElementTree

import requests

from core.settings import MAIN_URL
from parser.services import login
from parser.services.helpers import xml_render, get_static_params, bool_to_str, get_conditions_save


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
) -> Union[Tuple[bool, str], Tuple[bool, Dict[str, str]]]:
    success, session_id = login('7777777777')
    if not success:
        return False, session_id if session_id else 'Ошибка логина'

    full_url = f'{MAIN_URL}/cxf/rest/partners/api/Sync/Policy/SavePolicy'

    date_create = datetime.today()
    date_start = date_create + timedelta(days=1)
    date_end = date_start + timedelta(days=count_days - 1)

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
            'session_id': session_id,
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
        return False, 'blank VSK response'
    response_xml = ElementTree.fromstring(response_xml_as_string)

    error = response_xml.find('{http://www.vsk.ru/schema/partners/common}error')
    if error is not None:
        return False, error.find('{http://www.vsk.ru/schema/partners/common}errorMessage').text

    bpId = response_xml.find('{http://www.vsk.ru/schema/partners/common}bpId').text
    policyId = response_xml.find('{http://www.vsk.ru/schema/partners/policy}policy').find(
        '{http://www.vsk.ru/schema/partners/model}policyId').text
    amount = response_xml.find('{http://www.vsk.ru/schema/partners/policy}amount').text
    policyNumber = response_xml.find('{http://www.vsk.ru/schema/partners/policy}policy').find(
        '{http://www.vsk.ru/schema/partners/model}policyNumber').text

    return True, {'bpId': bpId,
                  'policyId': policyId,
                  'amount': amount,
                  'policyNumber': policyNumber,
                  'session_id': session_id}
