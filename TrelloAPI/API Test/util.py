import requests
import json

def fetch(action, url, query):
    return json.loads(requests.request(action, url, params = query).text)

class Util:
    def __init__(self, api_key, api_token):
        self.key = str(api_key)
        self.token = str(api_token)

    def fetch(self, action, url, query = { }):
        query.update({
            'key': self.key,
            'token': self.token
        })

        return fetch(action, url, query)

    def set_list_position(self, list_id, pos):
        board_id = self.fetch('GET', f'https://api.trello.com/1/lists/{list_id}')['idBoard']
        lists = self.fetch('GET', f'https://api.trello.com/1/boards/{board_id}/lists')

        for index, list in enumerate(lists):
            list['pos'] = index + 1

        for list in lists.copy():
            if list['id'] == list_id:
                lists.remove(list)
                lists = lists[0: pos - 1] + [list] + lists[pos - 1 :]
                
                break

        for index, list in enumerate(lists):
            list['pos'] = index + 1

        for list in lists:
            self.fetch('PUT', f'')

        print(lists)

        