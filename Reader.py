import csv
from Video import Film
from Video import Google_Talk
import smtplib
from random import randint

""" Reads from two .csv files to send email containing a film and Talk at
Google recommendation to given email address"""

print "Welcome to my final project! In order for this code to execute, the code will \
require you to enter your gmail email credentials. (See code for details -- don't worry, \
this code is innocuous!)"
username = raw_input("Enter your gmail address:")
password = raw_input("Enter your gmail password:")

'''First, create lists `film_library` and `gt_library` that contain instances of Film() \
objects and Google_Talk() objects, respectively. 
'''

film_library = []
with open("C:\Python27\Udacity_Final_Project\AFI.csv","rb") as f:
    reader = csv.reader(f)
    for film_info in reader:
       new_film = Film(*film_info)
       film_library.append(new_film)

gt_library = []
with open("C:\Python27\Udacity_Final_Project\GT.csv","rb") as f:
    reader = csv.reader(f)
    for talk_info in reader:
       new_talk = Google_Talk(*talk_info)
       gt_library.append(new_talk)

'''Next, randomly choose a Film() that has NOT been seen yet to feature in our program's
email. '''

rnum_keeper = []
while len(rnum_keeper)<100:
   rnum = randint(0,99)
   while rnum in rnum_keeper: #This while loop is to ensure a random number isn't tested twice
      rnum = randint(0,99)
   if film_library[rnum].check_seen() == 'FALSE': # = If a movie hasn't been seen yet:
      msg1 = str(film_library[rnum].email_template()) #`msg` for email message
      with open('C:\Python27\Udacity_Final_Project\AFI.csv', 'rb') as file1: #opens AFI.csv to edit rows to list `new_row`
         new_row = []
         reader = csv.reader(file1)
         for row in reader:
            new_row.append(row)
         new_row[rnum][2] = 'TRUE'
      with open('C:\Python27\Udacity_Final_Project\AFI.csv', 'wb') as file2:
         writer = csv.writer(file2)
         for row in new_row:
            writer.writerow(row)
      break
   else:
      rnum_keeper.append(rnum)
      if len(rnum_keeper) == 100: #If all movies have been sent in an email/seen already
         msg1 = "Congrats -- you've seen all the movies on \
AFI's 100 Years ... 100 Movies list! Go buy yourself a drink \
with someone you care about." + '\n' + '---------------------------------'
         break
      
'''Repeat procedure for Google Talk videos. '''

rnum_keeper = []
while len(rnum_keeper)<62:
   rnum = randint(0,61)
   while rnum in rnum_keeper:
      rnum = randint(0,61)
   if gt_library[rnum].check_seen() == 'FALSE': 
      msg2 = str(gt_library[rnum].email_template()) 
      with open('C:\Python27\Udacity_Final_Project\GT.csv', 'rb') as file1:
         new_row = []
         reader = csv.reader(file1)
         for row in reader:
            new_row.append(row)
         new_row[rnum][2] = 'TRUE'
      with open('C:\Python27\Udacity_Final_Project\GT.csv', 'wb') as file2:
         writer = csv.writer(file2)
         for row in new_row:
            writer.writerow(row)
      break
   else:
      rnum_keeper.append(rnum)
      if len(rnum_keeper) == 62:
         msg2 = '\n' + "Congrats -- you've seen some of the most watched \
Talks at Google on Youtube! Go enlighten the world with your \
new knowledge."

msg = msg1 + msg2 # concatenate email messages

'''Sends email via gmail with 'msg' body of text. Program prompts user for credentials
to execute the code and send the email.  
'''

From = 'zthomas.nc@gmail.com'
Recipient = username
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(username, password)
server.sendmail(From, Recipient, msg)
print "Done! Just a minute until the email appears in your inbox ..."
server.quit()



