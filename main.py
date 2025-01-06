import asyncio, time
import requests as r
import os
import websocket
import colorama
from colorama import Fore, init
import requests
import random
import time
import os

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')

token = input("Enter Token Here: ")
channel_id = input("Enter Channel ID Here: ")

clear()

messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'no', 'ikr', 'you’re the human version of a participation trophy', 'I’ve seen better decisions in a toddler’s drawing', 'you bring as much to the table as a broken chair', 'if I had a nickel for every time you said something smart, I’d be broke', 'you’re like a cloud – when you disappear, it’s a beautiful day', 'I’d agree with you, but then we’d both be wrong', 'your brain is like a web browser with 100 tabs open and no memory', 'you’re not the sharpest tool in the shed, are you?', 'you’ve got the personality of a damp sponge', 'if I wanted to hear something stupid, I’d talk to myself', 'you have the charm of a brick wall', 'you have the intelligence of a rock, but not a cool one', 'if you were any more basic, you’d be a default font', 'is that your brain, or are you just staring into space?', 'I didn’t know we were doing a "try not to be smart" challenge', 'you’re like a broken pencil—pointless', 'your IQ is lower than your shoe size', 'I’ve seen more brain activity in a potato', 'you’re about as useful as a screen door on a submarine', 'your sense of direction is so bad, you get lost in your own thoughts', 'you couldn’t pour water out of a boot if the instructions were on the heel', 'you have the mental agility of a brick', 'if ignorance is bliss, you must be the happiest person alive', 'you’re like a phone with no signal – completely useless', 'you’re the human equivalent of a typo', 'you’re the type of person who’d lose a race against a turtle', 'your brain is so small, it could fit in a thimble', 'if I wanted your opinion, I’d ask for it... but I didn’t, so I won’t', 'you’re the reason we have instructions on shampoo bottles', 'you have the emotional depth of a puddle', 'if you were any more dense, we’d have to call a physicist', 'you’re like a dictionary with no words', 'I’d explain it to you, but I left my English-to-Dingbat dictionary at home', 'you couldn’t find your way out of a paper bag', 'if you were any more basic, you’d be a plain toast', 'you have the personality of a wet rag', 'your "wisdom" is as thin as a pancake', 'you bring as much excitement as a traffic cone', 'your ideas are as useful as a screen door on a submarine', 'you have the creativity of a brick', 'calling you an idiot would be an insult to idiots', 'if brains were dynamite, you wouldn’t have enough to blow your nose', 'you’re the kind of person who reads the back of a cereal box for fun', 'you’re like a cat in a swimming pool – completely out of place', 'I could explain it to you, but you’d still not get it', 'you have all the personality of a dial-up internet connection', 'if you had a dime for every smart thought, you’d still be poor', 'you’re like the human version of a typo', 'I’ve met houseplants with more common sense', 'you’re about as useful as a one-legged man in a butt-kicking contest', 'you must have been the class clown, because you’re always the punchline', 'if your brain was made of sand, it wouldn’t even fill a sandcastle', 'you’re like a VHS tape in the age of Netflix', 'your brain’s so empty, you could rent it out as storage space', 'you’re like a phone with no charger – completely useless', 'I’ve seen more logic in a bowl of spaghetti', 'you’re the kind of person who thinks they’re funny just by breathing', 'you’re the human equivalent of a mistake', 'you’ve got the social skills of a potato', 'I’m not saying you’re dumb, but you’ve got a real talent for it', 'if stupidity was a sport, you’d be a gold medalist', 'you have the mental capacity of a brick wall', 'you have less personality than a plank of wood', 'you have the charm of a wet noodle', 'I’ve met rocks with more charisma', 'you have the energy of a drained battery', 'you could fall into a pool and still not get wet', 'I’ve seen more intelligent conversations in a can of tuna fish', 'you bring nothing to the table except for the table itself', 'you’ve got the depth of a puddle', 'your ideas are like bad Wi-Fi – no one wants them', 'I could give you a dollar and you still wouldn’t know what to do with it', 'your future’s so bright, you must have a flashlight', 'you’re the kind of person who walks into a room and forgets why they’re there', 'you must be the reason the word "basic" exists', 'you’re the best at being the worst', 'you’re the kind of person who brings a spoon to a knife fight', 'you’re like a glass of warm milk – bland and useless', 'you’ve got the common sense of a jellyfish']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

print(f'''
{Fore.RED}╦╔═╦ ╦╔═╗╦ ╦╔╦╗╔═╗
{Fore.RED}╠╩╗╚╦╝╠═╣║ ║ ║ ║ ║
{Fore.RED}╩ ╩ ╩ ╩ ╩╚═╝ ╩ ╚═╝
{Fore.RESET}-----------------------
{Fore.RESET}USER INFO:
{Fore.GREEN}User: @{username}
{Fore.YELLOW}ID: {userid}
{Fore.BLUE}Channel: {channel_id}
''')

while True:
    wait_time = random.randint(7, 10)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    time.sleep(wait_time)
