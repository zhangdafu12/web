/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80013
Source Host           : localhost:3306
Source Database       : netta

Target Server Type    : MYSQL
Target Server Version : 80013
File Encoding         : 65001

Date: 2019-05-23 14:39:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `news_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `body` longtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `timestamp` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `agree_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `news_id` (`news_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`news_id`) REFERENCES `news` (`news_id`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES ('58', '9', '4', '惊起一滩鸥鹭', '2019-04-26 12:13:55', '0');
INSERT INTO `comments` VALUES ('60', '9', '16', '江月何年初照人', '2019-05-06 14:59:10', '0');
INSERT INTO `comments` VALUES ('85', '9', '15', '也无风雨也无晴', '2019-05-06 14:46:17', '0');
INSERT INTO `comments` VALUES ('88', '9', '15', '123456789', '2019-05-06 11:21:31', '0');
INSERT INTO `comments` VALUES ('89', '9', '15', '４５６７８９', '2019-05-06 11:35:32', '0');
INSERT INTO `comments` VALUES ('91', '9', '4', '江月年只相似', '2019-05-07 03:48:46', '0');
INSERT INTO `comments` VALUES ('93', '9', '4', '江月年年只相似', '2019-05-13 14:33:46', '-13');

-- ----------------------------
-- Table structure for givelike
-- ----------------------------
DROP TABLE IF EXISTS `givelike`;
CREATE TABLE `givelike` (
  `con_rep_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `like_type` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of givelike
-- ----------------------------
INSERT INTO `givelike` VALUES ('53', '15', 'reply', '5');
INSERT INTO `givelike` VALUES ('56', '15', 'comment', '7');
INSERT INTO `givelike` VALUES ('44', '15', 'reply', '10');
INSERT INTO `givelike` VALUES ('28', '15', 'reply', '12');
INSERT INTO `givelike` VALUES ('57', '15', 'reply', '52');
INSERT INTO `givelike` VALUES ('93', '16', 'comment', '55');
INSERT INTO `givelike` VALUES ('64', '4', 'reply', '83');

-- ----------------------------
-- Table structure for middle_mylike
-- ----------------------------
DROP TABLE IF EXISTS `middle_mylike`;
CREATE TABLE `middle_mylike` (
  `user_id` int(11) NOT NULL,
  `news_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`news_id`),
  KEY `news_id` (`news_id`),
  CONSTRAINT `middle_mylike_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `middle_mylike_ibfk_2` FOREIGN KEY (`news_id`) REFERENCES `news` (`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of middle_mylike
-- ----------------------------
INSERT INTO `middle_mylike` VALUES ('4', '13');
INSERT INTO `middle_mylike` VALUES ('4', '17');
INSERT INTO `middle_mylike` VALUES ('4', '18');
INSERT INTO `middle_mylike` VALUES ('4', '19');
INSERT INTO `middle_mylike` VALUES ('4', '20');

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` longtext,
  `news_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `author` varchar(255) DEFAULT NULL,
  `watch_num` int(11) DEFAULT NULL,
  `comment_num` int(11) DEFAULT NULL,
  `like_num` int(11) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL COMMENT '简介',
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('9', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', null, '2019-05-07 20:57:35', 'xxxxx', '123', '122', '123', 'head_pic/4.jpg', 'https://www.baidu.com', null);
INSERT INTO `news` VALUES ('10', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', null, '2019-04-23 22:09:56', 'cdfg', '45', '89', '1', '../static/img/test3.jpg', '', null);
INSERT INTO `news` VALUES ('11', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', 'jyu', '2019-04-14 10:42:45', 'kil', '5896', '69', '563', '../static/img/test3.jpg', null, null);
INSERT INTO `news` VALUES ('12', 'ddd', null, '2019-04-15 20:43:17', 'xxxxx', '123', '123', '121', 'head_pic/4.jpg../static/img/test3.jpg', 'https://www.baidu.com', null);
INSERT INTO `news` VALUES ('13', 'ddd', null, '2019-05-07 13:26:31', 'xxxxx', '123', '123', '123', 'head_pic/4.jpg../static/img/test3.jpg', 'https://www.baidu.com', null);
INSERT INTO `news` VALUES ('14', 'ddhju', null, '2019-04-15 21:03:28', 'cdfg', '45', '89', '3', '../static/img/test3.jpg', '', null);
INSERT INTO `news` VALUES ('15', 'gtyty', 'jyu', '2019-04-14 10:31:16', 'kil', '5896', '69', '563', '../static/img/test3.jpg', null, null);
INSERT INTO `news` VALUES ('16', 'ddd', null, '2019-04-23 22:10:23', 'xxxxx', '123', '123', '121', 'head_pic/4.jpg../static/img/test3.jpg', 'https://www.baidu.com', null);
INSERT INTO `news` VALUES ('17', 'ddd', null, '2019-05-07 13:29:10', 'xxxxx', '123', '123', '122', 'head_pic/4.jpg', 'https://www.baidu.com', null);
INSERT INTO `news` VALUES ('18', 'ddhju', null, '2019-05-07 13:41:00', 'cdfg', '45', '89', '5', '', '', null);
INSERT INTO `news` VALUES ('19', 'gtyty', 'jyu', '2019-05-07 13:41:25', 'kil', '5896', '69', '565', null, null, null);
INSERT INTO `news` VALUES ('20', 'ddd', null, '2019-05-07 14:04:26', 'xxxxx', '123', '123', '122', 'head_pic/4.jpg', 'https://www.baidu.com', null);

-- ----------------------------
-- Table structure for notify_remind
-- ----------------------------
DROP TABLE IF EXISTS `notify_remind`;
CREATE TABLE `notify_remind` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipientID` int(11) NOT NULL,
  `kind` varchar(255) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT NULL,
  `status` tinyint(255) DEFAULT NULL,
  `from_user_name` varchar(255) DEFAULT NULL,
  `content` text,
  `news_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of notify_remind
-- ----------------------------
INSERT INTO `notify_remind` VALUES ('3', '4', 'comment', '2019-05-12 03:25:58', '1', '福尔摩斯', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '11');
INSERT INTO `notify_remind` VALUES ('4', '15', 'comment', '2019-05-12 03:34:32', '0', '福尔摩斯', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '12');
INSERT INTO `notify_remind` VALUES ('5', '4', 'comment', '2019-05-13 06:08:22', '1', '12306', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '9');
INSERT INTO `notify_remind` VALUES ('6', '4', 'comment', '2019-05-13 06:08:45', '1', '12306', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '9');
INSERT INTO `notify_remind` VALUES ('7', '4', 'comment', '2019-05-13 06:08:59', '1', '12306', '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '9');
INSERT INTO `notify_remind` VALUES ('8', '4', 'like', '2019-05-13 06:52:51', '0', null, '最早2020年通车！苏州今年将推进中心城区5条重点道路建设', '9');

-- ----------------------------
-- Table structure for replies
-- ----------------------------
DROP TABLE IF EXISTS `replies`;
CREATE TABLE `replies` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `body` text,
  `timestamp` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `from_uid` int(11) NOT NULL,
  `to_uid` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `reply_id` int(11) DEFAULT NULL,
  `reply_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '点赞数',
  `agree_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_id` (`comment_id`),
  KEY `from_uid` (`from_uid`) USING BTREE,
  KEY `to_uid` (`to_uid`) USING BTREE,
  CONSTRAINT `replies_ibfk_1` FOREIGN KEY (`from_uid`) REFERENCES `users` (`user_id`),
  CONSTRAINT `replies_ibfk_2` FOREIGN KEY (`to_uid`) REFERENCES `users` (`user_id`),
  CONSTRAINT `replies_ibfk_3` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of replies
-- ----------------------------
INSERT INTO `replies` VALUES ('27', '滟滟随波千万里', '2019-04-27 15:50:11', '16', '4', '58', '58', 'comment', '0');
INSERT INTO `replies` VALUES ('43', '谁家今夜扁舟子', '2019-05-06 14:46:35', '15', '15', '60', '42', 'reply', '0');
INSERT INTO `replies` VALUES ('55', '何处相思明月楼', '2019-05-06 14:38:42', '15', '15', '60', '43', 'reply', '0');
INSERT INTO `replies` VALUES ('56', '江天一色无纤尘，皎皎空中孤月轮', '2019-05-06 14:48:53', '15', '15', '60', '43', 'reply', '0');
INSERT INTO `replies` VALUES ('57', '江流宛转绕芳甸', '2019-05-13 14:39:55', '15', '15', '60', '55', 'reply', '0');
INSERT INTO `replies` VALUES ('58', '江流宛转绕芳甸，月照花林皆似霰', '2019-05-13 14:39:44', '15', '15', '60', '43', 'reply', '-1');
INSERT INTO `replies` VALUES ('59', '我们注定无法与往事和解，因为在那 触不可及的彼岸伫立着我们未曾拥有的一生', '2019-05-13 14:33:42', '4', '4', '93', '93', 'comment', '-4');
INSERT INTO `replies` VALUES ('60', '人似乎都在遗忘过去、、、、', '2019-05-12 11:25:08', '4', '4', '93', '59', 'reply', '0');
INSERT INTO `replies` VALUES ('61', '民主与专制', '2019-05-12 11:32:41', '4', '15', '60', '58', 'reply', '0');
INSERT INTO `replies` VALUES ('62', 'jaii', '2019-05-13 15:12:18', '16', '4', '93', '59', 'reply', '-10');
INSERT INTO `replies` VALUES ('63', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '2019-05-13 14:05:02', '16', '4', '93', '60', 'reply', '0');
INSERT INTO `replies` VALUES ('64', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '2019-05-13 14:52:50', '16', '4', '60', '61', 'reply', '1');

-- ----------------------------
-- Table structure for search_result
-- ----------------------------
DROP TABLE IF EXISTS `search_result`;
CREATE TABLE `search_result` (
  `search_id` int(11) NOT NULL AUTO_INCREMENT,
  `kind` varchar(64) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `content` longtext,
  `label` varchar(255) DEFAULT NULL,
  `detail` longtext,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`search_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of search_result
-- ----------------------------
INSERT INTO `search_result` VALUES ('1', 'organization', '腾讯科技（深圳）有限公司', null, 'img/organization-demo.jpg', '腾讯科技（深圳）有限公司成立于1998年11月，是目前中国最大的互联网综合服务提供商之一，也是中国服务用户最多的互联网企业之一。成立十年多以来，腾讯一直秉承一切以用户价值为依归的经营理念，始终处于稳健、高速发展的状态。2004年6月16日，腾讯公司在香港联交所主板公开上市（股票代号700）。\r\n腾讯科技（深圳）有限公司成立于1998年11月，是目前中国最大的互联网综合服务提供商之一，也是中国服务用户最多的互联网企业之一。成立十年多以来，腾讯一直秉承一切以用户价值为依归的经营理念，始终处于稳健、高速发展的状态。2004年6月16日，腾讯公司在香港联交所主板公开上市（股票代号700）。\r\n', '腾讯科技  /  马化腾  /  微信  /  QQ  /  3Q大战', null, null);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `nick_name` varchar(255) NOT NULL,
  `true_name` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `head_pic` varchar(255) DEFAULT NULL,
  `birthday` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `province` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '' COMMENT '个人描述',
  `is_administrator` tinyint(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('4', '123', '123', '福尔摩斯', '王大锤', 'female', 'head_pic/4.jpg', '2019-04-20', '万盛区', '重庆市', '重庆市', '力量与智慧的完美结合', '0');
INSERT INTO `users` VALUES ('15', '1234', '1234', '12354', null, null, 'head_pic/default.jpg', null, null, null, null, null, '0');
INSERT INTO `users` VALUES ('16', '12306', '12306', '12306', '中国铁路网', 'male', 'head_pic/default.jpg', null, '遵化市', '河北省', '唐山市', null, '0');
