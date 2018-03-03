
CREATE DATABASE
IF NOT EXISTS `newdb` CHARACTER
SET utf8;

USE `newdb`;


DROP TABLE IF EXISTS `sampDBtable`;
create table sampDBtable
(
	id INT UNSIGNED NOT NULL auto_increment PRIMARY KEY,
	Standardmodels TEXT NOT NULL,
	accountid decimal(6,2) not null,
	title CHAR NULL DEFAULT "-",
	titleimg VARCHAR(255) NULL DEFAULT "-",
	srclink TEXT NOT NULL,
	creattime datetime NOT NULL,
	endtime datetime NOT NULL,
	tag VARCHAR(255) NULL DEFAULT "-",
	integral MEDIUMINT not null,
	Latitude decimal(18,11) unsigned not null,
	Longitude decimal(18,11) unsigned not null,
	logintime datetime NOT NULL
) ENGINE=InnoDB CHARACTER SET = utf8;

DROP PROCEDURE IF EXISTS `sampDBtablecount`;
delimiter //
CREATE PROCEDURE sampDBtablecount (OUT countresult INT)
BEGIN
SELECT COUNT(*) INTO countresult FROM sampDBtable;
END //
delimiter ;


DROP TABLE IF EXISTS `wechatappuser`;
create table wechatappuser
(
	id INT UNSIGNED NOT NULL auto_increment PRIMARY KEY,
	session_key VARCHAR(255) NULL DEFAULT "-",
	expires_in MEDIUMINT not null,
	openid VARCHAR(255) NULL DEFAULT "-",
	serSession VARCHAR(255) NULL DEFAULT "-",
	thename VARCHAR(255) NULL DEFAULT "-",
	cellphone VARCHAR(255) NULL DEFAULT "-",
	telephone VARCHAR(255) NULL DEFAULT "-",
	wechat VARCHAR(255) NULL DEFAULT "-",
	qq VARCHAR(255) NULL DEFAULT "-",
	birthday datetime NOT NULL,
	idcard VARCHAR(255) NULL DEFAULT "-",
	address VARCHAR(255) NULL DEFAULT "-",
	sell TEXT NOT NULL,
	buy TEXT NOT NULL,
	email VARCHAR(255) NULL DEFAULT "-",
	url TEXT NOT NULL,
	onlinestatus VARCHAR(255) NULL DEFAULT "-"
) ENGINE=InnoDB CHARACTER SET = utf8;

DROP PROCEDURE IF EXISTS `wechatappusercount`;
delimiter //
CREATE PROCEDURE wechatappusercount (OUT countresult INT)
BEGIN
SELECT COUNT(*) INTO countresult FROM wechatappuser;
END //
delimiter ;


DROP TABLE IF EXISTS `integralhistory`;
create table integralhistory
(
	category MEDIUMTEXT NOT NULL,
	FromAccountid TEXT NOT NULL,
	Fromintegral MEDIUMINT not null,
	ToAccountid TEXT NOT NULL,
	Tointegral MEDIUMINT not null,
	settlementstate CHAR NULL DEFAULT "-",
	time datetime NOT NULL
) ENGINE=InnoDB CHARACTER SET = utf8;

DROP PROCEDURE IF EXISTS `integralhistorycount`;
delimiter //
CREATE PROCEDURE integralhistorycount (OUT countresult INT)
BEGIN
SELECT COUNT(*) INTO countresult FROM integralhistory;
END //
delimiter ;