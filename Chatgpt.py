import openai

openai.api_key = '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'

file_path = r'C:\Users\mukil\Downloads\chat_gpt_article.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    information = file.read()

test = True
while test:

# Ask a question
    question = input("Ask a question (enter q to quit): ")

    if (question == "q"):
        test = False

    else:
# Combine the information and the question
        prompt = information + '\nQuestion: ' + question

# Send the prompt to ChatGPT
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=500
        )

# Get the answer from the response
        answer = response.choices[0].text.strip()

# Print the answer
        print(answer)




