from customtkinter import *

MainWindow = CTk()
MainWindow.geometry("400x300")

def Show():
    # OtherWindow = CTkToplevel(MainWindow)
    # OtherWindow.geometry("300x200+100+100")
    # # OtherWindow.attributes('-topmost', True)
    # Label = CTkLabel(OtherWindow, text="Hello from the other window!")
    # Label.pack(pady=20)
    # OtherWindow.mainloop()
    # MainWindow.clipboard_append(entry.get())
    # selection = MainWindow.selection_get()
    # print("Selection:", selection)
    switch.toggle()
    
def Printwithkey(event):
    Event = event.char
    if Event == "\r":
        # Button.invoke()
        switch.toggle()
        



Button = CTkButton(MainWindow, text="Click Me", command=Show)
Button.pack(pady=20)
MainWindow.bind_all("<Key>", Printwithkey)
# tabview = CTkTabview(MainWindow, width=300, height=200)
# tabview.add("Tab 1")
# tabview.add("Tab 2")
# tabview.pack(pady=10)

# Button1 = CTkButton(tabview.tab("Tab 1"), text="Button in Tab 1")
# Button1.pack(pady=10)
# entry2 = CTkEntry(tabview.tab("Tab 2"), placeholder_text="Entry in Tab 2")
# entry2.pack(pady=10)

# scrollableframe = CTkScrollableFrame(MainWindow, width=300, height=100)
# scrollableframe.pack(pady=10)

# for i in range(100):
#     label = CTkLabel(scrollableframe, text=f"Label {i+1}")
#     label.pack(pady=5)

entry = CTkEntry(MainWindow, placeholder_text="Type here...")
entry.pack(pady=10)

switch = CTkSwitch(MainWindow, text="Enable Option")
switch.pack(pady=10)

MainWindow.mainloop()