import json
from openai import OpenAI
from langchain.chat_models import ChatOpenAI, openai

TEST_OPENAI_API_KEY = "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"


def get_llm_response(user_prompt, system_prompt):
    client = OpenAI(
        api_key=TEST_OPENAI_API_KEY,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    return completion.choices[0].message.content

    # here should be a movie script generator, but here is a hardcoded example

def generate_movie_script(prompt, universe):
    script = ""
    for scene_number, scene_name in universe.items():
        dialogue = generate_dialogue(scene_number, scene_name, prompt)
        script += f"'Location {scene_number}: {scene_name}'\n"
        script += f"'Persona: {', '.join(characters.values())}'\n\n"
        script += dialogue + "\n\n"
    return script

def generate_dialogue(scene_number, scene_name, prompt):
    prompt = f"Location {scene_number}: {scene_name}\n{prompt}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    dialogue = response.choices[0].text.strip()
    return dialogue

    # Определение персонажей и вселенной
characters = {
        "Tom": "Tom",
        "Leo": "Leo",
        "Elizabeth": "lizabeth",
        "Nargul": "Nargul",
        "Lora": "Lora"
}

universe = {
    1: "Meeting in the forest",
    2: "Meeting with Nargul",
    3: "Search for a kitten",
    4: "Meeting with Lora",
    5: "Returning home"
}

if __name__ == "__main__":
    prompt = "Elizabeth: Something's bothering me..."

generated_script = generate_movie_script(prompt, universe)
print(generated_script)
