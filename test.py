import openai
import io
openai.api_key = "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"

adda= openai.Completion.create(
    model = "text-davinci-003",
    prompt = "who is modi",
    max_tokens = 4000,
    temperature = 0
)
# print(adda)

print(adda.choices[0].text)