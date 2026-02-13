def main():
      userTime = input("Enter a time: ")
      convertedTime = convert(userTime)
      print(convertedTime) # Debug
      
      if convertedTime >= float(7.00) and convertedTime <= float(8.00):
            print("breakfast time")
      elif convertedTime >= float(12.00) and convertedTime <= float(13.00):
            print("lunch time")
      elif convertedTime >= float(18.00) and convertedTime <= float(19.00):
            print("dinner time")
      else:
            print("not time to eat")
      
      

def convert(time):
      hour, minute = time.split(":")
      parsedMinute = float(minute) / 60
      
      convertedTime = float(hour) + float(parsedMinute)
      
      return convertedTime
      

if __name__ == "__main__":
      main()