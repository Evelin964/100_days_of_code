import tkinter as tk
import pandas as pd
import random
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
BACK_IMAGE_PATH = "31.Day_31/images/card_back.png"
FRONT_IMAGE_PATH = "31.Day_31/images/card_front.png"
RIGHT_IMAGE_PATH = "31.Day_31/images/right.png"
WRONG_IMAGE_PATH = "31.Day_31/images/wrong.png"



class FlashCard():
    def __init__(self) -> None:
        self.ui_setup()
        self.read_data()
        
        self.text_item = None
        self.card_face = "back"
        self.word_dict = {}
        self.is_running = False
       
        self.correct_flag = False
        self.flip_card_event_id = None
        random.seed(42) 
        
        self.missed_words = []
        self.correct_words = []
        
       
        
    
    
    def ui_setup(self):
        self.window = tk.Tk()
        self.window.title("Flash Card")
        self.window.resizable(False, False)
        self.window.geometry("800x600")
        
        
        
        self.create_back_image()
        self.create_front_image()
        self.create_right_image()  
        self.create_wrong_image()  
        
        self.create_canvas()
        
        
        # # Bind functions to the images
        self.canvas.tag_bind(self.right_image_item, "<Button-1>", self.right_image_clicked)
        self.canvas.tag_bind(self.wrong_image_item, "<Button-1>", self.wrong_image_clicked)
        
    def create_canvas(self):
        self.canvas = tk.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
        
        self.card_image_item = self.canvas.create_image(400, 300, image=self.back_image)  # Center the image at (400, 300)
       
        self.canvas.grid(column=0, row=0)
        
        self.right_image_item = self.canvas.create_image(600, 540, image=self.right_image)  # Add right image to canvas
        self.wrong_image_item = self.canvas.create_image(200, 540, image=self.wrong_image)  # Add wrong image to canvas
        
    def flip_card(self):
        
        if len(self.word_dict) == 0:
            
            if len(self.data) == 0:
                self.card_timer()
                return
    
            self.feed_new_word()
        
        self.decide_card_face()
        self.card_timer()

    def decide_card_face(self):        
        if self.card_face=="back":
            self.canvas.itemconfig(self.card_image_item, image=self.back_image)
            self.update_text(self.word_dict['back'])
            del self.word_dict['back'] 
            self.card_face = "front"
        elif self.card_face=="front":
            self.canvas.itemconfig(self.card_image_item, image=self.front_image)
            self.update_text(self.word_dict["front"])
            del self.word_dict['front'] 
            self.card_face = "back"
       
    def feed_new_word(self):    
        self.current_index = random.randint(0, len(self.data)-1) 
        self.word_choice = self.data[self.current_index]
        
        self.word_dict = {'back':self.word_choice["French"], 
                    'front': self.word_choice["English"]}
        
        self.canvas.itemconfig(self.card_image_item, image=self.back_image)
        self.card_face = "back"
    
    def missed_words_action(self):
        if self.word_choice not in self.missed_words:
            self.missed_words.append(self.word_choice)
        if self.word_choice in self.data:
            self.data.remove(self.word_choice)
        self.restart_action()
        self.word_dict = {}
        self.canvas.itemconfig(self.card_image_item, image=self.back_image)
        self.update_text("")
        self.flip_card()         
                   
    def correct_card_action(self):
        if self.word_choice not in self.correct_words:
            self.correct_words.append(self.word_choice)
        if self.word_choice in self.data:
            self.data.remove(self.word_choice)
        self.restart_action()
        self.word_dict = {}
        self.canvas.itemconfig(self.card_image_item, image=self.back_image)
        self.update_text("")
        self.flip_card()
        
    def restart_action(self):
        if self.flip_card_event_id:
            self.window.after_cancel(self.flip_card_event_id)
            self.flip_card_event_id = None
                
    def card_timer(self):
        self.is_running = True
        if len(self.data)>0:
            
            self.flip_card_event_id = self.window.after(3000, self.flip_card)
        else:
            if len(self.correct_words) == self.nr_of_words:
               
                self.is_running = False
                self.canvas.itemconfig(self.card_image_item, image=self.back_image)
                self.update_text("You have learned all the words")
            else:
                print("You extend the list now")
                self.data.extend(self.missed_words)
                print(f'The self_data list is now after extenxion: {self.data}')
                self.missed_words = []
                self.flip_card()
                          
    def read_data(self):
        data = pd.read_csv("31.Day_31/data/french_words.csv")
        self.data = data.to_dict(orient="records") # -> a list of dicts
        self.nr_of_words = len(self.data)
          
    def create_right_image(self):
        right_image = Image.open(RIGHT_IMAGE_PATH)
        right_image = right_image.resize((70, 70))
        self.right_image = ImageTk.PhotoImage(right_image)
        
    def create_wrong_image(self):
        wrong_image = Image.open(WRONG_IMAGE_PATH)
        wrong_image = wrong_image.resize((70, 70))
        self.wrong_image = ImageTk.PhotoImage(wrong_image)
        
    def create_back_image(self):
        back_image = Image.open(BACK_IMAGE_PATH)
        back_image = back_image.resize((600, 400))  # Resize location
        self.back_image = ImageTk.PhotoImage(back_image)
    
    def create_front_image(self):
        front_image = Image.open(FRONT_IMAGE_PATH)
        front_image = front_image.resize((600, 400))  # Resize location
        self.front_image = ImageTk.PhotoImage(front_image)
        
    def right_image_clicked(self, event):
        if not self.is_running:

            if self.nr_of_words == 101:
                self.flip_card()  
        else:
            self.correct_flag = True
            self.correct_card_action()
            
    def wrong_image_clicked(self, event):
        if self.is_running:
            self.correct_flag = False
            self.missed_words_action()
                  
    def update_text(self, text):
        if hasattr(self, 'text_item'):
            # Update the existing text item
            self.canvas.itemconfig(self.text_item, text=text)
        else:
            # Create a new text item and store its reference
            self.text_item = self.canvas.create_text(400, 300, text=text, font=("Arial", 40, "bold"))

        
        
        

        
    
        
        


if __name__ == "__main__":
    flash_card = FlashCard()
    
    flash_card.window.mainloop()
    
    
