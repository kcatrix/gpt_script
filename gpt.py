import openai

openai.api_key = "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"

def generate_response(prompt):
        completions = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
        )

        message = completions.choices[0].text
        return message

print("Bonjour, je suis ChatGPT, comment puis-je vous aider aujourd'hui ?")
while True:
    question = input("Vous : ")
    if question == "stop":
            print("ChatGPT : Au revoir, à bientôt !")
            break
    else:
        response = generate_response(question)
        print("ChatGPT : " + response)