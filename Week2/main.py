
#Adding Modules using import

import utils
import greetings
#from greetings import hello

import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    utils.print_hi('PyCharm')
    utils.hello()
    greetings.hello()
    print(greetings.student1)
    print(greetings.student1["first_name"])

    # Playing with datetime library
    today = datetime.datetime.today()
    print(today)
    print(today.month)
    print(today.year)
    detail_today = datetime.datetime.now()
    print(detail_today)



