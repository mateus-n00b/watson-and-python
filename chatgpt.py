import openai
openai.api_key = "<YOUR API KEY>"

def answer(text: str):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=[{"role": "user", "content": text}]
    )
    print(completion)
    return completion['choices'][0]['message']['content']
