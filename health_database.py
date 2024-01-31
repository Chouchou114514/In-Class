"""
Single patient record: [Name(str),age(int),MRN(int), Tests(list)]
Test list: [("HDL",100)]
"""

def create_database_entry(name, age, mrn):
    new_patient = [name, age, mrn, []]
    return new_patient

def print_database(db):
    rooms = ["Room A", "Room B", "Room C"]
    for i, zipped_data in enumerate(zip(db, rooms)):
        patient, room = zipped_data
        if i == 1:
            continue
        print("{} = Name:{}, MRN:{}, Age:{}, List:{}, Room:{}".format(i, patient[0], patient[2], patient[1], patient[3], room))

def get_patient(db, MRN):
    for patient in db:
        if patient[2] == MRN:
            answer = patient
            break
    return answer

def add_test_to_patient(db,MRN,test_name,test_value):
    patient = get_patient(db,MRN)
    patient[3].append([test_name,test_value])


def main():
    db = []
    db.append(create_database_entry("Ann Ables", 36, 101))
    db.append(create_database_entry("Bob Boylse",25,102))
    db.append(create_database_entry("Chris Chou", 50, 103))

    print_database(db)
    add_test_to_patient(db, 101, "HDL", 100)
    add_test_to_patient(db,101,"LDL", 102)
    print()
    print_database(db)
if __name__ == "__main__":
    main()