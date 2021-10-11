import csv

# Create list of users with compromised passwords
compromised_users = []

# Open file containing compromised users
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  # Add compromised usernames to compromised_users list
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username'])

# Write to file
with open("compromised_sers.txt", "w") as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

# Send encoded message to boss
import json

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# Remove passwords.csv file
with open("new_password.csv", "w") as new_passwords_obj:
  slash_null_sig = '''
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  '''
  new_passwords_obj.write(slash_null_sig)
