import markovify

from .cosmos import cosmos

# @d
# user = 'U0316HMAS'
# @tom
# user = 'U034S6QF6'
# @austin
# user = 'U03169VDW'
# @rid
user = 'U0314Q64M'
# @thomas
# user = 'U031D6P73'
# @matty
# user = 'U03LTN7RH'
# @beej
# user = 'U03JA1HKP'
# @nickpray
# user = 'U09BC6LR5'

def main():
  messages = [ item["text"] for item in cosmos.get_message_events_for_user(user) ]
  newline_delimited_messages = "\n".join(messages)

  model = markovify.NewlineText(newline_delimited_messages)
  for i in range(20):
    print(model.make_sentence())
