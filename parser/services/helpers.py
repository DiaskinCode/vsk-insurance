from lxml.etree import Element


def xml_render(template_name: str, context: dict) -> bytes:
    with open(template_name, 'r') as f:
        xml = f.read()

    for key in context:
        xml = xml.replace(f'({key})', context[key])
    return xml.encode('utf-8')


def get_static_params() -> dict:
    return {'headers': {'Content-Type': 'application/xml',
               'ClientCertSubjectCN': 'marketplace',
               'ClientCertSubject': 'MARKETPLACE'},
            'cert': (
                'parser/cert/buisness_protection.pem',
                'parser/cert/buisness_protection.key')}


def bool_to_str(value: str or bool) -> str:
    return str(value).lower()


def get_conditions_calculate(risk_code: str) -> str:
    return f'''
    <model:conditions>
                <model:insuranceSum>20000000</model:insuranceSum>
                <model:conditionProductRisks>
                    <model:risk>
                        <model:riskCode>{risk_code.upper()}</model:riskCode>
                    </model:risk>
                </model:conditionProductRisks>
            </model:conditions>'''


def get_conditions_save(risk_code: str, date_start: str, date_end: str) -> str:
    return f'''<model:conditions>
        <model:insuranceSum>20000000</model:insuranceSum>
        <model:beginDate>{date_start}+03:00</model:beginDate>
        <model:endDate>{date_end}+03:00</model:endDate>
        <model:conditionProductRisks>
            <model:risk>
                <model:riskCode>{risk_code.upper()}</model:riskCode>
            </model:risk>
        </model:conditionProductRisks>
    </model:conditions>'''


def find_in_xml(response_xml: Element, type_xml: str, arg: str) -> str or None:
    search_result = response_xml.find('{%s}%s' % (type_xml, arg))
    if search_result is not None:
        return search_result.text
