import openai

openai.api_key = "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"

#recepe_generator()
ingredients = []

while True:
    ingradient = input("Please Enter Ingredients. Enter done once its complete.")
    if ingradient.lower() == "done":
        break

    ingredients.append(ingradient)

def recepe_generator(ingradients):
    message = []

    for ingredient in ingredients:
        message.append({"role":"user", "content":ingredient})
     
    message.extend(
          [{"role" : "system", "content" : "direct, point"},
           {"role" : "assistent", "content" : "you are high end chef. You are generate a receipe in given ingredients"}]
      )

    response = openai.ChatCompletion.create(
       model = "gpt-4o",
       message = message,
       max_tokens = 300,
       temperature = 0.9
    )
    return response.choices[0].messages.content

print(recepe_generator(ingredients))
