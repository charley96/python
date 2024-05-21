# Want to write a function that gets the program running and responds to the user
# Direct flow according to user selection
# Main function will point to one of two other functions
# Usually best practice to create variable outside of function
# Break everything up as each function should just have 1 job

welcome_prompt = "Welcome Doctor, what would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press Q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"
error_message = "Error! Could not save patient details due to invalid input"
patient_and_diagnosis_list = []

def list_patients():
    for i in patient_and_diagnosis_list:
        print(i)

def assess_skin(skin_health):
    if skin_health == "1":
        return some_dehydration
    elif skin_health == "2":
        return severe_dehydration
    else:
        return ""

def assess_eyes(eye_health):
    if eye_health == "1":
        return no_dehydration
    elif eye_health == "2":
        return severe_dehydration
    else:
        return ""

def diagnose_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eye = input(eye_prompt)
        return assess_eyes(eye)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""

def start_new_diagnosis():
    # Based on user input to determine dehydration level
    patient_name = input(name_prompt)
    diagnosis = diagnose_appearance()
    
    return save_new_diagnosis(patient_name, diagnosis)

def save_new_diagnosis(name, diagnosis):
    if diagnosis == "" or name.isalpha() == False:
        print(error_message)
        return
    final_diagnosis = name + " - " + diagnosis
    patient_and_diagnosis_list.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis, "\n")

def main():
    while(True):
        selection = input(welcome_prompt)
        if      selection == "1":
            list_patients()
        elif    selection == "2":
            start_new_diagnosis()
        elif    selection == "q":                   # want to the process to run indefinately, until q is pressed
            return

# main()


def test_assess_skin():             # This is considered unit testing
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("Charley") == "")             # 3 trues indicate that the function has passed the test


# test_assess_skin()

def test_diagnose_appearance():     # This is integration testing
    print(diagnose_appearance()) 

# test_diagnose_appearance()

# Want to test all of our functions
# Can do unit tests for eyes, assessing skin and somewhat for save new diagnosis
# The rest should be integration tested

def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("charley") == "")

# test_assess_eyes()

def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(patient_and_diagnosis_list)
    save_new_diagnosis("123", "")
    print(patient_and_diagnosis_list)
    save_new_diagnosis("123", "Charley Jones")
    print(patient_and_diagnosis_list)
    save_new_diagnosis("Charley Jones", "123")
    print(patient_and_diagnosis_list)
    save_new_diagnosis("CharleyJones", "No dehydration")
    print(patient_and_diagnosis_list)

test_save_new_diagnosis()       # Found issue with spaces being recognised as non-alpha characters. Would need to fix.