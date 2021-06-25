# coding = utf-8

from copy import deepcopy

import pandas
import yaml
from pandas import DataFrame

agent_id = []


class OperationExcel(object):
    def __init__(self, excel_path):
        self.file = pandas.read_excel(excel_path)
        self.values = self.file.values
        self.file_path = excel_path

    def get_values(self):
        """
        read excel
        """
        return self.values

    def update_excel(self, row_index, col_index, up_data, sheet_name="Sheet1", index=False, header=True):
        """
        修改excel
        """
        self.values[row_index][col_index] = up_data
        DataFrame(self.values).to_excel(self.file_path, sheet_name=sheet_name, index=index, header=header)


class OperationYaml(object):
    def __init__(self, yaml_path):
        self.file = open(yaml_path, "r", encoding='utf-8')
        self.cfg = self.file.read()

    def load_yaml(self):
        return yaml.load(self.cfg)

    def dict_yaml(self, excel_path):  # , new_yaml_path):
        file = OperationExcel(excel_path)
        # print(file.values)
        intents = list()
        intent = dict()
        utter_faq = dict()
        for i in file.values:
            intent["intent"] = "faq|" + i[1]
            utter_faq_key = "utter_faq|" + i[1]
            utter_faq[utter_faq_key] = i[4]
            if "||" in i[2]:
                examples_value = i[2].split("||")
            else:
                print(i[2])
                examples_value = []
                examples_value.append(i[2])
                print(examples_value)
            intent["examples"] = examples_value
            if isinstance(i[4], str):
                value = i[4].strip().replace("_x000d_", "")
            else:
                value = i[4]
            utter_faq[utter_faq_key] = {"response_mode": 'all',
                                        "response": [{"text": value}]}
            # print(intent)
            intents.append(deepcopy(intent))  # 解决list append过程中值被覆盖问题
        # print(intents)
        return intents, utter_faq
        # dict_yaml_value = OperationYaml(yaml_path).load_yaml()
        # print(dict_yaml_value["intents"])
        # dict_yaml_value["intents"] = intents
        # # print(dict_yaml_value["intents"])
        # print(dict_yaml_value)
        # dict_yaml_value["faqs"] = utter_faq
        # print(dict_yaml_value)
        # file = open(new_yaml_path, "w", encoding="utf-8")
        # yaml.dump(dict_yaml_value, file, allow_unicode=True, default_flow_style=False, sort_keys=False)  # 该行的代码中sort_keys的默认值为True，改为Flase后可修复代顺序变化的问题
        # file.close()


def main():
    excel_path = ["../data/{51Talk（未缩减）}知识点_2021-03-31 07_08_25.xlsx",
                  "../data/{Dior知识库（未缩减）}知识点_2021-03-31 07_03_51.xlsx",
                  "../data/{Nike知识库（未缩减）}知识点_2021-03-31 07_05_06.xlsx",
                  "../data/{新东方（未缩减）}知识点_2021-03-31 07_07_51.xlsx",
                  "../data/{育学园（未缩减）}知识点_2021-03-31 07_02_33.xlsx"]
    yaml_path = "../domain.yaml"
    new_yaml_path = "../domain_z.yaml"
    intents_list = []
    utter_faq_dict = {}
    for i in excel_path:
        intents, utter_faq = OperationYaml(yaml_path).dict_yaml(i)
        # print(intents)
        # print(utter_faq)
        intents_list.extend(deepcopy(intents))
        utter_faq_dict.update(utter_faq)
    # print(intents_list)
    # print(utter_faq_dict)
    dict_yaml_value = OperationYaml(yaml_path).load_yaml()
    print(dict_yaml_value["faqs"])
    dict_yaml_value["intents"] = intents_list
    # print(dict_yaml_value["intents"])
    # print(dict_yaml_value)
    dict_yaml_value["faqs"] = utter_faq_dict
    # print(dict_yaml_value)
    file = open(new_yaml_path, "w", encoding="utf-8")
    yaml.dump(dict_yaml_value, file, allow_unicode=True, default_flow_style=False,
              sort_keys=False)  # 该行的代码中sort_keys的默认值为True，改为Flase后可修复代顺序变化的问题
    file.close()


if __name__ == '__main__':
    # excel_path = "../data/{新东方（未缩减）}知识点_2021-03-31 07_07_51.xlsx"
    # yaml_path = "../domain.yaml"
    # new_yaml_path = "../domain4.yaml"
    # OperationYaml(yaml_path).dict_yaml(excel_path, new_yaml_path)
    main()
