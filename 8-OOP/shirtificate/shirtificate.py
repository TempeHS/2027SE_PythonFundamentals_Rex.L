from fpdf import FPDF


class Shirtificate(FPDF):
      def __init__(self, name):
            super().__init__(orientation="portrait", format="A4")
            self.name = name
            self.add_page()
            self.build()


      def build(self):
            self.set_fill_color(20, 20, 20)
            self.rect(0, 0, 210, 297, "F")
            self.set_font("Helvetica", style="B", size=36)
            self.set_text_color(255, 255, 255)
            self.set_y(20)
            self.cell(0, 20, "CS50 Shirtificate", align="C")
            self.image("shirtificate.png", x=10, y=50, w=190)
            self.set_font("Helvetica", "B", 24)
            self.set_text_color(255, 255, 255)
            self.set_y(110)
            self.cell(0, 20, f"{self.name} took CS50", align="C")


def main():
      user_input = input("Name: ")
      pdf = Shirtificate(user_input)
      pdf.output("shirtificate.pdf")
      print("shirtificate.pdf created")


if __name__ == "__main__":
      main()