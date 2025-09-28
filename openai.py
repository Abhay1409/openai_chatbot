from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''

#copy your text history here that you want to analyze.




'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Abhay who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Abhay"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)