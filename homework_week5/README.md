# Task2
**Create a new database named website.**
```
CREATE SCHEMA `website` DEFAULT CHARACTER SET utf8 ;
```
![Result](/pic/create_website_db.png)

**Create a new table named member, in the website database.**
```
CREATE TABLE `website`.`member` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    `name` VARCHAR(255) NOT NULL COMMENT 'Name',
    `username` VARCHAR(255) NOT NULL COMMENT 'Username',
    `password` VARCHAR(255) NOT NULL COMMENT 'Password',
    `follower_count` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
    );
```
![Result](/pic/create_member_table.png)

# Task3
**INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.**
```
INSERT INTO `website`.`member` (`name`, `username`,`password`) 
VALUES ('test', 'test','test');
```
![Result](/pic/create_test.png)
```
INSERT INTO `website`.`member` (`name`, `username`,`password`,`follower_count`,`time`) VALUES ('Midori', 'Midori','test',100,'2023-04-15 12:30:00'),('Stella', 'Stella','test',100,'2023-04-10 13:30:00'),('Yun', 'Yun','test',100,'2024-02-10 13:30:00'),('Hoho', 'Hoho','test',100,CURRENT_TIMESTAMP);
```
![Result](/pic/create_4_test.png)

**SELECT all rows from the member table.**
```
SELECT * FROM website.member;
```
![Result](/pic/select_all_rows.png)

**SELECT all rows from the member table, in descending order of time.**
```
SELECT * FROM website.member ORDER BY time DESC;
```
![Result](/pic/select_all_rows_time.png)

**SELECT total 3 rows, second to fourth, from the member table, in descending order of time.**
```
SELECT * FROM website.member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![Result](/pic/select_3_rows_time.png)

**SELECT rows where username equals to test.**
```
SELECT * FROM website.member WHERE username = 'test';
```
![Result](/pic/select_test.png)

**SELECT rows where name includes the es keyword.**
```
SELECT * FROM website.member WHERE name LIKE '%es%';
```
![Result](/pic/select_es.png)

**SELECT rows where both username and password equal to test.**
```
SELECT * FROM website.member WHERE username = 'test' AND password = 'test';
```
![Result](/pic/select_and_test.png)

**UPDATE data in name column to test2 where username equals to test.**
```
UPDATE website.member SET name = 'test2' WHERE username = 'test';
```
![Result](/pic/update.png)

# Task4
**SELECT how many rows from the member table.**
```
SELECT COUNT(*) FROM website.member;
```
![Result](/pic/select_how_many.png)

**SELECT the sum of follower_count of all the rows from the member table.**
```
SELECT SUM(follower_count) FROM website.member;
```
![Result](/pic/select_sum.png)

**SELECT the average of follower_count of all the rows from the member table.**
```
SELECT AVG(follower_count) FROM website.member;
```
![Result](/pic/select_avg.png)

**SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.**

```
SELECT AVG(sub.follower_count) AS avg_follower_count 
FROM (
    SELECT follower_count
    FROM website.member
    ORDER BY follower_count DESC
    LIMIT 2
) AS sub;
```
![Result](/pic/select_avg2.png)

# Task5
**Create a new table named message, in the website database.**
```
CREATE TABLE website.message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
    FOREIGN KEY (member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL COMMENT 'Content',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Content',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time'
);
```
![Result](/pic/create_message_table.png)
```
INSERT INTO `website`.`message` (`member_id`,`content`, `like_count`,`time`) VALUES (2,'Hello', 5,'2023-04-15 12:56:00'),(3,'Hello back', 3,'2023-04-15 13:30:00'),(5,'See you later', 5,'2024-04-30 13:30:00'),(4,'See you soon', 3,'2024-04-30 13:30:50'),(1,'Test message', 1,'2020-04-15 12:00:00');
```
![Result](/pic/create_message_rows.png)

**SELECT all messages, including sender names. We have to JOIN the member table to get that.**
```
SELECT message.*, member.name AS sender_name
FROM website.message
JOIN website.member ON message.member_id = member.id;
```
![Result](/pic/join.png)

**SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.**
```
SELECT message.*, member.name AS sender_name
FROM website.message
JOIN website.member ON message.member_id = member.id
WHERE username = 'test';
```
![Result](/pic/join_test.png)

**Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.**
```
SELECT AVG(message.like_count) AS average_likes
FROM website.message
JOIN website.member ON message.member_id = member.id
WHERE member.username = 'test';
```
![Result](/pic/join_avg_test.png)

**Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.**
```
SELECT AVG(message.like_count) AS average_likes, member.name AS sender_name
FROM website.message
JOIN website.member ON message.member_id = member.id
GROUP BY member_id,sender_name;
```
![Result](/pic/join_group_by.png)