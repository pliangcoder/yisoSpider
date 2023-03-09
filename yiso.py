import sys
import requests
import json
import datetime
from win10toast import ToastNotifier
from random_sleep import random_sleep
import random

"""
readme:
yiso（易搜网站）爬虫 
网址：https://yiso.fun
"""


def get_json_files(url):  # 请求数据的函数
    try:
        response = requests.get(url, headers=__yiso_headers, timeout=20)
        jsonfiles = response.json()
        response.close()
        return jsonfiles
    except:
        response = requests.get(url, headers=__yiso_headers, timeout=20)
        if response.status_code == [300, 400]:
            print(f"-----------------------{search_name}结束------------------------")
            _new_search_list = search_list.remove(search_name)
            return _new_search_list


def _analysis_equipment(json_file):  # 解析函数  核心逻辑

    _analysis_failed = 0
    if json_file is None:
        return _analysis_failed  # 如果没有数据返回失败
    else:
        for num in range(0, 10):
            if json_file["data"]["list"][num]["creatorName"] == "老***盘":  # 标题党跳过
                pass
            else:
                aliyunurl = json_file["data"]["list"][num]["url"]  # 解析数据
                file_name = json_file["data"]["list"][num]["fileInfos"][0]["fileName"]
                if int(switch_mode) == 1:
                    if (file_name == search_name) or (file_name in search_name) or (search_name in file_name):  #
                        # 查询字符串是否在字符串中
                        if aliyunurl in url_list:  # 数组去重
                            pass
                        elif file_name in name_list:  # 名字数组去重
                            pass
                        elif aliyunurl in compare_list:  # 文件去重，防止重复 抓取
                            pass
                        else:
                            print("---------精准查找找到-------")
                            print(file_name + "链接： " + " " + aliyunurl)

                            url_list.append(aliyunurl)
                            name_list.append(file_name)
                else:

                    if aliyunurl in url_list:  # 数组去重
                        pass
                    elif file_name in name_list:  # 名字去重
                        pass
                    elif aliyunurl in compare_list:  # 文件去重，防止重复 抓取
                        pass
                    else:
                        if file_name == search_name:
                            print(f"---------------精准找到——————————url ={aliyunurl}")
                            print(f"---------------精准找到——————————url ={aliyunurl}")
                            print(f"---------------精准找到——————————url ={aliyunurl}")
                        print(file_name + "链接： " + " " + aliyunurl)
                        url_list.append(aliyunurl)
                        name_list.append(file_name)
        _analysis_failed = 1
        return _analysis_failed

    #     try:
    #         if end_time is None or end_time is None:
    #             time.sleep(*start_time)
    #         elif end_time in None and end_time is None:
    #             time.sleep(2)
    #         else:
    #
    #             else:
    #                 raise "error type"
    #     except:
    #         time.sleep(2)
    # except:
    #     raise "error type"

    # if start_time - int(start_time) or end_time - int(end_time) != 0:  # 判断是不是整数
    #
    #     time.sleep(random.uniform(start_time, end_time))
    # else:
    #     time.sleep(random.randint(start_time, end_time))


def save_url_and_name_into_file(url_lists, name_lists):  # 文件保存
    f = open("url_path/url.txt", mode="a+", encoding="utf-8")
    kong = "                                   "
    f.write(kong)
    f.write("\n")
    f.write(kong)
    files_time = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    f_times = f"<---文件写入时间--->>>>>  {files_time}"
    f.write(f_times)
    f.write('\n')
    for aliyun_url_name, aliyun_url in zip(name_lists, url_lists):  # 用zip函数同时遍历两个列表
        f.write("标题：")
        f.write(aliyun_url_name)
        f.write("   ")
        f.write("链接:   ")
        f.write(aliyun_url)
        f.write("\n")
    f.close()


def read_url_files():
    f = open("urlpath/url.txt", mode="r", encoding="utf-8")
    content = f.readlines()
    for line in content:
        url = line.strip().split("链接:")[-1].strip()
        init_list.append(url)
    return init_list


def get_random_useragent():  # 构造随机请求头
    f = open(r"F://Note//url_path//headers_list.json", mode="r", encoding="utf-8")
    agent = json.load(f)
    every_agent_list = agent["headers"]["Chrome"]
    suji_agent = random.choice(every_agent_list)
    return suji_agent


agent = get_random_useragent()
__yiso_headers = {"authority": "yiso.fun",
                  "method": "GET",
                  "path": "/",
                  "scheme": "https",
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                            "application/signed-exchange;v=b3;q=0.9",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                  "cache-control": "max-age=0",
                  "cookie": "__51vcke__JkIGvjjs25ETn0wz=01d86e4a-fb88-5d28-a700-69b388a8c643; "
                            "__51vuft__JkIGvjjs25ETn0wz=1672143403975; "
                            "__vtins__JkIGvjjs25ETn0wz=%7B%22sid%22%3A%20%22fc76e38e-fe83-5574-8f0a-5d2d3e567cd3%22"
                            "%2C%20"
                            "%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A"
                            "%201673508000774%2C%20%22ct%22%3A%201673506200774%7D; __51uvsct__JkIGvjjs25ETn0wz=14",
                  "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
                  "sec-ch-ua-mobile": "?0",
                  "sec-ch-ua-platform": "\"Windows\"",
                  "sec-fetch-dest": "document",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-site": "none",
                  "sec-fetch-user": "?1",
                  "upgrade-insecure-requests": "1",
                  "user-agent": agent}


def information():
    toaster = ToastNotifier()
    toaster.show_toast("python information",
                       "文件保存成功",
                       icon_path=r"C://Users//14927//Pictures//Camera Roll/python3png.ico",
                       duration=10)


if __name__ == "__main__":
    search_list = input("输入你要搜索的内容用空格隔开：").split(" ")  #
    switch_mode = input("输入你想查询的方式1：精准查询，2：模糊查询.")
    if search_list[-1] == " " or None:
        search_list.remove(search_list[-1])
    else:
        print("---------开始爬取-------")
        url_list = []
        name_list = []
        init_list = []
        print("---------loading-----")
        compare_list = read_url_files()
        print("---------正在读取本地url-----")
        for _content in range(0, len(search_list)):
            search_name = search_list[_content]
            for page in range(1, 100):
                random_sleep(1, 3)
                main_url = f"https://yiso.fun/api/search?name={search_name}&pageNo={page}"
                try:
                    print(f"-----------------------当前正在解析第{page}页-----------------------")
                    jsonFile = get_json_files(main_url)
                    if page % 7 == 0:  # 回退模拟
                        print("----回退一次--------")
                        resp = requests.get(
                            f"https://yiso.fun/api/search?name={search_name}&pageNo={page - 1}")
                        _analysis_equipment(resp.json())
                        random_sleep(1, 2.5)
                    else:
                        analysis_code = _analysis_equipment(jsonFile)
                        if analysis_code == 0:
                            print("-----解析失败-----response为空------")
                        else:
                            random_sleep(1, 2.5)
                except:
                    new_search_list = get_json_files(main_url)
                    for new_content in new_search_list:
                        newname = new_search_list[new_content]
                        random_sleep(2, 4)
                        for var in range(1, 10):
                            main_url = f"https://yiso.fun/api/search?name={newname}&pageNo={page}"
                    break
            print(f"--------{search_name} end------")
        try:
            if not len(url_list):
                print("------failed 没找到-------")
                print("------failed 没找到-------")
                sys.exit()
            else:
                save_url_and_name_into_file(url_list, name_list)
                name_list = []
                url_list = []
                print("----end----")
                information()
                sys.exit()
        except:
            sys.exit()
