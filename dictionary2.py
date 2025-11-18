#Import Library
import datetime #untuk format birthdate/date joined
#Dictionary template 
teacher_template = {
    'name' :'name',
    'subject' :'subject',
    'datejoined': datetime.datetime(2020,11,11)
}
data_teacher = {}
while True:
    print(f"{'Teacher SCS':^20}")
    print("="*30)
    teacher = dict.fromkeys(teacher_template.keys())
    teacher['name'] = input("Input Name:")
    teacher['subject'] = input("Input Subject:")
    year = int(input("Year:"))
    month = int(input("Month:"))
    date = int(input("Date:"))
    teacher['datejoined'] = datetime.datetime(year,month,date)
    print(f"{'name':<20} {'subject':<20} {'datejoined':<20}")
    print("="*20)
    for b in data_teacher:
        nama = data_teacher['name']
        mapel = data_teacher['subject']
        tanggal = data_teacher['datejoined']
        print(f"{nama:<20} {mapel:<20} {tanggal:`<20}")
    print("\n")
    option = input("Continue (Y/N)?")
    if option =="N":
        break
print("Finish Thank You")