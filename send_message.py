import requests

message = input('Enter a Message: ')
number = input('Enter the phone number: ')


magic = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data = magic)
if r.json()['success']:
        print('Yeah!!! Your message has been sent')
else:
    print('Ugh! Sorry message could not be sent')
