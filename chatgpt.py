import openai
import argparse

YOUR_API_KEY =  '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'

def chatGPT(prompt, API_KEY=YOUR_API_KEY):
    openai.api_key = API_KEY

    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 2**10,
        top_p =1,
        frequency_penalty =0,
        presence_penalty =0
        )
    ret = completion['choices'][0]['text']
    return ret

if __name__ == "__main__":
    prompt = input("사용자:")
    completion = chatGPT(prompt).strip()
    print(f"chtGPT : {completion}")
