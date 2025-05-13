from google import genai

key="AIzaSyCx9IOR6I_xtoyBkybS5-phOWl67ma0osQ"
client = genai.Client(api_key=key)

intput1=input("Enter your prompt: ")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=intput1
)
print(response.text)