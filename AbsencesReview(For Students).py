from  customtkinter import * 


# +++++++++++++++++++++++++++Main Window+++++++++++++++++++++++++++

app=CTk()
app.geometry("600x500+400+95")
app.title("Absences Review (For Students)")
app._set_appearance_mode("system")

#++++++++++++++++++++++++++ Frame ++++++++++++++++++++++++++++
frame1=CTkFrame(app,
                  width=580,
                  height=480,
                  corner_radius=10,
                  fg_color="#B8F5DE",
                  border_width=2,
                  border_color="#9EF1D1"
                  )
frame1.place(x=10,y=10)


#+++++++++++ Entry and lebls  +++++++++++++
Entery1=CTkEntry(app,
                  width=300,
                  height=30,
                  placeholder_text="Enter Student ID",
                  corner_radius=10,
                  fg_color="white",
                  )
Entery1.place(x=175,y=100)    

Entery2=CTkEntry(app,
                  width=300,
                  height=  30,
                  placeholder_text="Enter Student paassword", 
                  corner_radius=10,
                  fg_color="white",
                  )
Entery2.place(x=175,y=145)




app.mainloop()