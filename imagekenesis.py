import tkinter as tk
from tkinter import ttk

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Imagekenesis")
        self.geometry('640x360')
        self.minsize(640, 360)
        container = tk.Frame(self, height=640, width=360)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Startup, Processing, Completion):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.display_frame(Startup)

    def display_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Startup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        inner_frame = tk.Frame(self, bg='#f21212')
        inner_frame.pack(fill='both', expand=True,)
        center_frame = tk.Frame(inner_frame, bg='#202020')
        center_frame.pack(side="left", fill="both", expand=1, padx=10, pady=10)

        title = tk.Label(
            center_frame,
            text="Welcome to Imagekenesis!",
            bg='#202020',
            fg='white',
            font=("Arial", 25) 
        )
        
        subtitle = tk.Label(
            center_frame,
            text="by willxw",
            bg='#202020',
            fg='white'
        )

        title.pack(padx=20, pady=20)
        subtitle.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            center_frame,
            text="Open Image",
            command=lambda: controller.display_frame(Processing),
            highlightbackground='#202020'
        )

        switch_window_button.pack(padx=20, pady=20)



class Processing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        inner_frame = tk.Frame(self, bg='#121212')
        inner_frame.pack(fill='both', expand=True,)

        left_frame = tk.Frame(inner_frame, bg='#202020')
        right_frame = tk.Frame(inner_frame, bg='#202020')

        left_frame.pack(side="left", fill="both", expand=1, padx=10, pady=10)
        right_frame.pack(side="right", fill="both", expand=1, padx=10, pady=10)


class Completion(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()