import csv
import os
from getpass import getpass
# import required module
from cryptography.fernet import Fernet

fernet = Fernet("J64ZHFpCWFlS9zT7y5zxuQN1Gb09y7cucne_EhuWyDM=")

with open('C:/Users/felix/OneDrive/Skrivebord/visual studio code/code p/loginchat/logins.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        line_count += 1
    csv_file.close

if line_count == 0:
    npw = getpass("make a password:")
    with open('C:/Users/felix/OneDrive/Skrivebord/visual studio code/code p/loginchat/logins.txt', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        encrypted = fernet.encrypt(bytes(npw, 'utf-8'))
        print(encrypted)
        writer.writerow([encrypted])
        csv_file.close
wpw = True
pw = getpass("enter your password:")
with open('C:/Users/felix/OneDrive/Skrivebord/visual studio code/code p/loginchat/logins.txt', mode='r') as csv_file1:
    csv_reader = csv.DictReader(csv_file1)
    for row in csv_reader:
        decrypted2 = str(fernet.decrypt(row['pass'][2:-1]))[2:-1]
        while wpw:
            if pw == decrypted2:
                wpw = False
                print("loged in ")
                run_ac = ""
                while run_ac != "l":
                    run_ac = input("do you want to(logout(l)/add msg(am)/read msg(rm))")
                    if run_ac == 'am':
                        run_w_to_msg = input("add message:")
                        with open('C:/Users/felix/OneDrive/Skrivebord/visual studio code/code p/loginchat/msgts.txt', mode='a') as csv_file:
                            writer = csv.writer(csv_file)
                            encrypted = fernet.encrypt(bytes(run_w_to_msg, 'utf-8'))
                            #print(encrypted)
                            fieldnames = ['message']

                            # write the header
                            writer.writerow(fieldnames)

                                # write the data
                            #writer.writerow(data)

                            writer.writerow([encrypted])
                            csv_file.close()
                    elif run_ac == 'l':
                        os.close
                    elif run_ac == 'rm':
                        with open('C:/Users/felix/OneDrive/Skrivebord/visual studio code/code p/loginchat/msgts.txt', mode='r') as csv_file1:
                            csv_reader2 = csv.DictReader(csv_file1)
                            for row in csv_reader2:
                                message = str(fernet.decrypt(row['message'][2:-1]))[2:-1]
                                print(message)
                            csv_file1.close
            else:
                wpw = True
                pw = getpass("enter your password:")
