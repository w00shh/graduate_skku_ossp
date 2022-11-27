import read_courses

input_text = Element("input_text")
student_ID = Element("student_ID")
output_text = Element("output_text")
def function_add_text(*args):
  output_text.element.innerText = input_text.value.replace("C:\\fakepath\\",".\\sample_data\\")
  read_courses.main(input_text.value.replace("C:\\fakepath\\",".\\sample_data\\"),student_ID.value)