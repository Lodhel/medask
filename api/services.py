import re


class MainServices:

    def check_data(self, number):
        # логика проверки данных полученных от пользователя
        pattern = re.compile('\d')
        result = pattern.findall(number)
        result = "".join(map(str, result))

        result_type = "dms"
        if len(result) == 12:
            pass
        elif len(result) == 10:
            result_type = "oms"
        return result_type


MainServices().check_data("9876-543210")