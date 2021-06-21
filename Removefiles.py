import  os, shutil, time

def main():

	path = "A/"
	days = 30

	deletedFiles = 0

	seconds = (days * 24 * 60 * 60)-time.time() 
	print(seconds)
	
	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			if seconds >= fetchFiles(root_folder):

				remove_file(root_folder)
				deletedFiles += 1 
			
				break

			else:
				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= fetchFiles(folder_path):

						remove_file(folder_path)
						deletedFiles += 1

				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= fetchFiles(file_path):

						remove_file(file_path)
						deletedFiles += 1 
				
			""" else:
				if seconds >= fetchFiles(path):

					remove_file(path)
					deleted_files_count += 1 

	else:
		print('"{path}" is not found')
		deletedFiles += 1 
 """

	print(f"Total folders deleted: {deletedFiles}")


def remove_file(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the ", path)


def deleteFile(path):

	if not os.remove(path):
		print("{path} is deleted successfully")

	else:
		print("It's not able to delete this file "+path)


def fetchFiles(path):

	time = os.stat(path).st_ctime
	return time

main()