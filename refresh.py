import datetime, time
from pprint import pprint

import requests


def poll_job(s, redash_url, job, poll_timeout):
    try:
        stime = datetime.datetime.now()
        while job['status'] not in (3, 4):
            response = s.get('{}/api/jobs/{}'.format(redash_url, job['id']), timeout=10)
            pprint(response.json())
            job = response.json()['job']
            time.sleep(1)
            difftime = datetime.datetime.now() - stime
            if difftime.total_seconds() > poll_timeout:
                raise Exception('Polling timeout.')
    except Exception as e:
        print(e)
        return None

    if job['status'] == 3:
        return job['query_result_id']

    return None


def get_fresh_query_result(redash_url, query_id, api_key, timeout):
    try:
        s = requests.Session()
        s.headers.update({'Authorization': 'Key {}'.format(api_key)})

        response = s.post('{}/api/queries/{}/refresh'.format(redash_url, query_id), timeout=10)
        pprint(response.json())

        if response.status_code != 200:
            raise Exception('Refresh failed.')

        result_id = poll_job(s, redash_url, response.json()['job'], timeout)

        if result_id:
            response = s.get('{}/api/queries/{}/results/{}.json'.format(redash_url, query_id, result_id), timeout=10001)
            if response.status_code != 200:
                raise Exception('Failed getting results.')
        else:
            raise Exception('Query execution failed.')

    except Exception as e:
        print(e)
        return None
    # とりあえずdebug中はだ
    print(response.json()['query_result']['data'])
    return response.json()['query_result']['data']['rows']


def write_result(status):
    # todo 処理を記載する

if __name__ == '__main__':
    # todo 引数化
    query_id = 3486
    # Need to use a *user API ey* here (and not a query API key).
    api_key = 'e8DVvqXSGwl7gWIGAmYarn9ELLtWPqwix8jzZLkk'
    poll_timeout = 720  # 20分 = 720秒
    result = get_fresh_query_result('https://redash-i3.dmm.com', query_id, api_key, poll_timeout)
    if result and (result[0]['result1'] == 2):
        # OK書き込み(関数にする)
        pprint(result[0])
    else:
        # NG書き込み(関数にする
        print('はずれ')
    # todo: クエリで0かえるようにして、0ちぇっくかな（ちないみに、prestoにクエリはいっている）
