import requests
import json
import time

"""

主要功能：

抓取 Python 四期同学仓库任务提交情况。

"""

__version__ = '170823 0:20_'
__author__ = 'zhuoxuan'


workmate = ['ouyangzhiping','badboy315','huijuannan','hscspring','ishanshan','yangshaoshun','RamyWu','scottming','bambooom','serena333','uniquenaer','Rebecca19','iamzhuoxuan','Mina-yy','LexieLee','AwesomeJason']
py104oc = ['ZoomQuiet','zoejane','Wangjunyu','faketooth','wilslee','simpleowen','omclub','fatfox2016','gzMichael']
all_non_stu = workmate + py104oc

check_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

start_issue = [10,43,67]
end_issue = [13,46,70]

all_stu = {}
all_stu_list = []

with open('py104_all_stu.txt','r',encoding = 'utf-8') as f:
    for line in f.readlines():
        temp = line.strip('\n').split(',')
        all_stu.update({temp[0]:temp[1]})
        all_stu_list.append(temp[0])

print(all_stu_list)
print('======')



for i in range(len(start_issue)):
    chap_allstu_name = []
    all_stu_comment_num = ['ch'+str(i),check_time]
    print(all_stu_comment_num)
    for x in range(start_issue[i],end_issue[i]+1):
        r = requests.get('https://api.github.com/repos/AIHackers/Py101-004/issues/'+str(x)+'/comments?page=1&per_page=100', auth=('iamzhuoxuan', 't{vu.VvEFFPyWi42'))
        print('https://api.github.com/repos/AIHackers/Py101-004/issues/'+str(x)+'/comments')
        raw_comment_count = r.json()
        #print(json.dumps(raw_comment_count, sort_keys=True, indent=4))
        all_comment_user = []
        task_link = []
        count = 0
        for i in raw_comment_count:
            first_dict = i
            for k,v in first_dict.items():
                if k == 'user':
                    second_dict = v
                    count +=  1
                    for k,v in second_dict.items():
                        if k == 'login':
                            all_comment_user.append(v)
                if k == 'html_url':
                    task_link.append(v)

        #print(all_comment_user)
        #print(task_link)

        #print(all_non_stu)
        #print('总 comment：')
        #print(len(all_comment_user))
        #print(len(task_link))
        contrast_a = set(all_non_stu)
        contrast_b = set(all_comment_user)

        #print('学员 comment 数：')
        all_stu_comment = list(contrast_b.difference(contrast_a))
        all_stu_comment_area_num = len(all_stu_comment)
        #print(all_stu_comment_area_num)
        all_stu_comment_num.append(all_stu_comment_area_num)
        #print(all_stu_comment,'all_stu_comment')
        chap_allstu_name.extend(all_stu_comment)



        #print(all_stu_comment)
        #for i in all_stu_comment:
        #    print(i)

    #print(all_stu_comment_num)


    print('-------- chap_allstu_name below------')
    print(chap_allstu_name)
    print(len(chap_allstu_name),'已交总人数')
    print('--------upload------')

    print(len(all_stu.keys())-len(chap_allstu_name),'人未提交作业')

    for item in all_stu.keys():
        if item not in chap_allstu_name:
            print(item,',',all_stu[item])

    record_file1 = open('all_stu_comment_num1.txt', 'a')

    record_file1.write('\n')
    for item in all_stu_comment_num:
        record_file1.write("%s\n" % item)
    record_file1.write('\n'+'-'*10)
    record_file1.write('\n')

    record_file2 = open('all_stu_comment_num2.txt', 'a')
    record_file2.write("%s\n" % all_stu_comment_num)
    #print('========')


# changelog
# v0.1.0 能够自动抓取、在 cli 打印某一章节任务完成人数（技术点：requests json 动态网页链接 阅读技术文档）
# v0.2.0 将抓取到的数据，写入 txt 文档，增加章节信息及查询时间信息
# v0.3.0 每周发布新任务后，简单改写列后，可自动读取所有章节完成人数
# v0.3.1 临时需求：计算各章未交作业名单，读取其邮箱 -> 嵌套越来越多了，要解决这个问题 -> 改装为函数
# 计划
# v0.3.2 封装为函数，依 PEP8 规范改写代码
