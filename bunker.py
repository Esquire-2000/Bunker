import colorama
from colorama import Fore,Back,Style
colorama.init()
totalClasses = int(input('Total Classes: '))
attendance = int(input('Classes Attended: '))
percentage = (attendance * 100) // totalClasses
print(Fore.YELLOW+'Percentage: %d%%' % percentage+Style.RESET_ALL)
if not percentage >= 75:
    attendClasses = 0
    while not percentage >= 75:
        totalClasses += 1
        attendance += 1
        attendClasses += 1
        percentage = (attendance * 100) // totalClasses
    print(Fore.RED+'Attend next %d classes to get back on track' % attendClasses+Style.RESET_ALL)
else:
    classesYouCanMiss = 0
    while percentage > 75:
        classesYouCanMiss += 1
        attendance -= 1
        percentage = (attendance * 100) // totalClasses
    if (classesYouCanMiss==1 or classesYouCanMiss==0):
        print(Fore.CYAN+'You can\'t miss the next class'+Style.RESET_ALL)

    else:
        print(Fore.GREEN+'You can bunk the next %d classes.' % classesYouCanMiss+Style.RESET_ALL)

