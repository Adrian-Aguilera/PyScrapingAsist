from openai import OpenAI

class GetdataGPT:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def get_data(self, model, html_content):
        messages = [
            {"role": "system", "content": "Extrae exclusivamente las clases de las etiquetas <img> y de las etiquetas <div> del siguiente HTML, sin incluir ningún mensaje adicional."},
            {"role": "user", "content": html_content}
        ]

        stream = self.client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

        final_content = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                final_content += chunk.choices[0].delta.content

        return final_content.strip()