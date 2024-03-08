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
    
    def get_userAgent(self, model, PrototypeUserAgent):
        messages = [
            {"role": "system", "content": f"{PromtUserAgent}"},
            {"role": "user", "content": PrototypeUserAgent}
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
    
    
    