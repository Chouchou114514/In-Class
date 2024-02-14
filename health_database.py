"""
Single patient record: [Name(str),age(int),MRN(int), Tests(list)]
Test list: [("HDL",100)]
"""

def create_database_entry(first_name, last_name, age, mrn, tests):
    new_patient = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'mrn': mrn,
        'tests': tests
    }
    return new_patient

def get_full_name(patient):
    full_name = patient['first_name'] + " " + patient['last_name']
    return full_name


def print_database(db):
    for i in db:
        print("MRN: {}, Full name: {}, Age: {}" .format(i['mrn'], i['first_name'] + " " + i['last_name'], i['age']))


def get_patient(db, mrn):
    for patient in db:
        if patient['mrn'] == mrn:
            return patient

def add_test_to_patient(db, mrn, test_name, test_value):
    patient = get_patient(db, mrn)
    patient[test_name] = test_value

def minor_or_adult(patient):
    if patient['age'] >= 18:
        print("{} is an adult." .format(get_full_name(patient)))
        return "adult"
    else:
        print("{} is a child" .format(get_full_name(patient)))
        return "minor"

def main():
    db = []
    db.append(create_database_entry("Ann", "Ables", 36, 101, [("HDL", 100)]))
    db.append(create_database_entry("Bob", "Boylse", 25, 102, [("HDL", 90)]))
    db.append(create_database_entry("Chris", "Chou", 50, 103, [("HDL", 110)]))

    pat = get_patient(db, 101)
    print(pat)
    print_database(db)
if __name__ == "__main__":
    main()