This is a simple example on how to reproduce a bug with psycopg3 and sentry_sdk.

Steps to reproduce:
1. Install requirements
```
pip install -r requirements.txt
```
2. Startup postgres
```
docker-compose up
```
3. Run test without Sentry (test will succeed)
```
./manage.py test
```
4. Run test with Sentry (test will fail)
```
export USE_SENTRY=True && ./manage.py test
```