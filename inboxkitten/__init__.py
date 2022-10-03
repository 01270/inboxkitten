import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

class InboxKitten:
    keys, storages = list(), list()
    senders, subjects = list(), list()
    def __init__(self, email): self.email = email

    def setup(self):
        if '@' in self.email: self.email = self.email.split('@')[0]
        response = requests.get('https://inboxkitten.com/api/v1/mail/list',
                    params={'recipient': self.email}, headers=headers)

        for mail in response.json():
            data, info = mail['storage'], mail['message']['headers']
            InboxKitten.keys.append(str(data['key'])); InboxKitten.storages.append(str(data['region']))
            InboxKitten.senders.append(str(info['from'])); InboxKitten.subjects.append(str(info['subject']))
        return True

    def clear(self):
        InboxKitten.keys.clear();InboxKitten.storages.clear()
        InboxKitten.senders.clear();InboxKitten.subjects.clear()


    class view:
        def __init__(self, index): self.index = index

        @property
        def text(self):
                response = requests.get(f'https://inboxkitten.com/api/v1/mail/getHtml?mailKey=storage-{InboxKitten.storages[self.index]}-{InboxKitten.keys[self.index]}', headers=headers)
                return response.text

        def save_html(self, filename):
            html = self.text
            if html:
                with open(filename, 'w', encoding='utf-8', errors='ignore') as html_file: html_file.write(html)
                return True
            else: raise(TypeError, 'Error while getting the html data')
