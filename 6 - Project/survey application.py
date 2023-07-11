import os
import random

# survey application class

class Application:
    def __init__(self):
        try:
            os.mkdir("survey")
        except:
            pass

        # create file inside survey folder
        with open("survey/survey_info.txt", "a"):
            pass

    # create function for unique code
    def unique_code(self):
        otp = random.randint(10000, 99999)
        otp = "00"+str(otp)+"00"
        return otp

    # read all data from the file
    def read_all_data(self):
        with open("survey/survey_info.txt", "r") as file:
            data = file.read()
        return data

    def add_info(self, name, age, family_mem, contact, location, qualification, working_people, annual_income):
        otp = self.unique_code()
        file_data = self.read_all_data()

        # check otp in file_data
        if otp in file_data:
            print("\n========== OTP Already Exist Try Again... ==========\n")

        else:
            with open("survey/survey_info.txt", "a") as file:
                print(
                    f"User {name} added to the survey and the otp is {otp}...")
                file.write(
                    f"User {name} added to the survey and the otp is {otp}...\n")
                file.write(f"Age is : {age}\n")
                file.write(f"Family member : {family_mem}\n")
                file.write(f"Contact is : {contact}\n")
                file.write(f"location is : {location}\n")
                file.write(f"Qualification is : {qualification}\n")
                file.write(f"Working People is : {working_people}\n")
                file.write(f"Annual Income : {annual_income}\n")
                print()

    def search(self, unique):
        # read existing file
        with open("survey/survey_info.txt", "r") as file:
            all_register_data = file.readlines()

        for user_data in all_register_data:
            if unique in user_data:
                pos = all_register_data.index(user_data)
                data = all_register_data[pos: pos+9]
                data = "".join(data)
                return data


class LoginRegister(Application):
    def __init__(self):
        super().__init__()
        # make folder
        try:
            os.mkdir("register")
        except:
            pass

        # create file inside register folder
        with open("register/register_user.txt", "a"):
            pass

        # create flag
        self.register_flag = False
        self.login_flag = False

    def register(self, name, age, email, pass2):
        # read existing file
        with open("register/register_user.txt", "r") as file:
            all_data = file.read()

        # check email in the all_data
        if email in all_data:
            print("\n========== Email Already Exist Try Again... ==========\n")

        else:
            # generate data
            data = f"{name},{age},{email},{pass2},\n"

            # append data in the file
            with open("register/register_user.txt", "a") as file:
                file.write(data)
                self.register_flag = True

        return self.register_flag

    def login(self, email, passwd):
        # read existing file
        with open("register/register_user.txt", "r") as file:
            all_register_data = file.readlines()

        # check user informatiom
        for user in all_register_data:
            user_data = user.split(",")

        # match data into user_data
        if (email == user_data[2]) and (passwd == user_data[3]):
            self.login_flag = True

        return self.login_flag


# application start from here
if __name__ == "__main__":
    # creating instance
    app = LoginRegister()

    print("\n--------------- Welcome To My Application ---------------\n")

    while True:
        print("1 - Registration \n2 - Login \n3 - Exit\n")

        ch = input("Enter Your Choice:")

        if ch == "1":
            print("\n--------------- Welcome To Registration Form ---------------\n")

            name = input("Enter Your Name :")
            age = input("Enter Your Age :")
            email = input("Enter Your Email :")
            pass1 = input("Enter Your Password :")
            pass1 = pass1.strip()

            if (len(pass1) < 5):
                print(
                    "\n========== Password should be greater than 5 character ==========\n")

            elif (len(pass1) > 15):
                print(
                    "\n========== Password should be less than 15 character ==========\n")

            else:
                pass2 = input("Enter Conform Password :")
                pass2 = pass2.strip()

                if (pass1 != pass2):
                    print("\n========== Invalid Password Try Again... ==========\n")

                else:
                    name = name.strip()
                    age = age.strip()
                    email = email.strip()

                    # send data to the method
                    w_flag = app.register(name, age, email, pass2)

                    if w_flag == False:
                        print("\n========== Registration Failed ==========\n")

                    else:
                        print("\n========== Registration Successfully ==========\n")

        elif ch == "2":
            print("\n--------------- Welcome To Login Form ---------------\n")
            email = input("Enter Your Email :")
            passwd = input("Enter Your Password :")

            # remove extra space
            email = email.strip()
            passwd = passwd.strip()

            # send data to the method
            r_flag = app.login(email, passwd)

            if r_flag == False:
                print("\n========== Login Failed ==========\n")

            else:
                print("\n========== Login Successfully ==========\n")

                # survey application start from here
                print(
                    "\n--------------- Welcome To Survey Application ---------------\n")

                while True:
                    print(
                        "1 - Add User Information \n2 - Search specific User with code \n3 - Exit Survey Application\n")

                    app_ch = input("Enter Application Choice :")

                    if app_ch == "1":
                        print("\n--------------- Add Information ---------------\n")

                        name = input("Enter Name: ")
                        age = input("Enter Age :")
                        family_mem = input("Enter Family Member :")
                        contact = input("Enter Contact :")
                        location = input("Enter Location :")
                        qualification = input("Enter Qulification :")
                        working_people = input("Enter Working People :")
                        annual_income = input("Enter Annaul Income :")

                        # remove extra space
                        name = name.strip()
                        age = age.strip()
                        family_mem = family_mem.strip()
                        contact = contact.strip()
                        location = location.strip()
                        qualification = qualification.strip()
                        working_people = working_people.strip()
                        annual_income = annual_income.strip()

                        app.add_info(name, age, family_mem, contact, location,
                                     qualification, working_people, annual_income)

                    elif app_ch == "2":
                        print(
                            "\n--------------- Search Unique code ---------------\n")

                        unique = input("Enter Your Unique code:")
                        unique = unique.strip()

                        data = app.search(unique)

                        if data == "None":
                            print(
                                "\n========== Unique Code Not Available ==========\n")

                        else:
                            print(data)

                    elif app_ch == "3":
                        print(
                            "\n========== Thank You For Using My Application ==========\n")
                        break

                    else:
                        print("\n========== Invalid Input ==========\n")

        elif ch == "3":
            print("\n========== Thank You For Using My Application ==========\n")
            break

        else:
            print("\n========== Invalid Input ==========\n")
