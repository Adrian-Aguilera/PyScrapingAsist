from openai import OpenAI
from GetdataGPT import GetdataGPT


key = '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'
model = "gpt-3.5-turbo"
html_content = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Clases de imágenes</title>
</head>
<body>
  <img src="example1.jpg" class="image-rounded test25">
  <img src="example2.jpg" class="image-thumbnail test4">
  <div class="gallery">
    <img src="example3.jpg" class="image-gallery test3">
  </div>
  <img src="example4.jpg" class='test-imagen test2'>
  <div class="gallery-5465">
    <img src="example3.jpg" class="image-Api test52">
  </div>
</body>
</html>

'''
gpt = GetdataGPT(key)

print(f'las clases son: {gpt.get_data(model, html_content)}')