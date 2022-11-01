import os
import os.path
from pathlib import Path

dict_refactor = {".find_element_by_id(" : ".find_element(By.ID,",
".find_element_by_name(" : ".find_element(By.NAME,",
".find_element_by_xpath(" : ".find_element(By.XPATH,",
".find_element_by_link_text(" : ".find_element(By.LINK_TEXT,",
".find_element_by_partical_link_text(" : ".find_element(By.PARTIAL_LINK_TEXT,",
".find_element_by_tag_name(" : ".find_element(By.TAG_NAME,",
".find_element_by_class_name(" : ".find_element(By.CLASS_NAME,",
".find_element_by_css_selector(" : ".find_element(By.CSS_SELECTOR,",
".find_elements_by_id(" : ".find_elements(By.ID,",
".find_elements_by_name(" : ".find_elements(By.NAME,",
".find_elements_by_xpath(" : ".find_elements(By.XPATH,",
".find_elements_by_link_text(" : ".find_elements(By.LINK_TEXT,",
".find_elements_by_partical_link_text(" : ".find_elements(By.PARTIAL_LINK_TEXT,",
".find_elements_by_tag_name(" : ".find_elements(By.TAG_NAME,",
".find_elements_by_class_name(" : ".find_elements(By.CLASS_NAME,",
".find_elements_by_css_selector(" : ".find_elements(By.CSS_SELECTOR,"}

path_result = Path("result_refactor")
if not os.path.exists(path_result):
    os.mkdir(path_result)

list_dir = os.listdir()

for i in list_dir:
    if  i.endswith(".py") and i != "main.py":
        with open(i, "r", encoding = "utf-8") as file_py:
            new_path = os.path.join(path_result,i)
            with open(new_path, "a", encoding = "utf-8") as file_resul:
                for x in file_py.readlines():
                   for key in dict_refactor:
                        if key in x:
                            x = x.replace(key, dict_refactor[key])
                   file_resul.write(x)
                
                
        
    