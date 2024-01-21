print("****WELCOME**TO**ATM****")
password=1234
balance=20000
print("1=**YES**\n2= **NO**")
a=eval(input("choose your option>>>...."))
if a==1:
    print("****THANK**YOU****")
    print("1=****ENGLISH****\n2=****HINDI****")
    c=eval(input("choose your option>>>>>..."))
    if c==1:
        print("****THANK**YOU****")
        b=eval(input("enter the pincode password>>>..."))
        if b==password:
            print("****THANK**YOU****")
            print("1=**Balance**\n2=**Deposite**\n3=**Withdraw**\n4=**change pincode**")
            b=eval(input("Choose your option>>>..."))
            if b==1:
                print("****THANK**YOU****")
                b=eval(input("enter the pincode password>>>..."))
                if b==password:
                    print("****THANK**YOU****")
                    print("YOUR ACOUNT BALANCE IS=$",balance)
                
            elif b==2:
                print("****THANK**YOU****")
                b=eval(input("enter the pincode password>>>..."))
                if b==password:
                    print("****THANK**YOU****")
                    c=eval(input("Enter the Deposite balance=$>>>>.."))
                    print("Your previous balance=$",balance)
                    if c>=0:
                        balance+=c
                        print("****See**Your** Remaining** balance=$")
                        b=eval(input("enter the pincode password>>>..."))
                        if b==password:
                            print("****THANK**YOU****")
                            print("Your Remaining Balannce=$",balance)
                    else:
                        print("You Can Deposite only Positive Rupees")


            
            elif b==3:
                print("****THANK**YOU****")
                b=eval(input("enter the pincode password>>>..."))
                if b==password:
                    print("****THANK**YOU****")
                    c=eval(input("Enter the Withdraw balance=$>>>>.."))
                    print("Your previous balance=$",balance)
                    if c>=0 and c<=balance:
                        balance-=c
                        print("****See**Your** Remaining** balance=$")
                        b=eval(input("enter the pincode password>>>..."))
                        if b==password:
                            print("****THANK**YOU****")
                            print("Your Remaining Balannce=$",balance)
                    else:
                        print("Please Withdraw as much or as much balance as you have in your bank")

            elif b==4:
                print("****THANK**YOU****")
                b=eval(input("enter the pincode password>>>..."))
                if b==password:
                    print("****THANK**YOU****")
                    a=eval(input("Change Your Pin Password>>>>..."))
                    b=a
                    if a>=1000 and a<=9999 and a!=password:
                        print("****THANK**YOU****")
                        print("Your pin Password is change")
                        c=eval(input("enter the Change Pin password>>>..."))
                        if c==b:
                            print("****THANK**YOU****")
                            print("Pin password login")
                        else:
                            print("Sorry")
                            print("Not login")
                    else:
                        print("sorry")
                        print("your Pin password only Four digit")
                else:
                    print("Sorry")
                    print("Your pin assword is wrong")

            else:
                print("Sorry")
                print("Please choose given option")
        else:
            print("Sorry")
            print("Your pin assword is wrong")

    elif c==2:
        print("****Dhanyawad****")
        b=eval(input("Kripya Aap Aapna Suraksha Kawach Dale>>>..."))
        if b==password:
            print("****Dhanyawad****")
            print("1=**Santulan Rasi**\n2=**Jama Rasi**\n3=**Nikasi Rasi**\n4=**Suraksha Kawach Badale**")
            b=eval(input("Diye Gaye Vikalpo Ko Chuniye >>>..."))
            if b==1:
                print("****Dhanyawad****")
                b=eval(input("Kripya Aap Aapna Suraksha Kawach Dale>>>..."))
                if b==password:
                    print("****Dhnyawad****")
                    print("Aaapki Santulan Rasi=$",balance)
                
            elif b==2:
                print("****Dhnyawad****")
                b=eval(input("Kripya Aap Aapna Suraksha Kawach Dale>>>..."))
                if b==password:
                    print("****Dhnyawad****")
                    c=eval(input("Kripya Aap Aapni Jama Rasi Dale=$>>>>.."))
                    print("Aaapki Santulan Rasi=$",balance)
                    if c>=0:
                        balance+=c
                        print("****Aap**Aapni**Bachi**Huwi**Rasi**Ko**check**Kare=$")
                        b=eval(input("Kripya Aap Aapna Suraksha Kawach Dale>>>..."))
                        if b==password:
                            print("****Dhnyawad****")
                            print("Aapki Bachi Huwi Rasi=$",balance)
                    else:
                        print("Aap kewal Dhanatmak rupees hi dal sakt ho")

            
            elif b==3:
                print("****Dhnyawad****")
                b=eval(input("Kripya Aap Aapna Suraksha Kawach Dale>>>..."))
                if b==password:
                    print("****Dhnyawad****")
                    c=eval(input("Kripya Aap Aapni Nikasi Rai Daliye=$>>>>.."))
                    print("Aapki Santulan Rasi=$",balance)
                    if c>=0 and c<=balance:
                        balance-=c
                        print("****Aap**Aapni**Bachi**Huwi**Rasi**Ko**check**Kare=$")
                        b=eval(input("Kripya Aap Aapni Nikasi Rai Daliye=$>>>..."))
                        if b==password:
                            print("****Dhnyawad****")
                            print("Aapki Bachi Huwi Rasi=$",balance)
                    else:
                        print("Kripya Utna Hi Rupaye Dalo Jitne Aapke Khate Me Hai")

            elif b==4:
                print("****Dhnyawad****")
                b=eval(input("Kripya Aap Aapni Nikasi Rai Daliye=$>>>..."))
                if b==password:
                    print("****Dhnyawad****")
                    a=eval(input("Kripya Aap Aapna Surksha Kawach Badale>>>>..."))
                    b=a
                    if a>=1000 and a<=9999 and a!=password:
                        print("****Dhnyawad****")
                        print("Aapka Suraksha Kawach Badal Gaya")
                        c=eval(input("Kripya Aap Aapna Badala Huwa Suraksha Kawach Dale>>>..."))
                        if c==b:
                            print("****Dhnyawad****")
                            print("Aapka Surakha Kawach Login Ho Gaya")
                        else:
                            print("Maph Kare")
                            print("Aapka Suraksha Kawach Login Nahi Huwa")
                    else:
                        print("Maph Kare")
                        print("Aapka Suraksha Kawach Kewal Chhar Anko Ka Hoga")
                else:
                    print("Maph Kare")
                    print("Aapka Suraksha Kawach Galat Hai")

            else:
                print("Maph Kare")
                print("Kripya Diye Gaye Vikalpo Se hi Chune")

        else:
            print("Sorry")
            print("Aapka Suraksha Kawach Galat Hai")           

    else:
        print("Sorry")
        print("Please Choose Your Given Option")
elif a==2:
    print("**NO**")
else:
    print("Sorry")
    print("Please Choose Your Given Option")







            
