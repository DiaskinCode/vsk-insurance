from rest_framework import serializers


class CalculatorSerializer(serializers.Serializer):
    count_days = serializers.IntegerField(label='Количество дней договора', write_only=True)

    accident_death = serializers.BooleanField(label='Смерть страхуемого', default=True, write_only=True)
    accident_disability = serializers.BooleanField(label='Инвалидность страхуемого', default=True, write_only=True)
    timedisability_accident = serializers.BooleanField(label='Временная нетрудоспособность страхуемого',
                                                       default=True, write_only=True)

    type_of_sport = serializers.CharField(label='Группа спорта', write_only=True)

    is_professional = serializers.BooleanField(label='Профессиональность страхуемого', default=False, write_only=True)
    is_sporttime = serializers.BooleanField(label='НС во время занятия спортом', default=False, write_only=True)

    promo = serializers.CharField(label='Промокод', write_only=True)

    total = serializers.IntegerField(label='Сумма расчета', read_only=True)
    detail = serializers.CharField(label='Подробности ошибки', read_only=True)


class SaveSerializer(CalculatorSerializer):
    birth_insured_person = serializers.DateField(label='День рождения страхуемого', write_only=True)
    fio_insured_person = serializers.CharField(label='ФИО страхуемого', write_only=True)

    birth_policyholder = serializers.DateField(label='День рождения страхователя', write_only=True)
    fio_policyholder = serializers.CharField(label="ФИО страхователя", write_only=True)
    phone_policyholder = serializers.CharField(label='Телефон страхователя', write_only=True)
    email_policyholder = serializers.CharField(label='Email страхователя', write_only=True)

