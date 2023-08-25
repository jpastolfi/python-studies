# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, recipient_name):
  template = open(card_type, 'r')
  card_to_write_name = '{}_generic.txt'.format(sender_name)
  card_to_write = open(card_to_write_name, 'w')
  try:
    card_to_write.write('Dear {}\n'.format(recipient_name))
    card_to_write.write(template.read())
    card_to_write.write('\nSincerely {}'.format(sender_name))
    yield card_to_write
  finally:
    template.close()
    card_to_write.close()
    
with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as first_order:
  print('Card Generated!')
with open('Mwenda_generic.txt', 'r') as test_run:
  print(test_run.read())

class Personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file_to_write = open('{}_personalized.txt'.format(sender), 'w')

  def __enter__(self):
    self.file_to_write.write('Dear {}\n'.format(self.receiver))
    return self.file_to_write
  
  def __exit__(self, exc_type, exc_value, traceback):
    self.file_to_write.write('\nSincerely {}'.format(self.sender))
    self.file_to_write.close()

with Personalized('John', 'Michael') as card:
  card.write('I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.')

with generic('happy_bday.txt', 'Josiah', 'Remy') as second_order:
  with Personalized('Josiah', 'Esther') as second_card:
    second_card.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")