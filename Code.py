import pandas as pd
import matplotlib.pyplot as plt
path = "/home/allsabaab/Documents/VSCode/Farm Inventory/Farm Inventory.csv"

def create_list():
    csv = pd.read_csv(path)
    equipment_name = input("Equipment Name: ").title()
    while True:
        try:
            print("1.Motorized 2.Automated 3.Manual 4.Hybrid 5.Semi-Automated 6.Smart")
            equipment_list = [" ","Motorized","Automated","Manual","Hybrid","Semi-Automated","Smart"]
            list_input1 = int(input("Select the Type of Equipment: "))
            if list_input1<=len(equipment_list) and list_input1>0:
                equipment_type = equipment_list[list_input1]
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Invalid Input!!!")
            continue
    primary_use = input("Primary Use: ").title()
    while True:
        try:
            print("1.Diesel 2.Petrol 3.Electric 4.Human/Animal 5.Hybrid 6.Others")
            power_source_list = [" ","Diesel","Petrol","Electric","Human/Animal","Hybrid"]
            list_input2 = int(input("Select the Type of Power Source: "))
            if list_input2==6:
                other_power_source = input("Other Power Source: ").title()
                power_source_list.append(other_power_source)
            if list_input2<=len(power_source_list) and list_input2>0:
                power_source_type = power_source_list[list_input2]
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Inavalid Input!!!")
            continue
    while True:
        try:
            print("1.Available 2.Not Available 3.Others")
            availability_list = [" ","Available","Not Available"]
            list_input3 = int(input("Select Availability: "))
            if list_input3==3:
                other_availability = input("Others: ").title()
                availability_list.append(other_availability)
            if list_input3<=len(availability_list) and list_input3>0:
                availability = availability_list[list_input3]
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Inavalid Input!!!")
            continue
    price = int(input("Enter Price: "))

    new = pd.DataFrame({"Equipment Name":[equipment_name],"Type":[equipment_type],"Primary Use":[primary_use],
                        "Power Source":[power_source_type],"Availability":[availability],"Price(BDT)":[price]})
    csv = pd.concat([csv, new], ignore_index=True)
    csv.to_csv(path, index=False)
    print("")
    print("List Created Successfully!!!")
    return csv

def clear_list():
    csv = pd.read_csv(path)
    while True:
        try:
            row_num = int(input("Enter the row you want to delete: "))-1
            if row_num <= len(csv):
                csv = csv.drop(row_num).reset_index(drop=True)
                csv.to_csv(path, index=False)
                print("")
                print("List Cleared Successfully!!!")
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Invalid Input!!!")
            continue
    return csv

def update_data():
    csv = pd.read_csv(path)
    while True:
        try:
            row_index = int(input("Enter the row: "))-1
            print("1.Equipment Name 2.Type 3.Primary Use 4.Power Source 5.Availability 6.Price(BDT)")
            column_list = [" ","Equipment Name","Type","Primary Use","Power Source","Availability","Price(BDT)"]
            column_index = int(input("Enter what do you want to change: "))
            if column_index <= len(column_list):
                new_value = input("Enter New Value: ")
                csv.loc[row_index, column_list[column_index]]= new_value
                csv.to_csv(path, index=False)
                print("")
                print("Data Updated Successfully!!!")
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Invalid Input!!!")
            continue
    return csv

def clear_data():
    csv = pd.read_csv(path)
    while True:
        try:
            row_index = int(input("Enter the row: "))-1
            print("1.Equipment Name 2.Type 3.Primary Use 4.Power Source 5.Availability 6.Price(BDT)")
            column_list = [" ","Equipment Name","Type","Primary Use","Power Source","Availability","Price(BDT)"]
            column_index = int(input("Enter what do you want to clear: "))
            if column_index <= len(column_list) and column_index > 0:
                csv.loc[row_index, column_list[column_index]]= " "
                csv.to_csv(path, index=False)
                print("")
                print("Data Cleared Successfully!!!")
                break
            else:
                print("Invalid Input!!!")
                continue
        except ValueError:
            print("Invalid Input!!!")
            continue
    return csv

def delete_inventory():
    csv = pd.read_csv(path)
    empty_columns = csv.columns
    empty_csv = pd.DataFrame(columns=empty_columns)
    empty_csv.to_csv(path, index=False)
    print("")
    print("Inventory Cleared Successfully!!!")
    return empty_csv

def show_inventory():
    csv = pd.read_csv(path)
    print("")
    print(csv)

def esc_button(event):
    if event.key == "escape":
        plt.close()

def bar_chart():
    csv = pd.read_csv(path)
    prices = csv["Price(BDT)"]
    min_price = csv["Price(BDT)"].min()
    max_price = csv["Price(BDT)"].max()
    norm = (prices - min_price) / (max_price - min_price)
    alphas = 0.5 + 0.5*norm
    colour_code = []
    for alpha in alphas:
        colour_code.append((1,0,0,alpha))
    ref = csv.plot.bar(y="Price(BDT)", color=colour_code, legend=False)
    ref.set_xticks(range(len(csv)))
    ref.set_xticklabels(range(1, len(csv)+1), rotation=0)
    ref.set_title("Equipment Vs Price(BDT) Graph")
    i = 0
    for i in range(len(csv)):
        print(i+1, csv["Equipment Name"][i])
    ref.set_xlabel("Equipments", fontsize=10)
    ref.set_ylabel("Price(BDT)", fontsize=10)
    plt.gcf().canvas.mpl_connect("key_press_event", esc_button)
    plt.tight_layout()
    plt.show()

def pie_chart():
    csv = pd.read_csv(path)
    titles = pd.Series(csv["Equipment Name"])
    prices = pd.Series(csv["Price(BDT)"])
    plt.pie(prices, labels=titles)
    plt.gcf().canvas.mpl_connect("key_press_event", esc_button)
    plt.show()

while True:
    print("")
    print("Welcome to Farm Inventory Management System")
    print("")

    try:
        print("1.Create List 2.Clear List 3.Update Data 4.Clear Data 5.Delete Inventory 6.Show Inventory 7.Price Chart")
        user = int(input("Enter what do you want to do: "))
        if user == 1:
            create_list()
        elif user == 2:
            clear_list()
        elif user == 3:
            update_data()
        elif user == 4:
            clear_data()
        elif user == 5:
            delete_inventory()
        elif user == 6:
            show_inventory()
        elif user == 7:
            while True:
                try:
                    chart = int(input("1.Bar Chart or 2.Pie Chart: "))
                    if chart == 1:
                        bar_chart()
                        break
                    elif chart == 2:
                        pie_chart()
                        break
                    else:
                        print("Invalid Input!!!")
                        continue
                except ValueError:
                    print("Invalid Input!!!")
                    continue
        else:
            print("Invalid Input!!!")
            continue
    except ValueError:
        print("Invalid Input!!!")
        continue
