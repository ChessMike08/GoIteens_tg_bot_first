import requests
import json
from datetime import datetime

def verify_date(date):
    try:
        act_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        eror = "Неправильний формат дати"
    else:
        if datetime.strptime("2022-02-24", "%Y-%m-%d") <= act_date <= datetime.now():
            return True
    return False

def get_stats(date):
    url = f"https://russianwarship.rip/api/v2/statistics/{date}"
    response = requests.get(url)
    response_str = response.text
    response_json = json.loads(response_str)
    if response_json['message'] == 'Statistics record not found.' or response_json['message'] == "The given data was invalid.":
        message = 'Statistics record not found.'
        return message
    message = f"""
    (мова: 🇺🇦)|(language: 🇬🇧)
    *Основні дані про війну на цей день*|*Basic data about the war on this day*
    Війна|War "{response_json['data']['war_status']['alias']}"
    {response_json['data']['day']} день війни|day of the war
    *Вид зброї: всього кол-во на цей день включно(+кол-во скільки прибавилось за цей день)*
    *Weapons: total number of weapons on this day inclusive (+ the number of weapons added during this day)*
    Особового складу|Personnel: {response_json['data']['stats']['personnel_units']}(+{response_json['data']['increase']['personnel_units']})
    Танків|Tanks: {response_json['data']['stats']['tanks']}(+{response_json['data']['increase']['tanks']})
    БМП|AFV: {response_json['data']['stats']['armoured_fighting_vehicles']}(+{response_json['data']['increase']['armoured_fighting_vehicles']})
    Артилерійських систем|Artillery systems: {response_json['data']['stats']['artillery_systems']}(+{response_json['data']['increase']['artillery_systems']})
    РСЗВ|MLRS: {response_json['data']['stats']['mlrs']}(+{response_json['data']['increase']['mlrs']})
    Засобів ППО|Air defense systems: {response_json['data']['stats']['aa_warfare_systems']}(+{response_json['data']['increase']['aa_warfare_systems']})
    Літаки|Planes: {response_json['data']['stats']['planes']}(+{response_json['data']['increase']['planes']})
    Гелікоптерів|Helicopters: {response_json['data']['stats']['helicopters']}(+{response_json['data']['increase']['helicopters']})
    Автотехніки та автоцистерн|Vehicles and fuel tanks: {response_json['data']['stats']['vehicles_fuel_tanks']}(+{response_json['data']['increase']['vehicles_fuel_tanks']})
    Кораблів/катерів|Ships/boats: {response_json['data']['stats']['warships_cutters']}(+{response_json['data']['increase']['warships_cutters']})
    БПЛА|UAVs: {response_json['data']['stats']['uav_systems']}(+{response_json['data']['increase']['uav_systems']})
    Спеціальної техніки|Special equipment: {response_json['data']['stats']['special_military_equip']}(+{response_json['data']['increase']['special_military_equip']})
    Установок ОТРК/ТРК|ATGM/SRBM systems: {response_json['data']['stats']['atgm_srbm_systems']}(+{response_json['data']['increase']['atgm_srbm_systems']})
    Крилатих ракет|Cruise missiles: {response_json['data']['stats']['cruise_missiles']}(+{response_json['data']['increase']['cruise_missiles']})
    """
    return message