from transformers import pipeline

data = {"name": "aditya", "age": 25}

summarizer = pipeline("summarization")

text_to_summarize = input("Please enter the text you want to summarize: ")

summary = summarizer(text_to_summarize, max_length=130, do_sample=False)[0][
    "summary_text"
]

# print("hjGJJJJJJJJJJJJJJJJJJJJJJJJJJJKSJHKkhkdhkjkjiiiiiiiii")

print("\nOriginal Text : ")
print(text_to_summarize)
print("\nSummary:")
print(summary)
