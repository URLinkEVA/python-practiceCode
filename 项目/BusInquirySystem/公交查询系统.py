import os
import pickle


def main():  # 主函数
    while True:
        print('-' * 30)
        print('------菜单------')
        print('1.线路查询')
        print('2.站点查询')
        print('3.换乘信息')
        print('4.后台管理员界面')
        print('5.管理员的账号管理界面')
        print('6.退出程序')
        print('-' * 30)
        num = int(input('请选择你的操作：\n'))
        if num == 1:
            line_find()
            continue
        if num == 2:
            site_find()
            continue
        if num == 3:
            change_line()
            continue
        if num == 5:
            manager_account()
            continue
        if num == 6:
            break
        if num == 4:
            manager()
            continue
        else:
            print('请重新做出你的选择！！')


def manager_account():  # 管理员账号管理界面的函数
    def new_():
        file_path = 'D:\公交查询系统\info.pkl'
        a = input('请设置你的账号：')
        b = input('请设置入你的密码：')
        w = input('请再次输入你的的密码：')
        d = {
            'user': a,
            'password': b
        }
        if b == w:
            if os.path.exists(file_path) and os.path.getsize(file_path):
                o = open('info.pkl', 'rb')
                m = pickle.load(o)
                with open('info.pkl', 'ab') as fp:
                    pickle.dump(d, fp)
                print('您已经注册成功！！')
            else:
                with open('info.pkl', 'wb') as fp:
                    pickle.dump(d, fp)
                print('您已经注册成功！！')
        else:
            print('对不起，你两次输入的密码不一致，请您重新输入！！')

    def xiaohui():
        h = open('info.pkl', 'w+')  # 清空文件里的内容。。。
        h.truncate()
        print('你已经销毁成功。。。')

    while True:
        print('-----管理员的账号管理界面------\n'
              '1.注册\n'
              '2.注销原有的所有账户\n'
              '3.退出管理员的账号管理界面')
        choice = input('请做出你的选择：\n')
        if choice == '1':
            new_()
        if choice == '2':
            xiaohui()
        elif choice == '3':
            print('-' * 35)
            print('------菜单------')
            print('1.线路查询')
            print('2.站点查询')
            print('3.换乘信息')
            print('4.后台管理员界面')
            print('5.管理员的账号管理界面')
            print('6.退出程序')
            print('-' * 35)
            break
        else:
            print('请重新做出你的选择')


def login():  # 用户登录的函数
    with open('info.pkl', 'rb') as fp:
        q = input('请输入你的的账号：')
        w = input('请输入你的的密码：')
        while True:
            try:
                data = pickle.load(fp)
                if q == data['user'] and w == data['password']:
                    print('您已经登录成功！！！')
                    return True

            except:
                break


def manager():  # 后台管理员界面的函数
    if login():
        while True:
            print('-' * 30)
            print('-----后台管理员界面-----')
            print('1.添加线路')
            print('2.删除线路')
            print('3.修改线路')
            print('4.查看所有线路')
            print('5.删除所有线路')
            print('6.退出')
            print('-' * 30)
            num = input('请做出你的选择:\n')
            if num == '3':
                revise_line()
                continue
            if num == '1':
                add_line()
                continue
            if num == '6':
                print('-' * 25)
                print('------菜单------')
                print('1.线路查询')
                print('2.站点查询')
                print('3.换乘信息')
                print('4.后台管理员界面')
                print('5.管理员的账号管理界面')
                print('6.退出程序')
                print('-' * 25)
                break
            if num == '5':
                clear_line_all()
                continue
            if num == '4':
                show_line_all()
                continue
            if num == '2':
                clear_line()
                continue
            else:
                print('请重新做出你的选择...')
    else:
        print('对不起，你登录失败，不可以让您进入后台管理员界面')


def revise_line():  # 定义修改线路的函数
    num = input('请输入您要修改的线路：')
    if check_add_line(num):
        print('您要修改的线路已经存在了。。。。')
        show_line_all()
        tag = input('请确认是否继续修改线路：(1为是，0为否)\n')
        if tag == '1':
            line = input('请再次确认你要修改的线路：\n')
            site = input('请输入你修改后的站点：\n')
            with open('line_info.pkl', 'rb') as fp:
                ls = []
                while True:
                    try:
                        data = pickle.load(fp)
                        # 遍历字典
                        for key, value in data.items():
                            if line in key:
                                ls.append({str(line): str(site)})
                            else:
                                ls.append(data)
                    except:
                        break
                save_data(ls)  # 存储修改后的数据
                print("您已经修改成功了！！！！")
    else:
        print('您要修改的线路不存在，需要创建一个新的线路。。。')
        add_line()


def line_check(num):  # 判断是否存在线路的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                if num in data:
                    print(f'{num}号线的路线经过的站点为{data[num]}')
                    return True
            except:
                break


def line_find():  # 线路查询的函数
    num = input('请输入你要查询的线路：\n')
    if line_check(num):
        pass
    else:
        print('您要查找的线路不存在....')


def site_check():  # 判断站点是否存在的函数
    with open('line_info.pkl', 'rb') as fp:
        num = input('请输入你要查询的站点名：\n')
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    ls = str(value)
                    if num in ls:
                        print(f'经过{num}站点的线路为{key}号线')
                        return True
            except:
                break


def site_find():  # 站点查询的函数
    if site_check():
        pass
    else:
        print('您要查询的站点不存在.....')


def check_add_line(num):  # 检查添加线路是否存在的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    if num in key:
                        return True
            except:
                break


def add_line():  # 添加线路的函数
    file_path = 'D:\公交查询系统\line_info.pkl'
    a = input('请输入添加的线路：')
    b = input('请输入经过的站点：')
    d = {
        a: {b}
    }
    if os.path.exists(file_path) and os.path.getsize(file_path):
        if check_add_line(a):
            print('您要添加的线路已经存在了......')
        else:
            with open('line_info.pkl', 'ab') as f:
                pickle.dump(d, f)
            print('您已经添加线路成功！！')
    else:
        with open('line_info.pkl', 'wb') as fp:
            pickle.dump(d, fp)
        print('您已经添加线路成功了！！')


def clear_line_all():  # 清楚所有线路的函数
    h = open('line_info.pkl', 'w+')  # 清空文件里的内容。。。
    h.truncate()
    print('你已经销毁成功。。。')


def show_line_all():  # 展示所有线路的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    print(f'{key}线路经过的站点是{value}')
            except:
                break


def clear_line():  # 删除线路的函数
    with open('line_info.pkl', 'rb') as fp:
        num = input('请输入你要删除的线路：\n')
        ls = []
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    if num in key:
                        pass
                    else:
                        ls.append(data)
            except:
                break
        save_data(ls)


def line_check(num):  # 判断是否存在线路的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                if num in data:
                    print(f'{num}号线的路线经过的站点为{data[num]}')
                    return True
            except:
                break


def show_site(num):  # 展示特定线路中的站点的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                if num in data:
                    return data[num]
            except:
                break


def change_line():  # 换乘信息的函数
    begin = input('请输入你的起点站点：\n')
    end = input('请输入你的终点站点：\n')
    if direct_line(begin, end):
        pass
    else:
        ls = []
        ls_ = []
        tag = True
        data = check_site(begin, end)
        # print(type(data[0]),type(data[1]))
        print(f'经过{begin}站点的线路为：{data[0]}，经过{end}站点的线路为{data[1]}')  # 判断经过起始点和终点的对应线路
        for i in range(len(list(data)[0])):
            ls.append(show_site(data[0][i]))
            print(f"{line_check(str(data[0][i]))}")
        for j in range(len(list(data)[1])):
            ls_.append(show_site(data[1][j]))
            print(f"{line_check(str(data[1][j]))}")
        for i in ls:  # i为集合的形式
            for a in list(i):
                for b in str(a).split(' '):  # 切割字符串
                    if b in str(ls_):  # 判断是否存在相同的站点
                        tag = False
                        print(f"您可以通过从{data[0]}号线的{b}站转到{data[1]}号线来到达目的地！！")
        if tag == True:
            print('对不起，无法通过换乘来到达目的地')


def direct_line(begin, end):  # 判断线路直达的函数
    with open('line_info.pkl', 'rb') as fp:
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    ls = str(value)
                    if begin in ls and end in ls:
                        print(f'您可以通过{key}号线路直接到达')
                        return True
            except:
                break


def save_data(ls):  # 存储数据的函数
    with open('line_info.pkl', 'wb') as fp:
        for data in ls:
            pickle.dump(data, fp)


def check_site(begin, end):  # 判断站点所在的线路的函数。
    with open('line_info.pkl', 'rb') as fp:
        ls = []
        ls_ = []
        while True:
            try:
                data = pickle.load(fp)
                # 遍历字典
                for key, value in data.items():
                    ls1 = str(value)
                    if begin in ls1:
                        ls.append(key)
                    if end in ls1:
                        ls_.append(key)
            except:
                break
        return ls, ls_


# def help_change_line_info(i, j):
#     with open('line_info.pkl', 'rb') as fp:
#         ls = []
#         ls_ = []
#         while True:
#             try:
#                 data = pickle.load(fp)
#                 # 遍历字典
#                 for key, value in data.items():
#                     ls1 = str(key)
#                     if i in ls1:
#                         ls.append(value)
#                     if j in ls1:
#                         ls_.append(value)
#             except:
#                 break
#         return ls, ls_


if __name__ == 'main':
    main()

main()
