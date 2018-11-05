import requests
from urllib.parse import urlparse, urljoin


POSTBIN_URL = 'http://postb.in'


class PostBin(object):

    def __init__(self):
        self.api = urljoin(POSTBIN_URL, '/api/bin')
        self.bin_id = self.get_id()
        self.bins = Bin(self.bin_id)
        self.request = Request(self.bin_id)

    def get_id(self):
        r = requests.post(self.api)
        resp = r.json()
        if resp.get('binId'):
            return resp.get('binId')
        return


class Bin(object):
    def __init__(self, bin_id: str=None):
        self.bin_id = bin_id
        self.url = urljoin(POSTBIN_URL, f'/api/bin/{bin_id}')

    def get(self) -> str:
        return requests.get(self.url).json()

    def delete(self) -> str:
        return requests.delete(self.url).json()

    def set(self, payload: str=None) -> str:
        return requests.post(urljoin(POSTBIN_URL, self.bin_id), data=payload).content




class Request(object):
    def __init__(self, bin_id=None):
        self.url = urljoin(POSTBIN_URL, f'/api/bin/{bin_id}/req/')

    def get(self, req_id: str=None) -> str:
        if not req_id:
            return
        print(f"RequestID: {req_id}")
        print(f"UR: {self.url}{req_id}")
        return requests.get(urljoin(self.url, req_id)).json()

    def shift(self):
        return requests.get(urljoin(self.url, 'shift')).json()


if __name__ == '__main__':
    pb = PostBin()
    print(pb.bins.set('{"test": "testing"}'))
    print(pb.bins.get())
