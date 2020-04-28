import markovify

from .cosmos import cosmos

team_ayy_lmao_users = {
  'd': 'U0316HMAS',
  'tom': 'U034S6QF6',
  'austin': 'U03169VDW',
  'rid': 'U0314Q64M',
  'thomas': 'U031D6P73',
  'matty': 'U03LTN7RH',
  'beej': 'U03JA1HKP',
  'nickpray': 'U09BC6LR5'
}

def main():
  user = team_ayy_lmao_users['rid']
  messages = [ item["text"] for item in cosmos.get_message_events_for_user(user) ]
  newline_delimited_messages = "\n".join(messages)

  model = markovify.NewlineText(newline_delimited_messages)
  for i in range(20):
    print(model.make_sentence())
