import json
from dotenv import load_dotenv
from fastapi import FastAPI, Form, HTTPException
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI
from prompt_templates import quiz_generation_template, quiz_result_feedback_template
from typing import Dict

from str_templates.input_templates import RESPONSE_JSON

load_dotenv()

app = FastAPI()

# Initialize LLMs
llm_tutor = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo-0125")
llm_reviewer = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo-0125")

# Define prompt templates
quiz_generation_prompt = PromptTemplate(
    input_variables=["content", "topic", "number", "total_points", "student_details", "response_json"],
    template=quiz_generation_template,
)

quiz_feedback_prompt = PromptTemplate(
    input_variables=["total_points", "score", "wrong_answers", "student_details", "topic"],
    template=quiz_result_feedback_template,
)

# Initialize LLM chains
quiz_chain = LLMChain(llm=llm_tutor, prompt=quiz_generation_prompt, output_key="quiz")
quiz_feedback_chain = LLMChain(llm=llm_reviewer, prompt=quiz_feedback_prompt, output_key="feedback")


@app.post("/generate_quiz")
async def generate_quiz(
        content: str = Form(...),
        topic: str = Form(...),
        number: int = Form(...),
        total_points: int = Form(...),
        student_details: str = Form(...),
) -> Dict:
    try:
        with get_openai_callback() as cb:
            response = quiz_chain.invoke(
                {
                    "content": content,
                    "topic": topic,
                    "number": number,
                    "total_points": total_points,
                    "student_details": student_details,
                    "response_json": json.dumps(RESPONSE_JSON),
                }
            )

        log_usage(cb)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_feedback")
async def get_feedback(
        total_points: int = Form(...),
        score: int = Form(...),
        wrong_answers: str = Form(...),
        student_details: str = Form(...),
        topic: str = Form(...),
) -> Dict:
    try:
        with get_openai_callback() as cb:
            response = quiz_feedback_chain.invoke(
                {
                    "total_points": total_points,
                    "score": score,
                    "wrong_answers": wrong_answers,
                    "student_details": student_details,
                    "topic": topic,
                }
            )

        log_usage(cb)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def log_usage(cb):
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}\n\n")
