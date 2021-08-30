import configparser
import json

import requests

global token
global instance_
global server_

module = GetParams('module')

if module == 'Login':
    ruta_ = GetParams("ruta_")

    config = configparser.ConfigParser()
    config.read(ruta_)
    email_ = config.get('USER', 'user')
    pass_ = config.get('USER', 'password')
    instance_ = config.get('USER', 'key')
    try:
        apikey_ = config.get('USER', 'apiKey')
    except:
        apikey_ = ""
    server_ = config.get('NOC', 'server')

    try:
        if apikey_ != "":
            token = apikey_
        else: 
            data = {'email': email_, 'password': pass_}
            res = requests.post(server_ + '/api/auth/login', data,
                                headers={'content-type': 'application/x-www-form-urlencoded'})
    
            if res.status_code == 200:
                res = res.json()
                if res['success']:
                    token = res['data']
                else:
                    raise Exception(res['message'])
            else:
                raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SendLog':
    token_ = GetParams('token')
    log_ = GetParams('log_')

    if not token_ or not log_:
        raise Exception('Missing Data')

    try:
        data = {'processToken': token_, 'key': instance_, 'log': log_}
        res = requests.post(server_ + '/api/rocketbot/log', data,
                            headers={'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token})
        tmp = res.json()
        if res.status_code != 200:
            raise Exception(tmp['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'SendAlert':
    token_ = GetParams('token')
    log_ = GetParams('log_')

    if not token_ or not log_:
        raise Exception('Missing Data')

    try:
        data = {'processToken': token_, 'message': log_}
        res = requests.post(server_ + '/api/rocketbot/alert', data,
                            headers={'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token})
        tmp = res.json()
        if res.status_code != 200:
            raise Exception(tmp['message'])
    except Exception as e:
        PrintException()
        raise e
