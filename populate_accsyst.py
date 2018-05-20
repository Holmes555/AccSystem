import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'AccSystem.settings')

import django
django.setup()

from accsyst.models import *


def populate():
    """Generate some Jobs and UserProfiles."""

    users = {
        'ivan2': {
            'username': 'ivan2',
            'e-mail': 'my@gmail.com',
            'password': 'RopTop63'
        },
        'zhenya': {
            'username': 'Z',
            'e-mail': 'z@gmail.com',
            'password': '123polkA'
        },
        'kostya': {
            'username': 'Kostya',
            'e-mail': 'kos_tya',
            'password': 'frog903J'
        },
        'snow': {
            'username': 'Snow',
            'e-mail': 'snow@l.ru',
            'password': 'snowBoard3'
        },
        'no_name': {
            'username': '',
            'e-mail': 'no@gmail.com',
            'password': 'Noname4'
        },
        'no_email': {
            'username': 'hi',
            'e-mail': '',
            'password': 'Noemail123'
        },
        'no_password': {
            'username': 'hello',
            'e-mail': 'nopass@yandex.by',
            'password': ''
        }
    }

    user_profiles = [
        {'user': users['ivan2'],
         'picture': '',
         'website': ''},
        {'user': users['kostya'],
         'picture': 'profile_images/Снимок_экрана.png',
         'website': 'http://www.kos.by'},
        {'user': users['zhenya'],
         'picture': '',
         'website': 'http://www.z.by'},
        {'user': users['snow'],
         'picture': 'profile_images/Снимок_экрана.png',
         'website': 'http://www.snow.com'},
        {'user': users['no_name'],
         'picture': 'profile_images/Снимок_экрана.png',
         'website': 'www..by'},
        {'user': users['no_email'],
         'picture': 'error',
         'website': ''},
        {'user': users['no_password'],
         'picture': '',
         'website': 'error'},
    ]

    jobs = [
        {'id': 1,
         'name': 'My job',
         'sra_id': 'SRR2018',
         'data_file': '',
         'result_file': '',
         'user': ''},
        {'id': 2,
         'name': 'S',
         'sra_id': '',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': '',
         'user': ''},
        {'id': 3,
         'name': 'S',
         'sra_id': '',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': '',
         'user': users['ivan2']},
        {'id': 4,
         'name': '',
         'sra_id': 'SRR10000',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': '',
         'user': users['zhenya']},
        {'id': 5,
         'name': '',
         'sra_id': '',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': '',
         'user': users['no_password']},
        {'id': 6,
         'name': '',
         'sra_id': 'SRR300',
         'data_file': '',
         'result_file': '',
         'user': users['kostya']},
        {'id': 7,
         'name': '',
         'sra_id': '',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': 'result_data/job_report12.csv',
         'user': users['snow']},
        {'id': 8,
         'name': 'S',
         'sra_id': '',
         'data_file': 'data_vcf/SRR5152945_filter.recode.vcf',
         'result_file': 'result_data/job_report11.csv',
         'user': users['no_name']},

    ]

    for user in users.values():
        add_user(user['username'], user['e-mail'], user['password'])

    for up in user_profiles:
        add_userprofile(up['user'], up['picture'], up['website'])

    for job in jobs:
        add_job(job['id'], job['name'], job['sra_id'],
                job['data_file'], job['result_file'], job['user'])

    print('Jobs:\n')
    for j in Job.objects.all():
        print(str(j))

    print('\nUser_profiles:\n')
    for u in User.objects.all():
        print(str(u))


def add_user(username, email, password):
    u = User.objects.get_or_create(username=username)[0]
    u.email = email
    u.set_password(password)
    u.save()


def add_userprofile(user, picture, website):
    u = User.objects.get(username=user['username'])
    up = UserProfile.objects.get_or_create(user=u)[0]
    up.picture = picture
    up.website = website
    up.save()


def add_job(id, name, sra_id, data_file, result_file, user):
    j = Job.objects.get_or_create(id=id, name=name, sra_id=sra_id,
                                  data_file=data_file, result_file=result_file)[0]
    u = None
    try:
        u = User.objects.get(username=user['username'])
    except TypeError:
        pass
    j.user = u
    j.save()


if __name__ == '__main__':
    print('Starting Rast population script...')
    populate()
