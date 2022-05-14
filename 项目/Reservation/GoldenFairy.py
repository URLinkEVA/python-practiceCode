"""
@Author: NephrenCake
@Date: 2022/5/11
@Desc: 黄金妖精会帮你完成……
"""
import json
import os
import time
import traceback
import requests

from random import random
from bs4 import BeautifulSoup


def json_to_dict(path):
    with open(path, 'rt', encoding='utf-8') as jsonFile:
        config_dict = json.load(jsonFile)
        return config_dict


class GoldenFairy:
    def __init__(self, conf_path="config.json"):
        self.conf = json_to_dict(conf_path)

        self.session = requests.Session()

        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'Connection': 'timeout=5',
            "Content-Type": "application/json",
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        }

    def login(self, service=None):
        if service is None:
            service = "https://u.njtech.edu.cn/oauth2/authorize"
        url = f'https://u.njtech.edu.cn/cas/login'
        # 获取i南工登录页面
        response = self.session.get(
            url=url,
            params={
                "service": service
            }
        )

        soup = BeautifulSoup(response.content, "html.parser")
        lt0 = soup.find('input', attrs={'name': 'lt'})['value']
        execution0 = soup.find('input', attrs={'name': 'execution'})['value']
        channel = self.conf["channel"]
        login_info = self.conf["loginInfo"]
        channelshow = login_info["channelshow"]

        # 登录
        response = self.session.post(
            url=url,
            params={
                "service": service
            },
            data={
                'username': login_info['username'],
                'password': login_info['password'],
                'channelshow': login_info['channelshow'],
                'channel': channel[channelshow],
                'lt': lt0,
                'execution': execution0,
                '_eventId': 'submit',
                'login': '登录',
            },
            allow_redirects=False
        )

        if "Expires" in response.headers.keys():
            print(f"成功连接校园网，成功连接[{login_info['channelshow']}]")
        return response

    def health(self):
        service = "http://pdc.njtech.edu.cn/#/dform/genericForm/wbfjIwyK"
        response = self.login(service)

        # 获取 token
        ticket = response.headers['Location'].split('?ticket=')[-1].split('#/')[0]
        response = self.session.get(
            url=f"http://pdc.njtech.edu.cn/dfi/validateLogin",
            params={
                "ticket": ticket,
                "service": service
            },
            headers=self.headers,
            allow_redirects=False
        )
        self.headers["Referer"] = f"http://pdc.njtech.edu.cn/?ticket={ticket}"
        self.headers["Authentication"] = json.loads(response.content)['data']['token']

        try:
            # 获取wid
            response = self.session.get("http://pdc.njtech.edu.cn/dfi/formOpen/loadFormListBySUrl?sUrl=wbfjIwyK",
                                        headers=self.headers, allow_redirects=False)
            wid = json.loads(response.content)['data'][0]['WID']

            # 获取历史提交记录
            response = self.session.get(
                f"http://pdc.njtech.edu.cn/dfi/formData/loadFormFillHistoryDataList?formWid={wid}&auditConfigWid=",
                headers=self.headers, allow_redirects=False)
            # 取最近一次提交数据，数据的结构和提交所需的结构不完全一致，进行修改后作为此次提交数据
            lastData = json.loads(response.content)["data"][0]
            dataMap = {
                "wid": "",
                "RADIO_KWYTQFSU": "本人知情承诺",  # 知情承诺
                "INPUT_KWYTQFSO": lastData['INPUT_KWYTQFSO'],  # 学号
                "INPUT_KWYTQFSP": lastData['INPUT_KWYTQFSP'],  # 姓名
                "SELECT_KX3ZXSAE": lastData['SELECT_KX3ZXSAE'],  # 学院
                "INPUT_KWYTQFSS": lastData['INPUT_KWYTQFSS'],  # 班级
                "INPUT_KX3ZXSAD": lastData['INPUT_KX3ZXSAD'],  # 手机号
                "INPUT_KWYUM2SI": lastData['INPUT_KWYUM2SI'],  # 辅导员
                "RADIO_KWYTQFSZ": lastData['RADIO_KWYTQFSZ'],  # 当前位置
                "RADIO_KWYTQFT0": lastData['RADIO_KWYTQFT0'],  # 所在省市区
                "CASCADER_KWYTQFT1": lastData['CASCADER_KWYTQFT1'][1:-1].split(', '),
                "RADIO_KWYTQFT2": lastData['RADIO_KWYTQFT2'],  # 身体状况
                "ONEIMAGEUPLOAD_KWYTQFT3": lastData['ONEIMAGEUPLOAD_KWYTQFT3'][1:-1].split(', '),  # 健康码
                "ONEIMAGEUPLOAD_KWYTQFT5": lastData['ONEIMAGEUPLOAD_KWYTQFT5'][1:-1].split(', '),  # 行程码
                "LOCATION_KWYTQFT7": lastData['LOCATION_KWYTQFT7'],  # 定位
            }

            # 构建AMID（不知道有啥意义，可能用于迷惑人，就是个时间戳，前面可能会加一个随机数，但是不加也可以）
            AMID = "AM@" + str(int(time.time() * 1000))

            # 发送表单数据
            postData = json.dumps({
                "auditConfigWid": "",
                "commitDate": time.strftime("%Y-%m-%d", time.localtime()),
                "commitMonth": time.strftime("%Y-%m", time.localtime()),
                "dataMap": dataMap,
                "formWid": wid,
                "userId": AMID,
            })
            response = self.session.post('http://pdc.njtech.edu.cn/dfi/formData/saveFormSubmitData',
                                         data=postData.encode("utf-8"), headers=self.headers, allow_redirects=False)
            if json.loads(response.content)["message"] == "请求成功":
                response = self.session.get(
                    f"http://pdc.njtech.edu.cn/dfi/formData/loadFormFillHistoryDataList?formWid={wid}&auditConfigWid=",
                    headers=self.headers, allow_redirects=False)
                print("健康打卡提交成功！\n此次提交的数据内容如下：\n" + json.dumps(json.loads(response.content)
                                                               ["data"][0], indent=0, separators=(', ', ': '),
                                                               ensure_ascii=False)[2:-1])
            else:
                print("❗❗❗\n健康打卡提交失败！\n数据提交失败，服务器未响应")
        except Exception as e:
            # 统一处理代码运行抛出的异常，通过通知提醒错误内容
            print("❗❗❗\n健康打卡提交失败！\n报错信息如下：\n" + traceback.format_exc())

    def library(self, where_to_go="逸夫图书馆"):
        self.login()

        # 1. get start: 获取 token
        start_url = "https://ehall.njtech.edu.cn/infoplus/form/TSGXY/start"
        response = self.session.get(
            url=start_url,
        )
        soup = BeautifulSoup(response.content, "html.parser")
        token = str(soup.find('meta', attrs={'itemscope': 'csrfToken'})).split('"')[1]

        # 2. post start: 获取 stepId 和 render_url
        self.headers["Referer"] = start_url
        response = self.session.post(
            url="https://ehall.njtech.edu.cn/infoplus/interface/start",
            data=json.dumps({
                "release": "",
                "formData": {"_VAR_URL": start_url, "_VAR_URL_Attr": {}}
            }),
            params={
                "idc": "TSGXY",
                "csrfToken": token,
            },
            headers=self.headers
        )
        render_url: str = json.loads(response.content)["entities"][0]
        stepId = int(render_url.split("/")[-2])
        # print("render_url", render_url)
        # print("stepId", stepId)

        # 3. post render: 获取个人信息
        self.headers["Referer"] = render_url
        response = self.session.post(
            url="https://ehall.njtech.edu.cn/infoplus/interface/render",
            params={
                "stepId": stepId,
                "csrfToken": token,
            },
            headers=self.headers
        )
        content = json.loads(response.content)
        formData: dict = content["entities"][0]["data"]
        assignTime = content["entities"][0]["step"]["assignTime"]
        # print(formData)
        # print(assignTime)

        # 4. post listNextStepsUsers: 合理预约图书馆入场券
        for k, v in formData.items():
            formData[k] = str(v)
        formData["fieldXq_Name"] = where_to_go
        formData["fieldXq"] = "1" if where_to_go == "逸夫图书馆" else "2"
        formData["_VAR_ENTRY_NAME"] = "图书馆预约申请"
        formData["_VAR_ENTRY_TAGS"] = "预约服务"
        formData["_VAR_RELEASE"] = "true"
        formData["fieldDateTo"] = int(formData["_VAR_TODAY"])  # 只能预约当天
        formData["fieldDateFrom"] = int(formData["fieldDateFrom"])  # 只能预约当天
        # formData["fieldJzzt"] = "星期五"  #
        # formData["fieldKyy"] = "57"  #
        # formData["fieldYyy"] = "1143"  # 三个废物字段

        response = self.session.post(
            url="https://ehall.njtech.edu.cn/infoplus/interface/listNextStepsUsers",
            headers=self.headers,
            params={
                "stepId": stepId,
                "actionId": 1,
                "formData": json.dumps(formData).encode("utf-8"),
                "timestamp": assignTime,
                "rand": random() * 999,
                "csrfToken": token,
            },
        )
        # print("response ", response)
        # print("response headers", response.headers)
        response = json.loads(response.content)
        # print("response json", response)

        if response["ecode"] == "SUCCEED":
            print("预约成功")
        elif response["ecode"] == "EVENT_CANCELLED":
            print("已经预约")
        elif response["ecode"] == "BAD_PARAMETERS":
            print("参数错误")
        elif response["ecode"] == "USER_LOGIN_REQUIRED":
            print("登录超时")


if __name__ == '__main__':
    c = GoldenFairy()
    # c.login()
    # c.health()
    c.library()
