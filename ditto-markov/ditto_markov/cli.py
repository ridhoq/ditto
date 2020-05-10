import sys

from .markov import get_model

team_ayy_lmao_users = {
  'd': 'U0316HMAS',
  'tom': 'U034S6QF6',
  'austin': 'U03169VDW',
  'rid': 'U0314Q64M',
  'thomas': 'U031D6P73',
  'matty': 'U03LTN7RH',
  'beej': 'U03JA1HKP',
  'nickpray': 'U09BC6LR5',
  'partypat': 'U22RC4XB2'
}

def main():
  user_name = sys.argv[1]
  user = team_ayy_lmao_users[user_name]
  model = get_model(user)
  for i in range(20):
    print(model.make_sentence())
