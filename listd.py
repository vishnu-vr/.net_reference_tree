import os
import sys

class reference_finder:
	def __init__(self):
	    self.NO_MORE_REFERENCE = "There are no Project to Project references"

	def find_reference(self,path):
		reference = os.popen('dotnet list '+ path +' reference').read()

		if self.NO_MORE_REFERENCE in reference:
			return []

		reference = reference.split()
		reference = reference[3:]
		return reference

	def print_reference_tree(self,path,space=""):
		self.print_path(path)

		space += "  "
		
		references = self.find_reference(path)
		for ref in references:
			self.print_arrow(space)
			self.print_reference_tree(ref,space)

	def print_arrow(self,space):
		print(space + "|")
		print(space + "-->",end="")


	def print_path(self,path):
		path = path.split("..\\")
		path = path[-1]
		print(path)

if __name__ == "__main__":
	try:
		path = sys.argv[1]
		# check whether the file is valid
		f = open(path)
		f.close()
	except Exception:
		print("INVALID FILE")
		path = False
	finally:
		if path == False:
			pwd = os.getcwd()
			pwd_split = pwd.split("\\")
			path = pwd + "\\" + pwd_split[-1] + ".csproj"

		try:
			# check whether the file is valid
			f = open(path)
			f.close()
		except Exception:
			print("CURRENT DIRECTORY DOESN'T CONTAINT A .CSPROJ FILE")
			sys.exit()

	finder = reference_finder()

	chdir = path.split("\\")
	os.chdir('\\'.join(chdir[:-1]))
	finder.print_reference_tree(path)

