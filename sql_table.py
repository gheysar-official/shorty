"""
SQL Table Create Statement ,
Follow the same order as given.
"""

URLs_table = '''
CREATE TABLE web_url(
ID serial,
URL VARCHAR(512),
S_URL VARCHAR(80), 
TAG VARCHAR(80),
created_at timestamp default now()::timestamp,
disabled_at timestamp,
COUNTER INT DEFAULT 0,
CHROME INT DEFAULT 0,
FIREFOX INT DEFAULT 0,
SAFARI INT DEFAULT 0,
OTHER_BROWSER INT DEFAULT 0,
ANDROID INT DEFAULT 0,
IOS INT DEFAULT 0, 
WINDOWS INT DEFAULT 0,
LINUX INT DEFAULT 0,
MAC INT DEFAULT 0,
OTHER_PLATFORM INT DEFAULT 0 , 
PRIMARY KEY(ID));
'''

log_table = '''
CREATE TABLE web_url_log
(
id serial PRIMARY KEY,
s_url varchar(80),
user_ip text,
created_at timestamp DEFAULT now()::timestamp
);
CREATE UNIQUE INDEX web_url_log_id_uindex ON web_url_log (id);
'''