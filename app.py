class LMSChatbot:
    def __init__(self):
        self.responses = {
            "enrollment": [
                "To enroll in a course, go to the LMS dashboard, select the course catalog, and click the enrollment or register button.",
                "If you cannot see the course, check if the course is open for enrollment or contact your academic advisor."
            ],
            "assignment": [
                "You can view assignments from your course dashboard. Submit the file or text before the due date using the assignment upload option.",
                "If the assignment is missing, check whether the course has closed submissions or contact the instructor."
            ],
            "grade": [
                "You can check your marks from the Results or Grades section in the LMS.",
                "If your grade is missing, contact your instructor or the LMS support team."
            ],
            "exam": [
                "Exam dates and schedules are normally listed in the course calendar or announcements section.",
                "If you cannot find the exam schedule, ask your instructor or the academic office."
            ],
            "login": [
                "If you are unable to login, check your username and password, reset your password, and ensure your account is active.",
                "If the issue continues, contact the LMS support desk."
            ],
            "payment": [
                "For fee or payment issues, contact the finance or billing office through your institution.",
                "Please share your student ID, course name, and payment reference if you need faster assistance."
            ],
            "support": [
                "For general support, email or call the LMS support team and share your issue details clearly.",
                "Include your student ID, course name, and the exact error message if possible."
            ],
        }

    def _detect_topic(self, message):
        text = message.lower()

        if any(word in text for word in ["enroll", "course", "registration", "class"]):
            return "enrollment"
        if any(word in text for word in ["assignment", "homework", "submit", "submission", "upload"]):
            return "assignment"
        if any(word in text for word in ["grade", "marks", "result", "score", "cgpa"]):
            return "grade"
        if any(word in text for word in ["exam", "test", "quiz", "deadline", "schedule"]):
            return "exam"
        if any(word in text for word in ["login", "password", "sign in", "signin", "access", "username"]):
            return "login"
        if any(word in text for word in ["fee", "payment", "invoice", "billing", "charge"]):
            return "payment"
        if any(word in text for word in ["support", "help", "problem", "issue", "error"]):
            return "support"

        return "support"

    def respond(self, message):
        if not message or not message.strip():
            return "Please type your LMS question."

        topic = self._detect_topic(message)
        options = self.responses.get(topic, self.responses["support"])
        return options[0]


def main():
    bot = LMSChatbot()
    print("Welcome to the LMS Query Chatbot!")
    print("Ask me about courses, assignments, grades, exams, login, fees, or general support.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_message = input("You: ")

        if user_message.strip().lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day.")
            break

        response = bot.respond(user_message)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
