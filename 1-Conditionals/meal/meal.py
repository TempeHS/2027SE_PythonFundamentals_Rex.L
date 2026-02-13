def main():
      userTime = input("Enter a time: ")
      convert(userTime)
      
      
      

def convert(time):
      hour, minute = time.split(":")
      parsedMinute = float(minute) / 60
      
      convertedTime = float(hour) + float(parsedMinute)
      
      return convertedTime
      

if __name__ == "__main__":
      main()