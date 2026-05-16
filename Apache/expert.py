found = False
symptom = False
issue = []

def engine_check():
    global found
    global symptom
    issue_element = []
    engine = input("Engine not starting (y,n)")

    if engine=='y':
        symptom = True
        issue_element.append("engine -> ")

    if engine == 'y':
        rumble = input("Does the engine rumble? (y/n)")
        if rumble == 'y':
            issue_element.append("rumble ->")
            print("problem: check mechanical alignment")
            found = True
        else:
            fuel = input("Is there fuel in tank (y/n)")
            if fuel == 'y':
                print("problem: ignition issue")
                found = True
            else:
                issue_element.append("fuel")
                print("No fuel bitch")
    return(issue_element)

print("Car troubleshooting Expert system\n")

issue.append(engine_check())

print(issue)

if found == False and symptom==False:
    print("No issues sar")
if found == False and symptom==True:
    print("Unknown issue, Please see mechanic")