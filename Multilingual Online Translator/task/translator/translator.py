import requests
from bs4 import BeautifulSoup
import sys

user_agent = 'Mozilla/5.0'
url = ''
languages = ["Arabic", "German", 'English', "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
languag = ["arabic", "german", 'english', "spanish", "french", "hebrew", "japanese", "dutch", "polish", "portuguese", "romanian", "russian", "turkish"]
lan = {1: "arabic", 2: "german", 3: "english", 4: "spanish", 5: "french", 6: "hebrew", 7: "japanese", 8: "dutch", 9: "polish", 10: "portuguese", 11: "romanian", 12: "russian", 13: "turkish"}

my_lang = sys.argv[1]
perev_lang = sys.argv[2]
word = sys.argv[3].strip()
perev = []
primer = []

if perev_lang == 'all':
    languages.remove(my_lang.capitalize())
    for i in languages:
        url = f'https://context.reverso.net/translation/{my_lang}-{i.lower()}/{word}'
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == 404:
            print(f'Sorry, unable to find {word}')
            exit()
        elif 200 > response.status_code > 404:
            print('Something wrong with your internet connection')
            exit()
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            perev = [i.text.strip() for i in soup.find_all('a', class_='translation')]
            primer = [element.text.strip() for element in soup.find('section', id="examples-content").find_all('span', class_="text")]
            print(f'{i} Translations')
            print(perev[1])
            print()
            print(f'{i} Examples')
            print(*primer[:2], sep='\n')
            print()
            with open(f'{word}.txt', 'a', encoding='utf-8') as f:
                print(f'{i} Translations', file=f)
                print(perev[1] + "\n", file=f)
                print(f'{i} Examples', file=f)
                print(*primer[:2], sep='\n', file=f)
                print(file=f)
elif perev_lang not in languag:
    print(f"Sorry, the program doesn't support {perev_lang}")
    exit()
else:
    url = f'https://context.reverso.net/translation/{my_lang}-{perev_lang}/{word}'
    response = requests.get(url, headers={'User-Agent': user_agent})
    print(response.status_code)
    if response.status_code == 404:
        print(f'Sorry, unable to find {word}')
        exit()
    elif 200 > response.status_code > 404:
        print('Something wrong with your internet connection')
        exit()
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        perev = [i.text.strip() for i in soup.find_all('a', class_='translation')]
        primer = [element.text.strip() for element in soup.find('section', id="examples-content").find_all('span', class_="text")]
        print(f'{perev_lang} Translations')
        print(perev[1])
        print()
        print(f'{perev_lang} Examples')
        print(*primer[:2], sep='\n')
        print()
        with open(f'{word}.txt', 'w+', encoding='utf-8') as f:
            print(f'{perev_lang} Translations', file=f)
            print(perev[1] + "\n", file=f)
            print(f'{perev_lang} Examples', file=f)
            print(*primer[:2], sep='\n', file=f)
            print(file=f)


