import requests


def get_max_int():
    name = ['Thanos', "Hulk", 'Captain America']
    heroes_int = {}
    for i in name:
        r = 'https://superheroapi.com/api/2619421814940190/search/' + i
        r = requests.get(r).json()
        heroes_int[i] = int(r['results'][0]['powerstats']['intelligence'])

    max_int = max(heroes_int.items())
    return max_int


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def get_link(self, path_to_file):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        res = requests.get(url=url, headers=headers, params=params)
        return res.json()

    def upload(self, path_to_file, file):
        href = self.get_link(path_to_file=path_to_file).get('href', '')
        res = requests.put(href, data=open(file, 'rb'))
        if res.status_code == 201:
            print('Файл успешно загружен')


if __name__ == '__main__':
    print(get_max_int())

    path_to_file = r''
    file = ''
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file, file)
