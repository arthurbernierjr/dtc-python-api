# Todos API (Python)

A Deeper Than Code backend example by Arthur Bernier Jr: Python 3.13, Django 6.1, Django REST framework, django-cors-headers, Postgres (via `dj-database-url` and `psycopg`), served by gunicorn on Railway.

Live: https://api-production-02380.up.railway.app

## The contract

Every Deeper Than Code backend serves exactly this. No trailing slashes.

| Request | Response |
|---|---|
| `GET /health` | 200 `{"ok":true}` |
| `GET /todos` | 200 `[{id,subject,details}]` ordered by id ascending |
| `GET /todos/:id` | 200 object, or 404 `{"error":"not found"}` |
| `POST /todos` body `{subject,details}` | 201 object |
| `PUT /todos/:id` body `{subject,details}` | 200 object, or 404 `{"error":"not found"}` |
| `DELETE /todos/:id` | 204 with empty body, or 404 `{"error":"not found"}` |
| blank, whitespace-only, or missing subject or details | 400 `{"error":"<message>"}` |
| malformed JSON body | 400 `{"error":"<message>"}` |

Objects contain exactly three keys: `id` (integer), `subject` (string), `details` (string). CORS is open to any origin for GET, POST, PUT, DELETE and OPTIONS with the `Content-Type` header. `GET /` is a small HTML page that points at `/todos`.

## Check it

```
node check.mjs https://api-production-02380.up.railway.app
```

`check.mjs` is the shared contract test (Node 18 or later, no packages). All 16 checks must print `PASS`.

## Environment variables

| Name | Purpose |
|---|---|
| `DATABASE_URL` | Postgres connection string (falls back to a local SQLite file when unset) |
| `PORT` | Port gunicorn listens on (Railway sets it; falls back to 8080) |
| `SECRET_KEY` | Django secret key |
| `ALLOWED_HOSTS` | Comma-separated hostnames Django will serve (the Railway domain) |
| `DEBUG` | `true` or `false`; keep it `false` in production |
| `CSRF_TRUSTED_ORIGINS` | Optional comma-separated origins for the Django admin |

Do not commit `SECRET_KEY` or `DATABASE_URL`.

## Layout

- `todoproject/settings.py`, `todoproject/urls.py`: project settings and routes (`DefaultRouter(trailing_slash=False)` plus `/health` and `/`).
- `todos/models.py`: the `Todo` model (`todos_todo` table).
- `todos/serializers.py`: the three-field serializer with blank and whitespace rejection.
- `todos/views.py`: `TodoViewSet`, `health`, `home`.
- `todos/exceptions.py`: the DRF exception handler that shapes every error as `{"error": "..."}`.
- `Procfile`: collectstatic, migrate, then gunicorn.
