#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import pymysql
import random
import string
import time

def init_admin(mydb, mycursor, size):
    admin_sql = "insert into Admin (adminID, name) VALUES (%s, %s)"
    for i in range(size):
        rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(3, 7)))
        val = (i, rand_str)
        mycursor.execute(admin_sql, val)
        mydb.commit()

def init_user(mydb, mycursor, size):
    user_sql = "insert into `User` (user_id, is_banned) VALUES (%s, %s)"
    employee_sql = "insert into employee (user_id, is_banned, `name`, `identity`) VALUES (%s, %s, %s, %s)"
    employer_sql = "insert into employer (user_id, is_banned, `name`, address, category) VALUES (%s, %s, %s, %s, %s)"

    default_address = ["Beijing", "Shanghai", "Chongqing", "Sichuan", "Zhejiang", "Jiangsu"]
    default_category = ["web", "sale", "food", "test1", "test2", "test3", "test4"]

    employers = []
    employees = []

    for i in range(size):
        val_user = (i, 0)
        mycursor.execute(user_sql, val_user)
        mydb.commit()

        rand = random.random()
        if rand > 0.9:
            rand_str = ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(3, 7)))
            rand_address = random.choice(default_address)
            rand_catelog = random.choice(default_category)
            val_employer = (i, 0, rand_str, rand_address, rand_catelog)
            mycursor.execute(employer_sql, val_employer)
            mydb.commit()
            employers.append(i)
        else:
            rand_name = ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(3, 7)))
            rand_identity = ''.join(
                random.choice(string.digits) for _ in range(15))
            val_employee = (i, 0, rand_name, rand_identity)
            mycursor.execute(employee_sql, val_employee)
            mydb.commit()
            employees.append(i)
    return [employees, employers]

def init_job(mydb, mycursor, size, employers):
    a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    index = 0
    job_sql = "insert into job (salary, job_detail, begin_time, end_time, job_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    for i in range(size):
        salary = round(random.randrange(1000, 1000000), 1)
        rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50)))
        begin_time = random.randint(start, end)
        end_time = random.randint(start, end)
        if(end_time <= begin_time):
            continue
        val = (salary, rand_str, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(begin_time)),
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)), index, random.choice(employers))
        try:
            mycursor.execute(job_sql, val)
            mydb.commit()
            index = index + 1
        except pymysql.err.IntegrityError as e:
            print("error job: " + str(e))
            continue
    return index

def init_comment(mydb, mycursor, size, size_of_user, size_of_job):
    a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    index = 0
    comment_sql = "insert into comment (comment_id, user_id, job_id, content, `time`, is_blocked) VALUES (%s, %s, %s, %s, %s, %s)"
    for i in range(size):
        rand_uid = random.randint(0, size_of_user)
        rand_jid = random.randint(0, size_of_job)
        rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50)))
        comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random.randint(start, end)))
        val = (index, rand_uid, rand_jid, rand_str, comment_time, random.randint(0, 1))
        try:
            mycursor.execute(comment_sql, val)
            mydb.commit()
            index = index + 1
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue
    return index

def init_comment_love_report(mydb, mycursor, size, size_of_user, size_of_comment):
    sql = "insert into comment_love_report (user_id, comment_id, love, report) VALUES (%s, %s, %s, %s)"
    for i in range(size):
        rand_owner = random.randint(0, size_of_user)
        rand_target = random.randint(0, size_of_comment)
        val = (rand_owner, rand_target, random.randint(0, 1), random.randint(0, 1))
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_job_love_report(mydb, mycursor, size, size_of_user, size_of_job):
    sql = "insert into job_love_report (user_id, job_id, love, report) VALUES (%s, %s, %s, %s)"
    for i in range(size):
        rand_owner = random.randint(0, size_of_user)
        rand_target = random.randint(0, size_of_job)
        val = (rand_owner, rand_target, random.randint(0, 1), random.randint(0, 1))
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_user_love_report(mydb, mycursor, size, size_of_user):
    sql = "insert into user_love_report (use_user_id, user_id, love, report) VALUES (%s, %s, %s, %s)"
    for i in range(size):
        rand_owner = random.randint(0, size_of_user)
        rand_target = random.randint(0, size_of_user)
        if(rand_owner == rand_target):
            continue
        val = (rand_owner, rand_target, random.randint(0, 1), random.randint(0, 1))
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_apply(mydb, mycursor, size, employees, size_of_job):
    a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    sql = "insert into apply (user_id, job_id, `time`) VALUES (%s, %s, %s)"
    for i in range(size):
        rand_uid = random.choice(employees)
        rand_jid = random.randint(0, size_of_job)
        rand_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random.randint(start, end)))
        val = (rand_uid, rand_jid, rand_time)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_follow_black(mydb, mycursor, size, users_log):
    sql = "insert into follow_unfollow_black (emp_user_id, user_id, follow, black) VALUES (%s, %s, %s, %s)"
    for i in range(size):
        rand_employer = random.choice(users_log[0])
        rand_employee = random.choice(users_log[1])
        val = (rand_employer, rand_employee, random.randint(0, 1), random.randint(0, 1))
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_send_receive(mydb, mycursor, size, users_log):
    a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    sql = "insert into send_receive_message (emp_user_id, user_id, `time`, content) VALUES (%s, %s, %s, %s)"
    for i in range(size):
        rand_employer = random.choice(users_log[0])
        rand_employee = random.choice(users_log[1])
        rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50)))
        rand_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random.randint(start, end)))
        val = (rand_employer, rand_employee, rand_time, rand_str)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def init_skill_tag(mydb, mycursor, size, employees, size_of_job):
    default_skill = ["java", "python", "c", "c++", "mysql", "c#", "go", "javascript", "test1", "test2", "test3"]
    size_of_skill_tag = len(default_skill)
    skill_tag_sql = "insert into skill_tag (skill_id, content) VALUES (%s, %s)"
    for i in range(size_of_skill_tag):
        skill_val = (i, default_skill[i])
        mycursor.execute(skill_tag_sql, skill_val)
        mydb.commit()

    employee_skill_sql = "insert into employee_skill (user_id, skill_id) VALUES (%s, %s)"
    job_skill_sql = "insert into job_skill (job_id, skill_id) VALUES (%s, %s)"
    for i in range(size):
        rand_uid = random.choice(employees)
        employee_val = (rand_uid, random.randint(0, size_of_skill_tag))
        try:
            mycursor.execute(employee_skill_sql, employee_val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue
    for i in range(size):
        rand_jid = random.randint(0, size_of_job)
        job_val = (rand_jid, random.randint(0, size_of_skill_tag))
        try:
            mycursor.execute(job_skill_sql, job_val)
            mydb.commit()
        except pymysql.err.IntegrityError as e:
            print("error: " + str(e))
            continue

def main():
    mydb = pymysql.connect("localhost", "zpapp", "zpapp", "zpapp")
    mycursor = mydb.cursor()

    size_of_admin = 10000 #admin表的大小
    print("init admin of size: " + str(size_of_admin))
    init_admin(mydb, mycursor, size_of_admin)

    size_of_user = 1000000 #user表的大小，同时生成继承自它的employer和employee
    print("init user, employee and employer of size: " + str(size_of_user))
    users_log = init_user(mydb, mycursor, size_of_user) #users_log[0] for employees, users_log[1] for employers

    temp_size_of_job = 1000000 #job表的尝试次数
    print("init job of size: " + str(temp_size_of_job))
    size_of_job = init_job(mydb, mycursor, temp_size_of_job, users_log[1])

    temp_size_of_comment = 100000 #comment表的尝试次数
    print("init comment of size: " + str(temp_size_of_job))
    size_of_comment = init_comment(mydb, mycursor, temp_size_of_comment, size_of_user, size_of_job)

    size_of_comment_love_report = 1000000  # job_love_report表的大小
    print("init comment_love_report of size: " + str(size_of_comment_love_report))
    init_comment_love_report(mydb, mycursor, size_of_comment_love_report, size_of_user, size_of_comment)

    size_of_job_love_report = 1000000 #job_love_report表的大小
    print("init job_love_report of size: " + str(size_of_job_love_report))
    init_job_love_report(mydb, mycursor, size_of_job_love_report, size_of_user, size_of_job)

    size_of_user_love_report = 1000000 #user_love_report表的大小
    print("init user_love_report of size: " + str(size_of_user_love_report))
    init_user_love_report(mydb, mycursor, size_of_user_love_report, size_of_user)

    size_of_apply = 1000000
    print("init apply of size: " + str(size_of_apply))
    init_apply(mydb, mycursor, size_of_apply, users_log[0], size_of_job)

    size_of_follow = 1000000
    print("init follow_unfollow_black of size: " + str(size_of_follow))
    init_follow_black(mydb, mycursor, size_of_follow, users_log)

    size_of_message = 1000000
    print("init send_receive_message of size: " + str(size_of_message))
    init_send_receive(mydb, mycursor, size_of_message, users_log)

    size_of_skill = 100000
    print("init skill_tag, employee_skill and job_skill of size: " + str(size_of_skill))
    init_skill_tag(mydb, mycursor, size_of_skill, users_log[0], size_of_job)

if __name__ == "__main__":
    main()