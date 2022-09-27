from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'garpix_vacancy',
]

GARPIX_VACANCY_TAG_MODEL = 'garpix_vacancy.models.Tag'

MIGRATION_MODULES.update({  # noqa
    'garpix_vacancy': 'app.migrations.garpix_vacancy'
})
