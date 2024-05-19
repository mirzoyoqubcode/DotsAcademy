import json
import re

import requests
import streamlit as st

from data import courses


from utils import render_mcq, render_fitb, render_tf

API_URL = "http://161.35.19.77:8080"


@st.cache_data
def generate_questions(content, topic, number, total_points, student_details):
    payload = {
        "content": content,
        "topic": topic,
        "number": number,
        "total_points": total_points,
        "student_details": student_details,
    }

    response = requests.post(f"{API_URL}/generate_quiz", data=payload)
    data = response.json()

    if isinstance(data, dict):
        quiz = data.get("quiz", None)
        if quiz is not None:
            quiz_data = json.loads(quiz)
            questions = []
            for question in quiz_data["questions"]:
                question_type = question["question_type"]
                if question_type == "multiple_choice":
                    questions.append(render_mcq(question))
                elif question_type == "fill_in_the_blank":
                    questions.append(render_fitb(question))
                elif question_type == "true_or_false":
                    questions.append(render_tf(question))
            return questions
    return []


def display_video_with_quiz(video_url, course_name):
    st.video(video_url)


def display_quizzes(course):
    content = course["content"]
    topic = course["name"]
    course_name = course["name"]
    number = 10  # Number of questions to generate
    total_points = 40  # Total points for the quiz
    student_details = "Name: John Doe, Age: 25, Level: Beginner"

    questions = generate_questions(content, topic, number, total_points, student_details)

    if questions:
        st.write("## Quiz")
        for question in questions:
            question_lines = question.strip().split("\n")
            question_type = question_lines[0].split(": ")[1]

            if question_type == "multiple_choice":
                question_text = question_lines[1].split(": ")[1]
                options = [option.strip() for option in question_lines[2:] if option.startswith("-")]
                answer = st.radio(question_text, options, key=f"mcq_{question_text}")

            elif question_type == "fill_in_the_blank":
                question_text = question_lines[1].split(": ")[1]
                st.write(question_text)
                answer = st.text_input("Enter your answer", key=f"fitb_{question_text}")

            elif question_type == "true_or_false":
                question_text = question_lines[1].split(": ")[1]
                answer = st.radio(question_text, ["True", "False"], key=f"tf_{question_text}")

            st.write("---")

        if st.button("Submit Final Test", key=f'submit_test_{course_name}'):
            score = 0
            wrong_answers = []

            for question in questions:
                question_lines = question.strip().split("\n")
                question_type = question_lines[0].split(": ")[1]
                question_text = question_lines[1].split(": ")[1]

                if question_type == "multiple_choice":
                    real_answer = re.search(r"Correct Answer: (.+)", question).group(1)
                    answer = st.session_state[f"mcq_{question_text}"]
                    if answer == f"- {real_answer}":
                        real_score = int(re.search(r"Point Value: (\d+)", question).group(1))
                        score += real_score
                    else:
                        wrong_answers.append(
                            f'Question: {question_text}, Student Answer: {answer}, Correct Answer: {real_answer}')

                elif question_type == "fill_in_the_blank":
                    real_answer = question_lines[2].split(": ")[1].lower()
                    answer = st.session_state[f"fitb_{question_text}"].lower()
                    if answer == real_answer:
                        real_score = int(re.search(r"Point Value: (\d+)", question).group(1))
                        score += real_score
                    else:
                        wrong_answers.append(
                            f'Question: {question_text}, Student Answer: {answer}, Correct Answer: {real_answer}')

                elif question_type == "true_or_false":
                    real_answer = question_lines[2].split(": ")[1].lower()
                    answer = st.session_state[f"tf_{question_text}"].lower()
                    if answer == real_answer:
                        real_score = int(re.search(r"Point Value: (\d+)", question).group(1))
                        score += real_score
                    else:
                        wrong_answers.append(
                            f'Question: {question_text}, Student Answer: {answer}, Correct Answer: {real_answer}')

            st.write("---")

            feedback_response = requests.post(f"{API_URL}/get_feedback",
                                              data={"wrong_answers": wrong_answers, "total_points": total_points,
                                                    "score": score, "student_details": student_details, "topic": topic})

            if feedback_response.status_code == 200:
                if score < 0.5 * total_points:
                    st.error(f"Your score: {score}/{total_points}")
                else:
                    st.balloons()

                    st.success(f"Your score: {score}/{total_points}")

                feedback_data = feedback_response.json()
                st.write("## Feedback")
                st.write(feedback_data.get("feedback", "No feedback available."))
            else:
                st.success(f"Your score: {score}/{total_points}")
    else:
        st.write("No questions generated.")


def display_videos(course):
    videos = course["videos"]
    course_name = course["name"]
    num_videos = len(videos)

    for i in range(num_videos):
        video_url = videos[i]
        with st.expander(f"Video {i + 1}"):
            display_video_with_quiz(video_url, course_name)

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    def callback():
        st.session_state.button_clicked = True

    with st.container():
        if (st.button("Take Final Test", key=f"take_test_{course_name}", on_click=callback)
                or st.session_state.button_clicked
        ):
            display_quizzes(course)


def main():
    st.set_page_config(
        page_title="QGenAI by DOTS",
        page_icon="💠",
    )
    st.title("📚 Learning Management System")

    st.write("## 🆓 FREE COURSES")
    for course in courses:
        st.write(f"## {course['name']}")
        st.image(course["image"])
        display_videos(course)


if __name__ == "__main__":
    main()
