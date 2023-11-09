
#my libraries

from translate import Translator
import tkinter as tk

#additional features (if I have time)

#text to speech using google text to speech library
#clearing the field clear button
#gttts synthesis
#dictionary lookup functionality
#a sound when successful or unsuccessful


# Create the main application window
app = tk.Tk()
app.title("WordBang!")

app.option_add('*Font', 'Courier 18')

# Customized Heading
heading_label = tk.Label(app, text="Welcome to WordBang! An app where you can translate and keep track of your Korean vocabulary!", font=("Impact", 30, "bold"))
heading_label.pack()

#I want history stored in a list
       
translation_history = []

# this is the function that will  handle translation
def translate():
    
    # this is going to get the input entry from the tkinter widget which is the english word we need to translate
    # we will also use the get() method provided by the entry widget, its how we "get" the input from the widget
    #english_word is where the variable is stored when the user inputs a word (so we can use it later)
    english_word = input_entry.get()
    
    #creating a translator class from the "translate" library and establish language parameters
    translator = Translator(to_lang="Korean")
    
    #using the translate method, we pass in the user input
    #the result is stored into the "translation" variable
    translation = translator.translate(english_word)
    
    #this is our label widget where it'll be displayed
    #the config method modifies the widget's text so it updates with the result of the translation
    #remember our translation is store in the translation variable
    #now lets display it
    translation_label.config(text="Korean Translation: " + translation)
    
     #conditional logic for the label widget
    #check for if the translation variable result is EMPTY or not
    if translation:
    # Translation found, display the result!
        translation_label.config(text="Korean Translation: " + translation)
        
# Add the translation to the history list
        translation_history.append((english_word, translation))
    
    # Clear the input field using the delete method
        input_entry.delete(0, 'end')

    # Update the history listbox by calling it
        update_history_listbox()

    else:
    # otherwise if the translation is not found, display a message
       
       translation_label.config(text="Translation not found for: " + english_word)
       




#storing the history inside of the tkinter widget using the listbox which is already in tkinter

history_label = tk.Label(app, text="My WordBang:")
history_label.pack()

history_listbox = tk.Listbox(app)
history_listbox.pack()

#wow now we need a function that will clear the listbox and update it with more!

def update_history_listbox():
    # Clear the history listbox
    history_listbox.delete(0, 'end')
    
    # Update the history listbox with the stored translations
    for english_word, translation in translation_history:
        history_listbox.insert('end', f"{english_word} is {translation}")


       

# Label for instructions for the user
#the pack() method is used to arrange and organize widgets like buttons and entry fields
#its really cool! it adjusts the size of widgets based on the available space in the window!
#tkinter does this from a top down pattern, no need to specify
instruction_label = tk.Label(app, text="Enter an English word to translate:")
instruction_label.pack()

# Entry for user input
input_entry = tk.Entry(app, font=("Courier", 12), bg='orange')
input_entry.pack()


# Button to trigger translation
translate_button = tk.Button(app, text="Translate & Add To My WordBang!", command=translate)
translate_button.pack()

# Label for displaying translation
translation_label = tk.Label(app, text="")
translation_label.pack()

# Start the main event loop (which will start the app!)
app.mainloop()
