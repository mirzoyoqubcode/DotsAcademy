from questions_template import fitb_template, tf_template, mcq_template


def render_mcq(question):
    options = "\n".join([f"- {option}" for option in question["options"]])
    return mcq_template.format(
        question_text=question["question_text"],
        options=options,
        correct_answer=question["correct_answer"],
        difficulty_level=question["difficulty_level"],
        point_value=question["point_value"],
    )


def render_fitb(question):
    return fitb_template.format(
        question_text=question["question_text"],
        correct_answer=question["correct_answer"],
        difficulty_level=question["difficulty_level"],
        point_value=question["point_value"],
    )

def render_tf(question):
    return tf_template.format(
        question_text=question["question_text"],
        correct_answer=question["correct_answer"],
        difficulty_level=question["difficulty_level"],
        point_value=question["point_value"],
    )