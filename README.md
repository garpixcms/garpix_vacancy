# Garpix Vacancy


## Быстрый старт

Установка:

```bash
pip install garpix_vacancy
```

Добавьте `garpix_vacancy` в `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'garpix_vacancy',
]
```


Также, в settings.py необходимо добавить миксины:

```bash
GARPIX_VACANCY_MIXIN = 'garpix_page.models.BasePage'
GARPIX_CONTACT_MIXIN = 'garpix_page.models.BasePage'
```



# Changelog

Смотри [CHANGELOG.md](CHANGELOG.md).

# Contributing

Смотри [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)