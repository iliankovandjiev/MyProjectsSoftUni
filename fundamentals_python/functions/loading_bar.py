def loading_bar(number):
    percent_complete = number // 10
    if percent_complete == 10:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f"{percent_complete}0% [{percent_complete * '%'}{(10 - percent_complete) * '.'}]")
        print('Still loading...')


integer_number = int(input())
loading_bar(integer_number)
