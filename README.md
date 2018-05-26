# Django Sample API

練習のためのAPI

## Documents

Domain: `example.com`

### `/api/v1/`

You can upload image and get it later.

#### `/api/v1/images`

| method | header | param | response |
| :------ | :------ | :----- | :-------- |
| GET    | `application/json`| - | `HTTP_200_OK` |
| POST   | `multipart/form-data` | `file`: Upload image<br>`name`: File name | `HTTP_201_CREATED`<br>see `/api/v1/images/<pk:int>` |

```json
{
  "count": 2,
  "next": "url to next page or null",
  "previous": "url to next page or null",
  "results": [
    {
        "pk": 2,
        "name": "table",
        "file": "http://example.com/media/images/fd883ff293434e7db82380bc6906a212.JPG",
        "created_at": "2018-05-26T21:21:17.733848+09:00"
    },
    {
        "pk": 1,
        "name": "test",
        "file": "http://example.com/media/images/1c52d898d1db4db689fb38a406bd1cd1.jpeg",
        "created_at": "2018-05-26T21:11:34.686626+09:00"
    }
  ]
}
```

#### `/api/v1/images/<pk:int>/`

Specify image object by primary key (pk).

| method | header | param | response |
| :----- | :----- | :---- | :------- |
| GET    | `application/json` | - | `HTTP_200_OK` |
| PUT    | `multipart/form-data` | `file`: Upload image<br>`name`: File name | `HTTP_200_OK` |
| PATCH  | `multipart/form-data` | specify field to update | `HTTP_200_OK` |
| DELETE | - | - | `HTTP_204_NO_CONTENT` |

```json
{
    "pk": 1,
    "name": "test",
    "file": "http://example.com/media/images/1c52d898d1db4db689fb38a406bd1cd1.jpeg",
    "created_at": "2018-05-26T21:11:34.686626+09:00"
}
```

## Environment

- Python 3.6 or later
- pipenv
- Django 2.0.5
- djangorestframework 3.8.5

### Setup environment

Install pipenv

```bash
$ python -V
Python 3.6.0
$ pip install --upgrade pip
$ pip install pipenv
```

Clone this repository

```bash
$ git clone https://github.com/StudioAquatan/django_sample_api
$ cd django_sample_api
```

Setup virtualenv

```bash
$ pipenv install
```

Setup database

```bash
$ cd src
$ pipenv run python manage.py migrate
```

Create superuser

```bash
$ pipenv run python manage.py createsuperuser
```

## Author

StudioAquatan

- pudding

## License

MIT
