import datetime
from dateutil.relativedelta import relativedelta

from users.models import CustomUser
from authors.models import Author
from libraries.models import Library
from publishers.models import Publisher
from vendors.models import Vendor
from books.models import Book

CustomUser.objects.create_user(first_name="Adam", last_name="Smith", email="member1@example.com", phone_number="3124567890", password="Password123!", role="1", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
CustomUser.objects.create_user(first_name="Leon", last_name="White", email="member2@example.com", phone_number="3124567890", password="Password123!", role="1", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
CustomUser.objects.create_user(first_name="James", last_name="McCormick", email="employee1@example.com", phone_number="3124567890", password="Password123!", role="2", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
CustomUser.objects.create_user(first_name="Chris", last_name="Brock", email="employee2@example.com", phone_number="3124567890", password="Password123!", role="2", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
CustomUser.objects.create_user(first_name="Jane", last_name="Doe", email="owner1@example.com", phone_number="3124567890", password="Password123!", role="3", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
CustomUser.objects.create_user(first_name="Jack", last_name="Doves", email="owner2@example.com", phone_number="3124567890", password="Password123!", role="3", street="8423 Bell Oaks Dr", city="Newburgh", state="Iowa", zip_code="47630")
print("Users successfully created. ")

Author.objects.create(first_name="David", last_name="Goggins", subject="Self-Help")
Author.objects.create(first_name="Gordon", last_name="Ramsey", subject="Curlinary")
Author.objects.create(first_name="JK", last_name="Rowling", subject="Sci-Fi")
Author.objects.create(first_name="Stephen", last_name="King", subject="Horror")
Author.objects.create(first_name="Tim", last_name="Ferris", subject="Business")
print("Authors successfully created. ")

Library.objects.create(name="Harold Washington Library Center", phone_number="3127474300", address="400 S State St, Chicago, IL 60605", owner=CustomUser.objects.get(email="owner2@example.com"))
Library.objects.create(name="Chinatown Branch Library", phone_number="3127478013", address="2100 S Wentworth Ave, Chicago, IL 60616", owner=CustomUser.objects.get(email="owner2@example.com"))
Library.objects.create(name="Sulzer Regional Library", phone_number="3127447616", address="4455 N Lincoln Ave, Chicago, IL 60625", owner=CustomUser.objects.get(email="owner1@example.com"))
Library.objects.create(name="Richard J. Klarchek Information Commons", phone_number="3124567890", address="N Sheridan Rd, Chicago, Illinois, EEUU", owner=CustomUser.objects.get(email="owner1@example.com"))
Library.objects.create(name="Evanston Public Library", phone_number="8474488600", address="1703 Orrington Ave, Evanston, IL 60201", owner=CustomUser.objects.get(email="owner1@example.com"))
print("Libraries successfully created. ")

Publisher.objects.create(name="Simon & Schuster", country="United States")
Publisher.objects.create(name="Bertelsmann Education Group", country="United States")
Publisher.objects.create(name="Scholastic", country="United States")
Publisher.objects.create(name="Penguin Random House", country="United States")
Publisher.objects.create(name="Macmillan Publishers", country="United States")
print("Publishers successfully created. ")

Vendor.objects.create(name="Pilsen Community Books", address="1102 W 18th St, Chicago, IL 60608", phone_number="3124789434")
Vendor.objects.create(name="Open Books Pilsen", address="905 W 19th St, Chicago, IL 60608", phone_number="3122439776")
Vendor.objects.create(name="Sandmeyer's Bookstore", address="714 S Dearborn St, Chicago, IL 60605", phone_number="3129222104")
Vendor.objects.create(name="Tangible Books", address="3324 S Halsted St, Chicago, IL 60608", phone_number="7735654088")
Vendor.objects.create(name="Madison Street Books", address="1127 W Madison St, Chicago, IL 60607", phone_number="3129294140")
print("Vendors successfully created. ")

Book.objects.create(title="Gordon Ramsay's Fast Food: Recipes from the F Word", price=6.99, library=Library.objects.get(name="Harold Washington Library Center"), author=Author.objects.get(first_name="Gordon", last_name="Ramsey"), publisher=Publisher.objects.get(name="Simon & Schuster"), vendor=Vendor.objects.get(name="Pilsen Community Books"), status="Borrowed", borrower=CustomUser.objects.get(email="member1@example.com"), borrow_date=datetime.datetime.now(), return_date=datetime.datetime.now() + relativedelta(months=1), charge=0)
Book.objects.create(title="On Writing", price=13.09, library=Library.objects.get(name="Sulzer Regional Library"), author=Author.objects.get(first_name="Stephen", last_name="King"), publisher=Publisher.objects.get(name="Penguin Random House"), vendor=Vendor.objects.get(name="Sandmeyer's Bookstore"), status="Borrowed", borrower=CustomUser.objects.get(email="member1@example.com"), borrow_date=datetime.datetime.now(), return_date=datetime.datetime.now() + relativedelta(months=1), charge=0)
Book.objects.create(title="The 4-Hour Work Week: Escape 9-5, Live Anywhere, and Join the New Rich", price=7.39, library=Library.objects.get(name="Richard J. Klarchek Information Commons"), author=Author.objects.get(first_name="Tim", last_name="Ferris"), publisher=Publisher.objects.get(name="Bertelsmann Education Group"), vendor=Vendor.objects.get(name="Sandmeyer's Bookstore"), status="Borrowed", borrower=CustomUser.objects.get(email="member1@example.com"), borrow_date=datetime.datetime.now(), return_date=datetime.datetime.now() + relativedelta(months=1), charge=0)
Book.objects.create(title="The Shining", price=10.89, library=Library.objects.get(name="Evanston Public Library"), author=Author.objects.get(first_name="Stephen", last_name="King"), publisher=Publisher.objects.get(name="Penguin Random House"), vendor=Vendor.objects.get(name="Tangible Books"), status="Borrowed", borrower=CustomUser.objects.get(email="member2@example.com"), borrow_date=datetime.datetime.now(), return_date=datetime.datetime.now() + relativedelta(months=1), charge=0)
print("Books successfully created. ")
