gambar = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
#Write your code below this line 👇
import random

pemain = int(input())
bot = random.randint(0, 2)
urutan = ['rock', 'paper', 'scissors']
if pemain > 2:
    print("You choose wrong number")
    exit()
print("You choose ", urutan[pemain])
r1 = urutan[pemain]
r2 = urutan[bot]
if r1 == r2:
    kemenangan = 'Draw'
elif r1 == 'rock' and r2 == 'scissors':
    kemenangan = 'Win'
elif r1 == 'paper' and r2 == 'rock':
    kemenangan = 'Win'
elif r1 == 'scissors' and r2 == 'paper':
    kemenangan = 'Win'
else:
    kemenangan = 'Lose'
print(gambar[pemain])
print("Bot choose ", urutan[bot])
print(gambar[bot])
print("You are " + kemenangan)
