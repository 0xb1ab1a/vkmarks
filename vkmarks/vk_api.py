from hashlib import md5
from django.conf import settings
from requests import request, ConnectionError


def call_api(method, data):
    """
    Calls VK.com OpenAPI method, check:
        https://vk.com/apiclub
        http://goo.gl/yLcaa
    """
    # We need to perform server-side call if no access_token
    if not 'access_token' in data:
        if not 'v' in data:
            data['v'] = '3.0'

        key, secret = get_key_and_secret()
        if not 'api_id' in data:
            data['api_id'] = key

        data['method'] = method
        data['format'] = 'json'
        url = 'http://api.vk.com/api.php'
        param_list = sorted(list(item + '=' + data[item] for item in data))
        data['sig'] = md5(
            (''.join(param_list) + secret).encode('utf-8')
        ).hexdigest()
    else:
        url = 'https://api.vk.com/method/' + method

    # try:
    return get_json_from(url, params=data)
    # except (TypeError, KeyError, IOError, ValueError, IndexError):
    # return None


def get_json_from(url, **kwargs):
    return get_request(url, **kwargs).json()


def get_request(url, method='GET', **kwargs):
    try:
        response = request(method, url, **kwargs)
    except ConnectionError as err:
        raise err
    response.raise_for_status()
    return response


def get_key_and_secret():
    return settings.SOCIAL_AUTH_VK_OAUTH2_KEY, settings.SOCIAL_AUTH_VK_OAUTH2_SECRET