# Fake Real Estate API
This is a DRF API that serves faked real estate data.

There is an existing admin user for the Django admin page that is created via a migration
```
username: admin
password: qwerty123
```
## Setup
- Install dependencies:
```shell
poetry install
```
- Start poetry shell
```shell
poetry shell
```
- Run migrations
```shell
make m
```
- Start server
```shell
make run
```
