from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'garpix_vacancy',
]

GARPIX_VACANCY_MIXIN = 'garpix_page.models.BasePage'
GARPIX_CONTACT_MIXIN = 'garpix_page.models.BasePage'
