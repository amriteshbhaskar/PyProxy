#!/usr/bin/env python3
import re, os, getpass, sys


if sys.version_info.major >= 3:
    if os.geteuid() != 0:
        exit('You need root privileges to run this script.\nPlease try again, this time using "sudo".\nExiting.')
    
    def password_hex(password):
        hex_password = []
        for i in password:
            if i in ['@','!','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',';',':','"',"'",',','<','.','>','/','?','`','~',' ']:
                hex_password.append('%' + str(hex(ord(i))[2:]))
            else:
                hex_password.append(i)
        return ''.join(hex_password)
    print('\n\033[5;37;40m🌟\033[0;37;40m https://github.com/fl4shi3r/PyProxy\n')
    choice = int(input('1.set proxy\n2.unset proxy\nEnter your choice (1/2): '))
    if choice == 1:
        import environment, apt, npm, git, gsetting, bash, dnf
        host_ip = input('Enter the Proxy Host address: ')
        host_port = input('Enter the Proxy host port: ')

        pc_username = input('Enter the pc username: ')
        if os.path.isdir('/home/'+pc_username):
            username = ''
            password = ''
            auth_choice = (input('Is authentication required in your college/organization (yes/no): ')).lower()
            if auth_choice == 'yes' :
                username = input('Enter the username: ')
                password_unhexed = getpass.getpass(prompt='Enter the password: ')
                password = password_hex(password_unhexed)
            elif auth_choice == 'no':
                pass
            else:
                print('Try again with correct option')
                exit(1)   

            environment.set_proxy(host_ip, host_port, auth_choice, pc_username, username, password) 
            apt.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
            npm.set_proxy( host_ip, host_port, auth_choice,pc_username, username, password)
            git.set_proxy(host_ip, host_port, auth_choice, pc_username,username, password )
            gsetting.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
            bash.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
            dnf.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
        else:
            print("Incorrect pc username. Try again with correct pc username")
            exit(1)
            

    elif choice == 2:
        import environment, apt, npm, git, gsetting, bash, dnf
        pc_username = input('Enter the pc username: ')
        if os.path.isdir('/home/'+pc_username):
            environment.unset_proxy() 
            apt.unset_proxy()
            npm.unset_proxy(pc_username)
            git.unset_proxy(pc_username)
            gsetting.unset_proxy(pc_username)
            bash.unset_proxy(pc_username)
            dnf.unset_proxy()
            reboot_choice = (input('Reboot is required to apply the changes\nDo you want to reboot your system(yes/no)')).lower()
            if reboot_choice == "yes":
                print('Rebooting your system')
                os.system('reboot')
            
        else:
            print("Incorrect pc username. Try again with correct pc username")
            exit(1)
    else:
        print("Try again with correct option")
    

    
else:
    print('Kindly use python3 to run this scrypt')
