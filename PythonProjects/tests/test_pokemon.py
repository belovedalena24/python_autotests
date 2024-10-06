import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '00f70d4fb7c3c8235c21b22ffc3f2db5' 
HEADER ={'Content-Type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 4047

def test_status_code():
    response = requests.get(url=f'{URL}/trainers',params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers',params = {'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Белка'

#Пример из обучающего видео
'''@pytest.mark.parametrize('key,value',[('name','Бульбазавр'),('trainer_id','TRAINER_ID'),('id','79303')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url=f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value '''