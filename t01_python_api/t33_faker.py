# coding=utf-8
from faker import Faker
import datetime

fk = Faker(['zh_CN'])

for i in range(10):
    result = fk.name()
    result = fk.company()
    result = fk.date()
    st = datetime.datetime.strptime('1920-01-01', '%Y-%m-%d')
    se = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d')
    result = fk.date_between(st, se)
    result = fk.date_this_month()
    result = fk.date_this_year()
    result = fk.date_time_between(start_date=st, end_date=se)
    result = fk.day_of_week()
    result = fk.month_name()
    result = fk.ascii_email()
    result = fk.ascii_free_email()
    result = fk.domain_name()
    result = fk.ipv4()
    result = fk.ipv4_private()
    result = fk.ipv4_public()
    result = fk.mac_address()
    result = fk.ipv6()
    result = fk.url()
    result = fk.job()
    result = fk.paragraph()
    result = fk.text()
    result = fk.ssn()

