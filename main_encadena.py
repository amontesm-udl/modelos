from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Cargar API Key de Gemini desde .env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

texto= "NotebookLM es una herramienta de investigación y escritura basada en IA que te ayuda a resumir y extraer información de fuentes densas y complejas. Puedes subir archivos PDF, Documentos de Google, Presentaciones de Google, URL de sitios web y más para crear un cuaderno con diversas fuentes."
# Crear prompt template
prompt = PromptTemplate(
    input_variables=["texto"],
    template="Resume el siguiente texto: {texto}"
)

# Inicializar Google Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # o gemini-pro, según tu API
    temperature=0.7
)

resultado = (prompt | llm).invoke({
    "texto": texto
})

# Solo mostrar el contenido
print("Resumen:", resultado.content)