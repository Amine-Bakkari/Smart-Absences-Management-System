from  customtkinter import * 


# +++++++++++++++++++++++++++Main Window+++++++++++++++++++++++++++

app=CTk()
app.geometry("600x500+400+95")
app.title("Absences Review (For Students)")
app._set_appearance_mode("system")

#+++++++++++ Frames +++++++++++++    

PobFrame=CTkFrame(app,
                  width=580,
                  height=20,
                  corner_radius=10)
PobFrame.place(x=10, y=10)

FrameNUM1=CTkFrame(app,
          width=200,
          height=280,
          corner_radius=10)
FrameNUM1.place(x=10, y=40)

FrameNUM2=CTkFrame(app,
          width=370,
          height=280,
          corner_radius=10)
FrameNUM2.place(x=220, y=40)

FrameNUM3=CTkFrame(app,
          width=580,
          height=150,
          corner_radius=10)       
FrameNUM3.place(x=10, y=330)



app.mainloop()