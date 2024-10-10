from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
  text=question['text']
  ans=question['answer']
  new_question=Question(text=text,answer=ans)
  question_bank.append(new_question)

q_brain=QuizBrain(q_list=question_bank)
q_brain.next_qn()