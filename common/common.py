def checkEmpty(str):
    if str.replace(" ", "") == '':
        return True #Chuỗi rỗng trả về đúng
    return False #Nếu không thì trả về sai


def checkNumber0to1(number):
    if 0 <= number <= 1:
        return True  #Nếu số nằm trong khoảng từ 0 tới 1 thì trả về đúng, nếu không trả về sai
    return False