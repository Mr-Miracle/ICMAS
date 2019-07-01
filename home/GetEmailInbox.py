from exchangelib import *
import pymysql
import time
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


class AccountInfo:
    username = r'lujihao'
    password = r'123456@a'
    EmailAddress = r'lujihao@inspur.com'
    datetime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))


class EmailInfo:
    credentials = Credentials(
        username=AccountInfo.username,
        password=AccountInfo.password,
    )
    account = Account(
        primary_smtp_address=AccountInfo.EmailAddress,
        credentials=credentials,
        autodiscover=True
    )

    try:
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("localhost", "root", "1", "ICMASDB")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        print("SYSInfo", AccountInfo.datetime, "数据库连接成功")

    except Exception as e:
        print("SYSInfo", AccountInfo.datetime, e)
        print("SYSInfo", AccountInfo.datetime, "数据库连接失败")

    for item in account.inbox.all().order_by('-datetime_received')[:10]:
        subject = str(item.subject)
        # 用正则表达式获取邮件的发件人名称
        # re.findall(re.compile('name=.{10}'),str(item.sender))
        sender = str(item.last_modified_name)
        # 截取日期的字符串字段
        received = str(item.datetime_received)[0:19]
        print("SYSInfo", AccountInfo.datetime, "获取到的数据为：", "[", subject, sender, received, "]")
        # 使用预处理语句插入获取的邮箱数据
        V_SQL = "INSERT INTO home_mailbox(subject,sender, received, create_datetime, modify_datetime) " \
                "VALUES ("+"'"+subject+"','"+sender+"','"+received+"','"+received+"','"+received+"')"
        try:
            print(V_SQL)
            cursor.execute(V_SQL)
            db.commit()
            print("SYSInfo", AccountInfo.datetime, "此条数据插入成功")

        except Exception as e:
            print("SYSInfo", AccountInfo.datetime, e)
            db.rollback()
            print("SYSInfo", AccountInfo.datetime, "数据插入失败，已回滚！！！")

    # 关闭数据库连接
    db.close()




