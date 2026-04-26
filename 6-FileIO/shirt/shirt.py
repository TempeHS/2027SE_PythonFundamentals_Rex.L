import sys
import os

supported_files = (".jpg", ".jpeg", ".png")

def main():
      input = sys.argv[1]
      output = sys.argv[2]
      
      validate_entry(input, output)
      

      
      
def validate_entry(input, output):
      file_supported = False
      same_file_type = False
      
      input_ext = os.path.splitext(input)
      output_ext = os.path.splitext(output)
      
      if len(sys.argv) != 3:
            return False
      elif input.endswith(supported_files) and output.endswith(supported_files):
            file_supported = True
      elif input_ext == output_ext:
            same_file_type = True

      
      
main()