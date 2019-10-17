import re


class MainServices:

    def check_data(self, number):
        # логика проверки данных полученных от пользователя
        pattern = re.compile('\d')
        result = pattern.findall(number)
        result = "".join(map(str, result))

        data_type = "dms"
        company = "СК МЕД-АСКЕР"
        if len(result) == 12:
            pass
        elif len(result) == 10:
            data_type = "oms"


        pattern = re.compile("[-]")
        result = pattern.findall(number)

        if result:
            pattern = re.compile("[\d -]")
            result = pattern.findall(number)
            result = [n for n, r in enumerate(result) if r not in (re.compile("\d")).findall("0123456789")]
            if result[0] == 4:
                if data_type == "dms":
                    company = "СК Рандеву"
                else:
                    company = "Страх-трах"
            elif result[0] == 2:
                if data_type == "oms":
                    company = "СК Рандеву"
                else:
                    company = "Страх-трах"

            return data_type, company

