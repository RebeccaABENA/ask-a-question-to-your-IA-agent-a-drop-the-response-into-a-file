import openai
import pandas as pd
import time
from IPython.display import display

api_key = "Your API KEY"
if not api_key:
    raise ValueError("KEY IS NOT FOUND ")
openai.api_key = api_key

prompt = 'YOUR REQUEST'

def generation_reponse(prompt):
    start_time = time.time()
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompte,
            max_tokens=100
        )
        end_time = time.time()
        duration = end_time - start_time

        return {
            "Réponse": response["choices"][0]["message"]["content"].strip(),
            "Temps (s)": round(duration, 2)
        }
    except Exception as e:
        print(f"ERROR OF SYSTEM : {e}")

result = generation_reponse(prompt)

df_results = pd.DataFrame([result])
display(df_results)

df_results.to_csv("NAMEOFYOURFILE.CSV", index=False)
print("YOU CAN FIND THE RESULT OF YOUR REQUEST INTO YOUR FILE")
