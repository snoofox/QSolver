import os
import re
import json
import asyncio
from ollama import AsyncClient

# CONFIG
OLLAMA_HOST = "OLLAMA_ENDPOINT"
CACHE_FILE = "cache.json"
INPUT_FILE = "questions.txt"
OUTPUT_FILE = "answers.md"


# Cache handling functions
def load_cache():
    if not os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'w') as fp:
            json.dump([], fp)
    with open(CACHE_FILE, 'r') as fp:
        return json.load(fp)


def save_cache(cache):
    with open(CACHE_FILE, 'w') as fp:
        json.dump(cache, fp)


async def get_gpt_solution(question):
    system_prompt = (
        "Please provide a concise yet comprehensive answer to the following question,"
        "ensuring it is easy to memorize and understand. Always answer with Markdown formatting."
        "You will be penalized if you do not answer with Markdown when it would be possible."
        "Do not use headings (e.g., #, ##, ###) in your answer."
    )

    client = AsyncClient(host=OLLAMA_HOST)
    response = await client.chat(
        model="llama3",
        messages=[
            {'role': 'system', 'content': system_prompt},
            {"role": "user", "content": question }
        ],
    )

    return response['message']['content']


async def main():
    cache = load_cache()

    with open(INPUT_FILE) as fp:
        questions = fp.readlines()

    questions = [q.strip() for q in questions]

    for i, question in enumerate(questions):
        if i in cache:
            print(f"Question {i} already answered. Skipping.")
            continue

        solution = await get_gpt_solution(question)
        formatted_solution = f"-> {solution}\n\n<br />\n\n"

        with open(OUTPUT_FILE, 'a') as fp:
            fp.write(f"## {question}\n\n{formatted_solution}")

        cache.append(i)
        save_cache(cache)


if __name__ == '__main__':
    asyncio.run(main())
