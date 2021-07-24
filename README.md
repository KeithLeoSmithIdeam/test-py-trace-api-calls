# test trace api calls



## Python VENV
Create
```
python3 -m venv /home/keith/test-py-api/venv
```
Activate venv
```
source /home/keith/test-py-api/venv/bin/activate
```
freeze
```
pip freeze -r requirements.txt 
or
pip freeze > requirements.txt 
```

## Test
```
curl http://127.0.0.1:5000/test

curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/test
```