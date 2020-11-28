import pyttsx3 
  
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 
  
engine.save_to_file("Chinmay", "output.mp3")

# say method on the engine that passing input text to be spoken 
engine.say('Hello sir, how may I help you, sir.') 
  
# run and wait method, it processes the voice commands.  
engine.runAndWait() 


# say method on the engine that passing input text to be spoken 
engine.say('Chinmay Osman Shunaiz') 
  
# run and wait method, it processes the voice commands.  
engine.runAndWait() 