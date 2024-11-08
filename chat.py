import os
import google.generativeai as genai

genai.configure(api_key="GEMENI_API_KEY")##put you gemeni api key here##


generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Act like you Are a doctor",
)
history=[]
print("Bot: Hello , how can i help you ?")
while True:
    user_input = input("You: ")
                    
    chat_session = model.start_chat(
                history=history
                    
                )

    response = chat_session.send_message(user_input)

    model_response= response.text
    print(f'Bot: {model_response}')
    print()
    history.append({"role":"user","parts":[user_input]})
    history.append({"role":"model","parts":[model_response]})           