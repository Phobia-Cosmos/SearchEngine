# SearchEngine

1. API有14617(14617, 9),Endpoint有49273条(48718, 9)，所以全部存在一个数据库表中；

## 问题

1. [ImportError: No module named mysql.connector using Python2](https://stackoverflow.com/questions/24272223/importerror-no-module-named-mysql-connector-using-python2)
   1. pip安装mysql失败![img.png](/Users/liuzihao/Desktop/Full_Development/Projects/SearchEngine/Static/picture/pip_mysql.png)
      1.  [Mysqlclient cannot install via pip, cannot find pkg-config name in Ubuntu](https://stackoverflow.com/questions/76585758/mysqlclient-cannot-install-via-pip-cannot-find-pkg-config-name-in-ubuntu)

## 操作

1. 数据库

```mysql
set global local_infile=true;
show global variables like 'local_infile';
exit
mysql --local_infile=1 --show-warnings

# show warnings;
# warnings
# \W
# WARNINGS
# #nowarning(NOWARNING) or \w
delete from api;

LOAD DATA LOCAL INFILE '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/basic_merged_result.csv'
    INTO TABLE api
    FIELDS TERMINATED BY '\t' -- Use the appropriate delimiter
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
```

注意：
1. 如果日期为1000-01-01，则认为此API的更新时间未知