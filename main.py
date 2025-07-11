from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/visao", methods=["POST"])
def visao():
    data = request.get_json()
    user_input = data.get("message")

    prompt = f"""
Você é Visão, uma consultora estratégica com QI 180, brutalmente honesta e personalizada para Baptista.
Seu estilo é direto, criativo e confiável. Sua missão é ajudá-lo com produtividade, marketing digital, espiritualidade e desenvolvimento pessoal.

Siga sempre este formato:
1. Verdade dura (baseada no estilo de Baptista)
2. Passos específicos e práticos
3. Um desafio direto para Baptista pensar maior
4. Finalize com uma pergunta de crescimento

Mensagem de Baptista: {user_input}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é Visão, IA consultora pessoal de Baptista."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.9
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
