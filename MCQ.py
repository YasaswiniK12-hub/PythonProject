from Question import Question
prompts=["What is the color of the Sun?\n a) Yellow/Red\n b) Pink\n c) Green\n\n",
           "What is the color of the apples?\n a) Red/Green\n b) Pink\n c) Teal\n\n",
           "What is the color of the strawberries?\n a) Orange\n b) Pink\n c) Red\n\n"]

questions=[
    Question(prompts[0],"a"),
    Question(prompts[1],"a"),
    Question(prompts[2],"c")
]

def run_test(questions):
    score=0
    for question in questions:
      ans=input(question.question)
      if ans==question.answer:
          score+=1;
    print(f"You got {score}/{len(questions)}")

run_test(questions)
