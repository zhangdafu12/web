import re


symbols = ["=", "<", ">", "≥", "≤", "并且", "或者"]

def convert(data):
    for symbol in symbols:
        if symbol in data:
            if symbol == "≥":
                change_symbol = ">="
            if symbol == "≤":
                change_symbol = "=<"
            if symbol == "并且":
                change_symbol = "and"
            if symbol == "或者":
                change_symbol = "or"
            if symbol == "=":
                change_symbol = "="
            if symbol == ">":
                change_symbol = ">"
            if symbol == "<":
                change_symbol = "<"
            if "是" in data:
                before_symbol = "is"
            else:
                before_symbol = "not"

            separate = data.split(symbol, 1)
            if "X" in separate[0]:
                before_property = re.search("1-(.*?)-X", separate[0]).group(1)

                if "X" in separate[1].strip("X"):
                    middle_property = re.search("1-(.*?)-X", separate[1]).group(1)

                    last_sentence = separate[1].split("X")[-1].strip("-")
                    if "-0-" in last_sentence:
                        last_list = [x for x in last_sentence.split("-") if x != "0" and x != "=" and x]

                        res_first_account = last_list[0]
                        res_first_balance = last_list[1]
                        res_second_account = last_list[2]
                        res_second_balance = last_list[3]

                        code = f"if {before_symbol} ({before_property} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} = {res_second_account}.{res_second_balance}"
                        return code
                    if "-1-" in last_sentence:
                        last_1_list = last_sentence.strip("-").split("-")
                        res_first_account = last_1_list[0]
                        res_first_balance = last_1_list[1]
                        if last_1_list[-1] == "0":
                            balance_plus = "0"
                        else:
                            balance_plus = ".".join(last_1_list[-3:])

                        code = f"if {before_symbol} ({before_property} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus}"

                        if re.search("微信支付", last_sentence):
                            pay = "微信支付"
                            code = f"if {before_symbol} ({before_property} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"
                        if re.search("支付宝支付", last_sentence):
                            pay = "支付宝支付"

                            code = f"if {before_symbol} ({before_property} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"

                        return code
                else:
                    middle = data.split("-0-", 1)[-1]
                    middle_account = middle.split("-", 2)[0]
                    middle_balance = middle.split("-", 2)[1]
                    last_sentence = middle.split("-", 2)[-1]

                    if "-0-" in last_sentence:
                        last_list = [x for x in last_sentence.split("-") if x != "0" and x != "=" and x]

                        res_first_account = last_list[0]
                        res_first_balance = last_list[1]
                        res_second_account = last_list[2]
                        res_second_balance = last_list[3]

                        code = f"if {before_symbol} ({before_property} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} = {res_second_account}.{res_second_balance}"
                        return code
                    if "-1-" in last_sentence:
                        last_1_list = last_sentence.strip("-").split("-")
                        res_first_account = last_1_list[0]
                        res_first_balance = last_1_list[1]
                        if last_1_list[-1] == "0":
                            balance_plus = "0"
                        else:
                            balance_plus = ".".join(last_1_list[-3:])

                        code = f"if {before_symbol} ({before_property} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus}"

                        if re.search("微信支付", last_sentence):
                            pay = "微信支付"
                            code = f"if {before_symbol} ({before_property} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"
                        if re.search("支付宝支付", last_sentence):
                            pay = "支付宝支付"

                            code = f"if {before_symbol} ({before_property} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"

                        return code
            else:
                before_account = separate[0].strip("-").split("-")[2]
                before_balance = separate[0].strip("-").split("-")[-1]
                if "X" in separate[1].strip("X"):
                    middle_property = re.search("1-(.*?)-X", separate[1]).group(1)

                    last_sentence = separate[1].split("X")[-1].strip("-")
                    if "-0-" in last_sentence:
                        last_list = [x for x in last_sentence.split("-") if x != "0" and x != "=" and x]

                        res_first_account = last_list[0]
                        res_first_balance = last_list[1]
                        res_second_account = last_list[2]
                        res_second_balance = last_list[3]

                        code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} = {res_second_account}.{res_second_balance}"
                        return code
                    if "-1-" in last_sentence:
                        last_1_list = last_sentence.strip("-").split("-")
                        res_first_account = last_1_list[0]
                        res_first_balance = last_1_list[1]
                        if last_1_list[-1] == "0":
                            balance_plus = "0"
                        else:
                            balance_plus = ".".join(last_1_list[-3:])

                        code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus}"

                        if re.search("微信支付", last_sentence):
                            pay = "微信支付"
                            code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"
                        if re.search("支付宝支付", last_sentence):
                            pay = "支付宝支付"

                            code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_property}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"

                        return code
                else:
                    middle = data.split("-0-", 1)[-1]
                    middle_account = middle.split("-", 2)[0]
                    middle_balance = middle.split("-", 2)[1]
                    last_sentence = middle.split("-", 2)[-1]

                    if "-0-" in last_sentence:
                        last_list = [x for x in last_sentence.split("-") if x != "0" and x != "=" and x]

                        res_first_account = last_list[0]
                        res_first_balance = last_list[1]
                        res_second_account = last_list[2]
                        res_second_balance = last_list[3]

                        code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} = {res_second_account}.{res_second_balance}"
                        return code
                    if "-1-" in last_sentence:
                        last_1_list = last_sentence.strip("-").split("-")
                        res_first_account = last_1_list[0]
                        res_first_balance = last_1_list[1]
                        if last_1_list[-1] == "0":
                            balance_plus = "0"
                        else:
                            balance_plus = ".".join(last_1_list[-3:])

                        code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus}"

                        if re.search("微信支付", last_sentence):
                            pay = "微信支付"
                            code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"
                        if re.search("支付宝支付", last_sentence):
                            pay = "支付宝支付"

                            code = f"if {before_symbol} ({before_account}.{before_balance} {change_symbol} {middle_account}.{middle_balance}): \n \t{res_first_account}.{res_first_balance} += {balance_plus} \n \t pay = {pay}"

                        return code

if __name__ == '__main__':
    b = '是-0-账户a-账户余额-<-1-111-X-账户b-账户余额-1-111-222-3333-X'

    a = convert(b)
    print(a)
    print()
