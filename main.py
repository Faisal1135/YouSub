import pyautogui as pg

pg.sleep(4)

pg.PAUSE = 3
P_SIGN_IN = (1274, 150)
P_EMAIL = (543, 413)
P_NEXT = (834, 601)
P_RECOVER = (614, 522)
P_NOT_NOW = (549, 639)
P_CONFIRM = (799, 688)
P_URLBAR = (203, 69)


def sign_in_google(email: str, password: str, recover_email: str):
    pg.click(P_SIGN_IN)
    pg.sleep(4)
    pg.click(P_EMAIL)
    pg.write(email)
    pg.press('enter')
    pg.sleep(4)
    pg.write(password)
    pg.press('enter')
    pg.click(P_RECOVER)
    pg.write(recover_email)
    pg.press('enter')
    pg.sleep(5)
    pg.click(P_NOT_NOW)

    # pg.click(P_CONFIRM)
    pg.click(18, 73)
    pg.sleep(4)


pg.click(P_URLBAR)
pg.write("https://www.youtube.com/channel/UCCCZQP_CkDl1UtGi21BAE7Q")
pg.press('enter')
# pg.hotkey('ctrl', 'I')

# name = pg.prompt("Enter your name")
# print(name)
# sign_in_google("harlodbrwer2490@gmail.com", "444FFFyyy",
#                "aiwvtemabsx1874@gmail.com")
# (815,684)

# harlodbrwer2490@gmail.com	444FFFyyy	aiwvtemabsx1874@gmail.com
# patsyadams9011@gmail.com	VVVbbb777	najsoutafrew1753@gmail.com
# lilliannguyen6032@gmail.com	kkkPPP999	alsutremanzfo1864@gmail.com
# nathanprobertson1863@gmail.com,
# while True:
#     print(pg.position())
# pg.sleep(5)

# pg.click(1274, 150)  # sign in co-ordinet
# 543,413    834,601
