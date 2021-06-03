from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", ):
        return "Hello beep boop"

    if user_message in ("who are you" , ):
        return "I am a Potential Alice Channel!"
    
    if user_message in ("date", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    return "I dont know!!!!"
            