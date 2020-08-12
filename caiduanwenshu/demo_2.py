# coding:utf-8
from tools.shujuku_conn.oracle_conn import OracleOperation
import re


db = OracleOperation()
DATA = db.execute_sql("SELECT case_id,clear_about_patent FROM jugement_table_0728_re_qx where identify='专利名称'")
data = db.get_data()
num = 0
#37992
for concent in data:
    case_id = concent[0]
    try:
        fmt_content_n = concent[1]
        # 专利名称
        data_name = []
        # name_1_1 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',patent)
        name_1_1_1 = re.findall('“([^”，；。]+)”发明', fmt_content_n)

        name_1_1_2 = re.findall('“([^”，；。]+)”、发明', fmt_content_n)
        name_1_1_3 = re.findall('“([^”，；。]+)”，发明', fmt_content_n)
        name_1_1_4 = re.findall('“([^”，；。]+)”涉案发明', fmt_content_n)
        name_1_1_5 = re.findall('“([^”，；。]+)”的发明', fmt_content_n)
        # name_1_2 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
        name_1_2_1 = re.findall('“([^”，；。]+)”实用新型', fmt_content_n)
        name_1_2_2 = re.findall('“([^”，；。]+)”、实用新型', fmt_content_n)
        name_1_2_3 = re.findall('“([^”，；。]+)”，实用新型', fmt_content_n)
        name_1_2_4 = re.findall('“([^”，；。]+)”涉案实用新型', fmt_content_n)
        name_1_2_5 = re.findall('“([^”，；。]+)”的实用新型', fmt_content_n)
        # name_1_3 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
        name_1_3_1 = re.findall('“([^”，；。]+)”外观', fmt_content_n)
        name_1_3_2 = re.findall('“([^”，；。]+)”、外观', fmt_content_n)
        name_1_3_3 = re.findall('“([^”，；。]+)”，外观', fmt_content_n)
        name_1_3_4 = re.findall('“([^”，；。]+)”涉案外观', fmt_content_n)
        name_1_3_5 = re.findall('“([^”，；。]+)”的外观', fmt_content_n)
        # name_1_4 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
        name_1_4_1 = re.findall('“([^”，；。]+)”专利', fmt_content_n)
        name_1_4_2 = re.findall('“([^”，；。]+)”、专利', fmt_content_n)
        name_1_4_3 = re.findall('“([^”，；。]+)”，专利', fmt_content_n)
        name_1_4_4 = re.findall('“([^”，；。]+)”涉案专利', fmt_content_n)
        name_1_4_5 = re.findall('“([^”，；。]+)”的专利', fmt_content_n)
        # name_1_5 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
        name_1_5_1 = re.findall('“([^”，；。]+)”申请', fmt_content_n)
        name_1_5_2 = re.findall('“([^”，；。]+)”、申请', fmt_content_n)
        name_1_5_3 = re.findall('“([^”，；。]+)”，申请', fmt_content_n)
        name_1_5_4 = re.findall('“([^”，；。]+)”涉案申请', fmt_content_n)
        name_1_5_5 = re.findall('“([^”，；。]+)”的申请', fmt_content_n)
        # name_2_1 = re.findall('发明名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_1_1 = re.findall('发明“([^”，；。]+)”', fmt_content_n)
        name_2_1_2 = re.findall('发明名称“([^”，；。]+)”', fmt_content_n)
        name_2_1_3 = re.findall('发明为“([^”，；。]+)”', fmt_content_n)
        name_2_1_4 = re.findall('发明名称为“([^”，；。]+)”', fmt_content_n)
        # name_2_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_2_1 = re.findall('实用新型“([^”，；。]+)”', fmt_content_n)
        name_2_2_2 = re.findall('实用新型名称“([^”，；。]+)”', fmt_content_n)
        name_2_2_3 = re.findall('实用新型为“([^”，；。]+)”', fmt_content_n)
        name_2_2_4 = re.findall('实用新型名称为“([^”，；。]+)”', fmt_content_n)
        # name_2_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_3_1 = re.findall('外观设计“([^”，；。]+)”', fmt_content_n)
        name_2_3_2 = re.findall('外观设计名称“([^”，；。]+)”', fmt_content_n)
        name_2_3_3 = re.findall('外观设计为“([^”，；。]+)”', fmt_content_n)
        name_2_3_4 = re.findall('外观设计名称为“([^”，；。]+)”', fmt_content_n)
        # name_2_4 = re.findall('专利名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_4_1 = re.findall('专利“([^”，；。]+)”', fmt_content_n)
        name_2_4_2 = re.findall('专利名称“([^”，；。]+)”', fmt_content_n)
        name_2_4_3 = re.findall('专利为“([^”，；。]+)”', fmt_content_n)
        name_2_4_4 = re.findall('专利名称为“([^”，；。]+)”', fmt_content_n)
        # name_2_5 = re.findall('申请名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
        name_2_5_1 = re.findall('申请“([^”，；。]+)”', fmt_content_n)
        name_2_5_2 = re.findall('申请名称“([^”，；。]+)”', fmt_content_n)
        name_2_5_3 = re.findall('申请为“([^”，；。]+)”', fmt_content_n)
        name_2_5_4 = re.findall('申请名称为“([^”，；。]+)”', fmt_content_n)
        name_3_1 = re.findall('名称为“([^”，；。]+)”（专利', fmt_content_n)
        name_3_2 = re.findall('名称为“([^”，；。]+)”（发明', fmt_content_n)
        name_3_3 = re.findall('名称为“([^”，；。]+)”（实用新型', fmt_content_n)
        name_3_4 = re.findall('名称为“([^”，；。]+)”（外观设计', fmt_content_n)
        name_3_5 = re.findall('名称为“([^”，；。]+)”（申请', fmt_content_n)
        # name_4_1 = re.findall('《.*?》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',fmt_content_n)
        name_4_1_1 = re.findall('《([^》，；。]+)》发明', fmt_content_n)
        name_4_1_2 = re.findall('《([^》，；。]+)》、发明', fmt_content_n)
        name_4_1_3 = re.findall('《([^》，；。]+)》，发明', fmt_content_n)
        name_4_1_4 = re.findall('《([^》，；。]+)》涉案发明', fmt_content_n)
        name_4_1_5 = re.findall('《([^》，；。]+)》的发明', fmt_content_n)
        # name_4_2 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
        name_4_2_1 = re.findall('《([^》，；。]+)》实用新型', fmt_content_n)
        name_4_2_2 = re.findall('《([^》，；。]+)》、实用新型', fmt_content_n)
        name_4_2_3 = re.findall('《([^》，；。]+)》，实用新型', fmt_content_n)
        name_4_2_4 = re.findall('《([^》，；。]+)》涉案实用新型', fmt_content_n)
        name_4_2_5 = re.findall('《([^》，；。]+)》的实用新型', fmt_content_n)
        # name_4_3 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
        name_4_3_1 = re.findall('《([^》，；。]+)》外观', fmt_content_n)
        name_4_3_2 = re.findall('《([^》，；。]+)》、外观', fmt_content_n)
        name_4_3_3 = re.findall('《([^》，；。]+)》，外观', fmt_content_n)
        name_4_3_4 = re.findall('《([^》，；。]+)》涉案外观', fmt_content_n)
        name_4_3_5 = re.findall('《([^》，；。]+)》的外观', fmt_content_n)
        # name_4_4 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
        name_4_4_1 = re.findall('《([^》，；。]+)》专利', fmt_content_n)
        name_4_4_2 = re.findall('《([^》，；。]+)》、专利', fmt_content_n)
        name_4_4_3 = re.findall('《([^》，；。]+)》，专利', fmt_content_n)
        name_4_4_4 = re.findall('《([^》，；。]+)》涉案专利', fmt_content_n)
        name_4_4_5 = re.findall('《([^》，；。]+)》的专利', fmt_content_n)
        # name_4_5 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
        name_4_5_1 = re.findall('《([^》，；。]+)》申请', fmt_content_n)
        name_4_5_2 = re.findall('《([^》，；。]+)》、申请', fmt_content_n)
        name_4_5_3 = re.findall('《([^》，；。]+)》，申请', fmt_content_n)
        name_4_5_4 = re.findall('《([^》，；。]+)》涉案申请', fmt_content_n)
        name_4_5_5 = re.findall('《([^》，；。]+)》的申请', fmt_content_n)
        # name_5_1 = re.findall('发明名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_1_1 = re.findall('发明《([^》，；。]+)》', fmt_content_n)
        name_5_1_2 = re.findall('发明名称《([^》，；。]+)》', fmt_content_n)
        name_5_1_3 = re.findall('发明为《([^》，；。]+)》', fmt_content_n)
        name_5_1_4 = re.findall('发明名称为《([^》，；。]+)》', fmt_content_n)
        # name_5_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_2_1 = re.findall('实用新型《([^》，；。]+)》', fmt_content_n)
        name_5_2_2 = re.findall('实用新型名称《([^》，；。]+)》', fmt_content_n)
        name_5_2_3 = re.findall('实用新型为《([^》，；。]+)》', fmt_content_n)
        name_5_2_4 = re.findall('实用新型名称为《([^》，；。]+)》', fmt_content_n)
        # name_5_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_3_1 = re.findall('外观设计《([^》，；。]+)》', fmt_content_n)
        name_5_3_2 = re.findall('外观设计名称《([^》，；。]+)》', fmt_content_n)
        name_5_3_3 = re.findall('外观设计为《([^》，；。]+)》', fmt_content_n)
        name_5_3_4 = re.findall('外观设计名称为《([^》，；。]+)》', fmt_content_n)
        # name_5_4 = re.findall('专利名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_4_1 = re.findall('专利《([^》，；。]+)》', fmt_content_n)
        name_5_4_2 = re.findall('专利名称《([^》，；。]+)》', fmt_content_n)
        name_5_4_3 = re.findall('专利为《([^》，；。]+)》', fmt_content_n)
        name_5_4_4 = re.findall('专利名称为《([^》，；。]+)》', fmt_content_n)
        # name_5_5 = re.findall('申请名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
        name_5_5_1 = re.findall('申请《([^》，；。]+)》', fmt_content_n)
        name_5_5_2 = re.findall('申请名称《([^》，；。]+)》', fmt_content_n)
        name_5_5_3 = re.findall('申请为《([^》，；。]+)》', fmt_content_n)
        name_5_5_4 = re.findall('申请名称为《([^》，；。]+)》', fmt_content_n)
        name_6_1 = re.findall('名称为《([^》，；。]+)》（专利', fmt_content_n)
        name_6_2 = re.findall('名称为《([^》，；。]+)》（发明', fmt_content_n)
        name_6_3 = re.findall('名称为《([^》，；。]+)》（实用新型', fmt_content_n)
        name_6_4 = re.findall('名称为《([^》，；。]+)》（外观设计', fmt_content_n)
        name_6_5 = re.findall('名称为《([^》，；。]+)》（申请', fmt_content_n)
        if len(name_1_1_1) > 0:
            for i in name_1_1_1:
                data_name.append(i)
        if len(name_1_1_2) > 0:
            for i in name_1_1_2:
                data_name.append(i)
        if len(name_1_1_3) > 0:
            for i in name_1_1_3:
                data_name.append(i)
        if len(name_1_1_4) > 0:
            for i in name_1_1_4:
                data_name.append(i)
        if len(name_1_1_5) > 0:
            for i in name_1_1_5:
                data_name.append(i)
        if len(name_1_2_1) > 0:
            for i in name_1_2_1:
                data_name.append(i)
        if len(name_1_2_2) > 0:
            for i in name_1_2_2:
                data_name.append(i)
        if len(name_1_2_3) > 0:
            for i in name_1_2_3:
                data_name.append(i)
        if len(name_1_2_4) > 0:
            for i in name_1_2_4:
                data_name.append(i)
        if len(name_1_2_5) > 0:
            for i in name_1_2_5:
                data_name.append(i)
        if len(name_1_3_1) > 0:
            for i in name_1_3_1:
                data_name.append(i)
        if len(name_1_3_2) > 0:
            for i in name_1_3_2:
                data_name.append(i)
        if len(name_1_3_3) > 0:
            for i in name_1_3_3:
                data_name.append(i)
        if len(name_1_3_4) > 0:
            for i in name_1_3_4:
                data_name.append(i)
        if len(name_1_3_5) > 0:
            for i in name_1_3_5:
                data_name.append(i)
        if len(name_1_4_1) > 0:
            for i in name_1_4_1:
                data_name.append(i)
        if len(name_1_4_2) > 0:
            for i in name_1_4_2:
                data_name.append(i)
        if len(name_1_4_3) > 0:
            for i in name_1_4_3:
                data_name.append(i)
        if len(name_1_4_4) > 0:
            for i in name_1_4_4:
                data_name.append(i)
        if len(name_1_4_5) > 0:
            for i in name_1_4_5:
                data_name.append(i)
        if len(name_1_5_1) > 0:
            for i in name_1_5_1:
                data_name.append(i)
        if len(name_1_5_2) > 0:
            for i in name_1_5_2:
                data_name.append(i)
        if len(name_1_5_3) > 0:
            for i in name_1_5_3:
                data_name.append(i)
        if len(name_1_5_4) > 0:
            for i in name_1_5_4:
                data_name.append(i)
        if len(name_1_5_5) > 0:
            for i in name_1_5_5:
                data_name.append(i)
        if len(name_2_1_1) > 0:
            for i in name_2_1_1:
                data_name.append(i)
        if len(name_2_1_2) > 0:
            for i in name_2_1_2:
                data_name.append(i)
        if len(name_2_1_3) > 0:
            for i in name_2_1_3:
                data_name.append(i)
        if len(name_2_1_4) > 0:
            for i in name_2_1_4:
                data_name.append(i)
        if len(name_2_2_1) > 0:
            for i in name_2_2_1:
                data_name.append(i)
        if len(name_2_2_2) > 0:
            for i in name_2_2_2:
                data_name.append(i)
        if len(name_2_2_3) > 0:
            for i in name_2_2_3:
                data_name.append(i)
        if len(name_2_2_4) > 0:
            for i in name_2_2_4:
                data_name.append(i)
        if len(name_2_3_1) > 0:
            for i in name_2_3_1:
                data_name.append(i)
        if len(name_2_3_2) > 0:
            for i in name_2_3_2:
                data_name.append(i)
        if len(name_2_3_3) > 0:
            for i in name_2_3_3:
                data_name.append(i)
        if len(name_2_3_4) > 0:
            for i in name_2_3_4:
                data_name.append(i)
        if len(name_2_4_1) > 0:
            for i in name_2_4_1:
                data_name.append(i)
        if len(name_2_4_2) > 0:
            for i in name_2_4_2:
                data_name.append(i)
        if len(name_2_4_3) > 0:
            for i in name_2_4_3:
                data_name.append(i)
        if len(name_2_4_4) > 0:
            for i in name_2_4_4:
                data_name.append(i)
        if len(name_2_5_1) > 0:
            for i in name_2_5_1:
                data_name.append(i)
        if len(name_2_5_2) > 0:
            for i in name_2_5_2:
                data_name.append(i)
        if len(name_2_5_3) > 0:
            for i in name_2_5_3:
                data_name.append(i)
        if len(name_2_5_4) > 0:
            for i in name_2_5_4:
                data_name.append(i)
        if len(name_3_1) > 0:
            for i in name_3_1:
                data_name.append(i)
        if len(name_3_2) > 0:
            for i in name_3_2:
                data_name.append(i)
        if len(name_3_3) > 0:
            for i in name_3_3:
                data_name.append(i)
        if len(name_3_4) > 0:
            for i in name_3_4:
                data_name.append(i)
        if len(name_3_5) > 0:
            for i in name_3_5:
                data_name.append(i)
        if len(name_4_1_1) > 0:
            for i in name_4_1_1:
                data_name.append(i)
        if len(name_4_1_2) > 0:
            for i in name_4_1_2:
                data_name.append(i)
        if len(name_4_1_3) > 0:
            for i in name_4_1_3:
                data_name.append(i)
        if len(name_4_1_4) > 0:
            for i in name_4_1_4:
                data_name.append(i)
        if len(name_4_1_5) > 0:
            for i in name_4_1_5:
                data_name.append(i)
        if len(name_4_2_1) > 0:
            for i in name_4_2_1:
                data_name.append(i)
        if len(name_4_2_2) > 0:
            for i in name_4_2_2:
                data_name.append(i)
        if len(name_4_2_3) > 0:
            for i in name_4_2_3:
                data_name.append(i)
        if len(name_4_2_4) > 0:
            for i in name_4_2_4:
                data_name.append(i)
        if len(name_4_2_5) > 0:
            for i in name_4_2_5:
                data_name.append(i)
        if len(name_4_3_1) > 0:
            for i in name_4_3_1:
                data_name.append(i)
        if len(name_4_3_2) > 0:
            for i in name_4_3_2:
                data_name.append(i)
        if len(name_4_3_3) > 0:
            for i in name_4_3_3:
                data_name.append(i)
        if len(name_4_3_4) > 0:
            for i in name_4_3_4:
                data_name.append(i)
        if len(name_4_3_5) > 0:
            for i in name_4_3_5:
                data_name.append(i)
        if len(name_4_4_1) > 0:
            for i in name_4_4_1:
                data_name.append(i)
        if len(name_4_4_2) > 0:
            for i in name_4_4_2:
                data_name.append(i)
        if len(name_4_4_3) > 0:
            for i in name_4_4_3:
                data_name.append(i)
        if len(name_4_4_4) > 0:
            for i in name_4_4_4:
                data_name.append(i)
        if len(name_4_4_5) > 0:
            for i in name_4_4_5:
                data_name.append(i)
        if len(name_4_5_1) > 0:
            for i in name_4_5_1:
                data_name.append(i)
        if len(name_4_5_2) > 0:
            for i in name_4_5_2:
                data_name.append(i)
        if len(name_4_5_3) > 0:
            for i in name_4_5_3:
                data_name.append(i)
        if len(name_4_5_4) > 0:
            for i in name_4_5_4:
                data_name.append(i)
        if len(name_4_5_5) > 0:
            for i in name_4_5_5:
                data_name.append(i)
        if len(name_5_1_1) > 0:
            for i in name_5_1_1:
                data_name.append(i)
        if len(name_5_1_2) > 0:
            for i in name_5_1_2:
                data_name.append(i)
        if len(name_5_1_3) > 0:
            for i in name_5_1_3:
                data_name.append(i)
        if len(name_5_1_4) > 0:
            for i in name_5_1_4:
                data_name.append(i)
        if len(name_5_2_1) > 0:
            for i in name_5_2_1:
                data_name.append(i)
        if len(name_5_2_2) > 0:
            for i in name_5_2_2:
                data_name.append(i)
        if len(name_5_2_3) > 0:
            for i in name_5_2_3:
                data_name.append(i)
        if len(name_5_2_4) > 0:
            for i in name_5_2_4:
                data_name.append(i)
        if len(name_5_3_1) > 0:
            for i in name_5_3_1:
                data_name.append(i)
        if len(name_5_3_2) > 0:
            for i in name_5_3_2:
                data_name.append(i)
        if len(name_5_3_3) > 0:
            for i in name_5_3_3:
                data_name.append(i)
        if len(name_5_3_4) > 0:
            for i in name_5_3_4:
                data_name.append(i)
        if len(name_5_4_1) > 0:
            for i in name_5_4_1:
                data_name.append(i)
        if len(name_5_4_2) > 0:
            for i in name_5_4_2:
                data_name.append(i)
        if len(name_5_4_3) > 0:
            for i in name_5_4_3:
                data_name.append(i)
        if len(name_5_4_4) > 0:
            for i in name_5_4_4:
                data_name.append(i)
        if len(name_5_5_1) > 0:
            for i in name_5_5_1:
                data_name.append(i)
        if len(name_5_5_2) > 0:
            for i in name_5_5_2:
                data_name.append(i)
        if len(name_5_5_3) > 0:
            for i in name_5_5_3:
                data_name.append(i)
        if len(name_5_5_4) > 0:
            for i in name_5_5_4:
                data_name.append(i)
        if len(name_6_1) > 0:
            for i in name_6_1:
                data_name.append(i)
        if len(name_6_2) > 0:
            for i in name_6_2:
                data_name.append(i)
        if len(name_6_3) > 0:
            for i in name_6_3:
                data_name.append(i)
        if len(name_6_4) > 0:
            for i in name_6_4:
                data_name.append(i)
        if len(name_6_5) > 0:
            for i in name_6_5:
                data_name.append(i)
        if len(data_name) > 0:
            data_name_set = list(set(data_name))
            test_name = [i for i in data_name_set if i != '']
            test_str_name = ';'.join(test_name)
        else:
            test_str_name = 'null'
        # sql = "update judgement_table_new_0717 set clear_about_patent='{}' where case_id='{}' and identify='专利名称'".format(
        #     test_str_name, case_id)
        sql = "insert into  caiduanwenshu_0728 values ('{}','{}','{}','专利名称')".format(case_id,fmt_content_n,test_str_name)
        db.execute_sql(sql)
        num += 1
        print('已清洗', num, '条')
    except Exception:
        num += 1
        with open('log.txt', 'a', encoding='utf-8') as aa:
            aa.write(case_id)
            aa.write('\n')