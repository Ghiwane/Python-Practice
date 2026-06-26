import csv
import os

def add_contact(name, num, email, file):
    try:
        file_exists = os.path.exists(file)
        with open(file, "a", encoding="utf-8", newline="") as f:
            lead = ["name", "num", "email"]
            writer = csv.DictWriter(f, fieldnames=lead)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "name": name,
                "num": num,
                "email": email
             })
        print("Saved succesfully!")
    except Exception as e:
        print(f"error : {e}")

def research_name(name, file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            found = False
            for line in reader:
                if name == line["name"]:
                    print(f"{line['name']}, {line['num']}, {line['email']}")
                    found = True
                    break
            if not found:
                print(f"{name} Not found")
    except FileNotFoundError:
        print("File not found")

add_contact("Zack", "0612345678", "Zack@mail.com", "contacts.csv")
add_contact("Nani", "0698765432", "Nani@mail.com", "contacts.csv")
research_name("Zack", "contacts.csv")
research_name("lunsi", "contacts.csv")