### Подготовка к запуску

- Надо создать проект в https://console.cloud.google.com/
  - затем скачать *json_file* (креды service account)
  - также добавить *email* (service_account) в google sheet для возможности редактирования
- Установить ликвидные пути к файлам в **.env** (см *.env-sample*)

### Запуск скрипта

```
python -m venv pdf_reader_env
pdf_reader_env\Scripts\activate
pip install -r requirements.txt
python.exe .\google_sheets_client.py
```
