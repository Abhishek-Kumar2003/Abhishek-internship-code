import streamlit as st
import csv
import random

class Stadium:
    def _init_(self, upper, middle, lower, total, booked, base):
        self.upper = upper
        self.middle = middle
        self.lower = lower
        self.total = total
        self.booked = booked
        self.notbooked = total - booked
        self.baseprice = base

    def book_ticket(self):
        dictionary = {3: "CSK vs RCB", 5: "RR vs SRH", 7: "CSK vs SRH", 9: "RCB vs SRH", 11: "CSK vs RR", 13: "RCB vs RR"}
        std = ['upper', 'middle', 'lower']
        st.write("Number of seats left:", self.notbooked)
        st.write("Number of seats left in upper stands:", self.upper)
        st.write("Number of seats left in middle stands:", self.middle)
        st.write("Number of seats left in lower stands:", self.lower)
        num = st.number_input("How many tickets you want to buy:", min_value=1, max_value=self.notbooked)
        if num > self.notbooked:
            st.error("More seats are being booked than the availability")
            return
        for _ in range(num):
            self.booked += 1
            self.notbooked -= 1
            names = st.text_input("Enter your name",key="name")
            phone = st.text_input("Enter your phone number",key="phone")
            if len(phone) != 10 or not phone.isdigit():
                st.error("Incorrect phone number given")
                break
            ages = st.number_input("Enter your age:",key="age")
            date = st.number_input("Enter the date of the match:",key="date")
            fld = [names, phone, ages, date]
            r = random.randint(1, 6)
            if date not in dictionary.keys():
                st.error("There is no match on that day")
                self.booked -= 1
                self.notbooked += 1
                break
            else:
                with open('C:/Users/SRIHARI/Desktop/VS Code project/booking.csv', 'a') as f1:
                    writ = csv.writer(f1, delimiter=',')
                    writ.writerow(["Name", "Phno", "Age", "Date"])
                    writ.writerow(fld)
            yesno = st.selectbox("Do you want to choose the stand?", ('Yes', 'No'))
            if yesno == 'Yes':
                stand = st.selectbox("Enter the stand you want to book", ('Upper', 'Middle', 'Lower'))
                stand = stand.lower()
                if stand == "upper":
                    self.upper -= 1
                    price = self.baseprice + 500
                    price = price + (price * 0.18)
                elif stand == "middle":
                    self.middle -= 1
                    price = self.baseprice + 1500
                    price = price + (price * 0.18)
                elif stand == "lower":
                    self.lower -= 1
                    price = self.baseprice + 600
                    price = price + (price * 0.18)
            else:
                stand = random.choice(std)
                if stand == "upper":
                    self.upper -= 1
                    price = self.baseprice + 500
                    price = price + (price * 0.18)
                elif stand == "middle":
                    self.middle -= 1
                    price = self.baseprice + 1500
                    price = price + (price * 0.18)
                elif stand == "lower":
                    self.lower -= 1
                    price = self.baseprice + 600
                    price = price + (price * 0.18)
            st.write("+  ", "Name", "    ", "Phone number", "     ", "Age", "     ", "Date of Match", "      ")
            st.write("+ ", names, "      ", phone, "        ", ages, "        ", date, "              ")
            st.write("+      Seat is in the", stand, "stand", "                           ")
            st.write("+      Entry gate is", r, "                                         ")
            st.write("+                           ", "Total price=", price, "                ")
            st.write("+                           ", "Ticket issued by DJKY Associates     ")

    def print_schedule(self):
        with open('C:/Users/SRIHARI/Desktop/VS Code project/schedule.csv', 'r') as x:
            read = csv.reader(x)
            for i in read:
                st.write(i)

    def enquiry(self):
        st.write("For further assistance contact at: 1800 123 456")
        st.write("\n\n")
        st.write("Email us: stadiumcare@greatwebsite.com")

if _name_ == "_main_":
    st.title("Stadium Ticket Booking System")
    stadium = Stadium(100, 52, 200, 2000, 1648, 1000)
    choice = st.sidebar.selectbox("Select an option", ("Booking", "Print Schedule", "Enquiry"))
    if choice == "Booking":
        stadium.book_ticket()
    elif choice == "Print Schedule":
        stadium.print_schedule()
    elif choice == "Enquiry":
        stadium.enquiry()
