from flask import Flask, render_template, request

app = Flask(__name__)

# =====================================================
# Generator Agent
# =====================================================
class GeneratorAgent:
    def generate(self, input_data, feedback=None):
        grade = input_data["grade"]
        topic = input_data["topic"]

        simplified = feedback is not None

        if simplified:
            explanation = (
                f"{topic} is studied in Grade {grade}. "
                f"It explains basic ideas related to {topic}. "
                f"The explanation uses simple words. "
                f"This helps students understand the topic easily."
            )
        else:
            explanation = (
                f"{topic} is an important topic in Grade {grade}. "
                f"It introduces the main ideas related to {topic}. "
                f"This topic helps build strong fundamentals. "
                f"It is useful for future learning."
            )

        mcqs = [
            {
                "question": f"Why is {topic} important to study?",
                "options": [
                    "It helps build basic understanding",
                    "It is not useful",
                    "It is only for exams",
                    "It has no applications"
                ],
                "answer": "It helps build basic understanding"
            }
        ]

        return {
            "explanation": explanation,
            "mcqs": mcqs
        }


# =====================================================
# Reviewer Agent
# =====================================================
class ReviewerAgent:
    def review(self, content, grade):
        feedback = []

        # Age appropriateness
        if grade <= 5 and len(content["explanation"].split()) > 45:
            feedback.append("Explanation is too complex for the given grade.")

        # Structure check
        if "explanation" not in content or "mcqs" not in content:
            feedback.append("Output structure is incorrect.")

        # MCQ correctness
        for mcq in content["mcqs"]:
            if mcq["answer"] not in mcq["options"]:
                feedback.append("MCQ answer does not match the options.")

        status = "pass" if not feedback else "fail"

        return {
            "status": status,
            "feedback": feedback
        }


# =====================================================
# Agent Pipeline + UI Trigger
# =====================================================
@app.route("/", methods=["GET", "POST"])
def index():
    generator_output = None
    reviewer_output = None
    refined_output = None

    if request.method == "POST":
        grade = int(request.form["grade"])
        topic = request.form["topic"]

        input_data = {
            "grade": grade,
            "topic": topic
        }

        generator = GeneratorAgent()
        reviewer = ReviewerAgent()

        # First generation
        generator_output = generator.generate(input_data)

        # Review
        reviewer_output = reviewer.review(generator_output, grade)

        # One-pass refinement
        if reviewer_output["status"] == "fail":
            refined_output = generator.generate(
                input_data,
                feedback=reviewer_output["feedback"]
            )

    return render_template(
        "index.html",
        generator=generator_output,
        reviewer=reviewer_output,
        refined=refined_output
    )


if __name__ == "__main__":
    app.run(debug=True)
