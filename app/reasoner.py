import os
import json

from dotenv import load_dotenv
from groq import Groq

from app.search import search

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "openai/gpt-oss-120b"


def classify_question(question):
    results = search(question, top_k=5)

    if not results:
        return {
            "classification": "NOT COVERED",
            "answer": "The rulebook does not contain sufficient information to answer this question.",
            "evidence": []
        }

    evidence_text = ""

    for i, result in enumerate(results, start=1):
        evidence_text += (
            f"\n--- Evidence {i} ---\n"
            f"Section: {result['title']}\n"
            f"Similarity: {result['score']:.4f}\n"
            f"Text:\n{result['text']}\n"
        )

    prompt = f"""
You are a strict Rulebook QA system.

The rulebook is the ONLY source of truth.

You MUST reason ONLY from the provided evidence.
Do NOT use outside knowledge.
Do NOT invent rules.

Classify the question into exactly one of:

ANSWERED
NOT COVERED
CONFLICT

Definitions:

ANSWERED:
The evidence contains enough information to answer the question.

NOT COVERED:
The evidence does not contain a rule that answers the question.

CONFLICT:
The evidence contains two or more contradictory rules that apply to the question.

Important:
If two rules give different requirements, limits, deadlines, permissions,
or outcomes for the same situation, classify it as CONFLICT.

Return ONLY valid JSON in this format:

{{
  "classification": "ANSWERED | NOT COVERED | CONFLICT",
  "answer": "short answer based only on the evidence",
  "citations": [
    {{
      "section": "section title",
      "similarity": 0.0000
    }}
  ]
}}

Question:
{question}

Retrieved Evidence:
{evidence_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    raw_response = response.choices[0].message.content.strip()

    try:
        result = json.loads(raw_response)
    except json.JSONDecodeError:
        result = {
            "classification": "NOT COVERED",
            "answer": raw_response,
            "citations": []
        }

    result["evidence"] = results

    return result


if __name__ == "__main__":
    question = input("\nEnter your question: ")

    result = classify_question(question)

    print("\nClassification:")
    print(result["classification"])

    print("\nAnswer:")
    print(result["answer"])

    print("\nCitations:")

    for citation in result.get("citations", []):
        print(
            f"- {citation['section']} "
            f"(similarity: {citation['similarity']:.4f})"
        )