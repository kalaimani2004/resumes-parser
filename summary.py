import ollama

def experience_summary(experience_text):
    prompt = f"Summarize the following professional experience in 2 lines:\n\n{experience_text}"
    response = ollama.chat(
        model='llama3',  # Make sure you've pulled this model: `ollama run llama3`
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()
