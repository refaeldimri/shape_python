import os
from datetime import datetime
import dotenv


class Utilities:
    file = None

    def write_file(self, string):
        """
        This function get a string and
        write it to self.file.
        :param string:
        :return None:
        """
        dotenv.load_dotenv()
        os.chdir(os.getcwd())
        file_name = os.getenv("FILENAME")
        time_date = os.getenv("TIMESTAMP")
        try:
            self.file = open(file_name, "a")
            string += \
                datetime.now().strftime(", " + time_date + "\n")
            self.file.write(string)
            self.file.flush()
            self.file.close()
        except Exception as e:
            print(e)
