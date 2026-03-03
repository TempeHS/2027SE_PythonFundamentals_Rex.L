import random as r
accepted_levels = ["1", "2", "3"]
problem_amount = 10
problems = {}


def main():
      user_score = 0

      
      while True:
            user_input = input("Enter a level: ")
            if user_input not in accepted_levels:
                  continue
            else:
                  break
      generate_problems()
      
      for key in problems:
            attempts = 3
            while attempts > 0:
                  try:
                        user_answer = input(f"{key}: ")
                        if int(user_answer) == problems[key]:
                              print("Correct!")
                              user_score += 1
                              break
                        else:
                              raise ValueError
                  except ValueError:
                              print("EEE")
                              attempts -= 1

      print(f"Score: {user_score}")
                  
            
def generate_problems():
      for i in range(problem_amount):
            x = r.randint(0, 100)
            y = r.randint(0, 100)
            problems[f"{x} + {y}"] = x + y
      
      
if __name__ == "__main__":
      main()