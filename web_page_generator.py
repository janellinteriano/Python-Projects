import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master.geometry('{}x{}'.format(950,200))

        self.varCustom = StringVar()

        self.userText = Label(self.master, text="Enter custom text ot click the Default HTML page button", font=('Helvetica', 13))
        self.userText.grid(row=0, column=2, padx=(25, 26), pady=(30, 0))
        
        self.input= Entry(self.master, text=self.varCustom, font=('Helvetica', 13), width=80)
        self.input.grid(row=2, column=2, columnspan=5, padx=(25, 25), pady=(25, 25))

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=6, column=5, padx=(0, 10), pady=(0, 0))

        self.user_btn = Button(self.master, text="Submit Custom", width=30, height=2, command=self.UserHTMLText)
        self.user_btn.grid(row=6, column=6, padx=(0, 10), pady=(0, 0))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # my function for allowing user input and displaying in new browser
    def UserHTMLText(self):
        userInput = self.varCustom.get() # gets user input as string value
        userFile = open("index.html", "w")
        userContent = "<html>\n<body>\n<h1>" + userInput + "</h1>\n</body>\n</html>" # displays text in the body of html file
        userFile.write(userContent)
        userFile.close()
        webbrowser.open_new_tab("index.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
