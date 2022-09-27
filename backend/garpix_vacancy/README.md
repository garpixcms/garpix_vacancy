# Garpix Vacancy


## Quickstart

Install with pip:

```bash
pip install garpix_user
```

Add the `garpix_vacancy` to your `INSTALLED_APPS`:

```python
# settings.py

# ...
INSTALLED_APPS = [
    # ...
    'garpix_vacancy',
]
```

and to migration modules:

```python
# settings.py

# ...
MIGRATION_MODULES = {
    'garpix_vacancy': 'app.migrations.garpix_vacancy',
}
```

Add to `urls.py`:

```python

# ...
urlpatterns = [
    # ...
    # garpix_user
    path('', include(('garpix_vacancy.urls', 'garpix_vacancy'), namespace='garpix_vacancy')),

]
```

The module consists of Tag model which is used for Vacancy. If you want to you custom Tag model from your project add it location to `settings.py` file:
``

```python

# settings.py

# ...
GARPIX_VACANCY_TAG_MODEL = 'app.models.Tag'

```


# Changelog

Смотри [CHANGELOG.md](CHANGELOG.md).

# Contributing

Смотри [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)