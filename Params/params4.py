import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
工单对接流程数据
"""
def get_parameter(name):
    #将tools封装成函数
    data = tools1.parse()
    param = data[name]["test"]["request"]
    return param

class Login_00():
    params = get_parameter('张越冀账号登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class createtask_01():
    params = get_parameter('创建发起流程')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_03():
    params = get_parameter('环节1保存意见')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveform_04():
    params = get_parameter('环节1保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_05():
    params = get_parameter('环节1保存更新')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_06():
    params = get_parameter('推送市局娄军军个人所得税处')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_07():
    params = get_parameter('娄军军登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class savety_08():
    params = get_parameter('市局接收岗保存意见')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_09():
    params = get_parameter('推送市局处理岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_10():
    params = get_parameter('徐俊登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]


class savety_11():
    params = get_parameter('市局处理岗保存意见')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveform_12():
    params = get_parameter('市局处理岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_13():
    params = get_parameter('市局处理岗保存更新')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_14():
    params = get_parameter('推送市局签发岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_15():
    params = get_parameter('王毅平登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class savety_16():
    params = get_parameter('市局签发岗保存意见')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_17():
    params = get_parameter('推送校稿')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class getform_18():
    params = get_parameter('获取校稿表单')
    url = params["url"]
    data = params["params"]
    header = params["headers"]

class savety_19():
    params = get_parameter('汇总校稿保存意见')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveform_20():
    params = get_parameter('保存汇总校稿form')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_21():
    params = get_parameter('保存汇总校稿工单数据')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_22():
    params = get_parameter('推送到稽查局13100540666江帆')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_23():
    params = get_parameter('江帆登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class savety_24():
    params = get_parameter('稽查局不同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_25():
    params = get_parameter('不同意回推汇总分发')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_26():
    params = get_parameter('再次转给稽查局')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_27():
    params = get_parameter('稽查局接收岗同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_28():
    params = get_parameter('推送到稽查处理岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_29():
    params = get_parameter('稽查处理岗同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_30():
    params = get_parameter('推送到稽查局签收岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_31():
    params = get_parameter('稽查局签发岗同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_32():
    params = get_parameter('稽查局签发岗推送汇总校稿')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_33():
    params = get_parameter('转分局流程同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_34():
    params = get_parameter('转分局流程保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_35():
    params = get_parameter('汇总分发继续转分局接收岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_36():
    params = get_parameter('潘耀平登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class savety_37():
    params = get_parameter('分局接收岗保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_38():
    params = get_parameter('分局接收岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_39():
    params = get_parameter('分局接收岗浦东转其他科室')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_40():
    params = get_parameter('业务科室接收岗保存同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_41():
    params = get_parameter('业务科室接收岗推送处理岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_42():
    params = get_parameter('业务处理岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_43():
    params = get_parameter('业务处理岗保存同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_44():
    params = get_parameter('业务科室处理岗推送签发岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_45():
    params = get_parameter('业务签发岗同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_46():
    params = get_parameter('业务科室签发岗推送各区税务局汇总岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdate_47():
    params = get_parameter('各区汇总表单保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class savety_48():
    params = get_parameter('各区汇总同意')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_49():
    params = get_parameter('推送各区税务局汇总签发岗')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_08():
    params = get_parameter('市局接收岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_16():
    params = get_parameter('市局签收岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_24():
    params = get_parameter('稽查局不同意保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_27():
    params = get_parameter('稽查局接收岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_29():
    params = get_parameter('稽查局处理岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_31():
    params = get_parameter('稽查局签发岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_40():
    params = get_parameter('业务科室接收岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class saveupdata_45():
    params = get_parameter('业务签发岗保存表单')
    url = params["url"]
    data = params["json"]
    header = params["headers"]