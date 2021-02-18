import tkinter
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    window = Tk()
    window.geometry("500x500")
    window.title("BIU inbar auto grades")

    biuphoto = PhotoImage(file="BIULOGO.png")
    photo = Label(window, image=biuphoto, bg="black").grid(row=0, column=0, sticky=W, pady=2, columnspan=5, rowspan=2)
    tkinter.Label(window, text="Id").grid(row=3, column=0, sticky=W, pady=2)
    tkinter.Label(window, text="Password").grid(row=4, column=0, sticky=W, pady=2)
    e1 = tkinter.Entry(window)
    e2 = tkinter.Entry(window, show="*")
    e1.grid(row=3, column=1, sticky=W, pady=2)
    e2.grid(row=4, column=1, sticky=W, pady=2)

    def buttonClick():
        id = e1.get()
        pwd = e2.get()
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        chromedriver = "c:/Users/cellium/Downloads/chromedriver.exe"
        driver = webdriver.Chrome(chromedriver, options=op)
        driver.get("https://inbar.biu.ac.il/Live/Login.aspx")
        driver.implicitly_wait(1)
        driver.find_element_by_name("edtUsername").send_keys(id)
        driver.find_element_by_name("edtPassword").send_keys(pwd)
        driver.find_element_by_css_selector("#btnLogin").click()
        driver.implicitly_wait(1)
        driver.find_element_by_css_selector("#tvMainn7").click()
        driver.find_element_by_css_selector("#tvMainn7Nodes > table:nth-child(2)").click()
        table_id = driver.find_element(By.ID, 'ContentPlaceHolder1_gvGradesList')
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        list = []
        for row in rows[1:]:
            td = row.find_elements(By.TAG_NAME, "td")
            if len(td) > 6 and td[6].text != '':
                course = td[1].text
                grade = td[6].text
                list.append((course, grade))
        total_rows = len(list)
        total_columns = len(list[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(window, width=20, fg='blue',
                          font=('Arial', 13, 'bold'))
                e.grid(row=i + 8, column=j)
                e.insert(END, list[i][j])

    button1 = tkinter.Button(window, text="submit", command=buttonClick)
    button1.grid(columnspan=2, row=5, column=0)
    window.mainloop()


if __name__ == '__main__':
    main()
