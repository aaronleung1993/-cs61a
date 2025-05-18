import ollama
m = 'gemma3:4b-it-qat'  # a small model

prefix = 'Oski the Bear is the official'
output = ollama.generate(model=m, prompt=prefix, raw=True)
print(output.response)

t = ollama.generate(model=m, prompt=prefix, raw=True, stream=True)
next(t).response

[next(t).response for _ in range(20)]

from IPython.display import display, Markdown, Latex
instruction = "Write a Python generator function that yields infinite odd numbers starting at 3."
output = ollama.generate(model=m, prompt=instruction)
display(Markdown(output.response))
