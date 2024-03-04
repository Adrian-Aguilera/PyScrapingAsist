from openai import OpenAI

class GetdataGPT:
    def __init__(self, api_key, promt=None):
        self.client = OpenAI(api_key=api_key)
        self.Promt = promt
        
    def get_data(self, model, html_content):
        messages = [
            {"role": "system", "content": f"{self.Promt}"},
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
    
    def UserAgent(self):
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'