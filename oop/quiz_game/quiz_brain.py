class QuizBrain:
  def __init__(self,q_list):
    self.question_number=0
    self.question_list=q_list
    self.correct_answers=0
  def has_more_qn(self):
    if self.question_number>=len(self.question_list):
      return False
    else:
      return True
    
  def next_qn (self):
    current_q= self.question_list[self.question_number]
    self.question_number+=1
    ans= input(f'Q. {self.question_number}: {current_q.text} (True/False)? ').lower()
     
    if not self.has_more_qn():
      print(f'You completed the quiz . Congrats, You scored {self.correct_answers} out of {len(self.question_list)}')
    else:
      if ans==current_q.answer.lower():
        self.correct_answers+=1
        print('Congrats You got it right!')
      else:
        print('Oopsie, Wrong answer!')
      self.current_score()
      self.next_qn( )
    
  def current_score(self):
    print(f'your current score {self.correct_answers}/ {self.question_number}')