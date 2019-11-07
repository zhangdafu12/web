/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80013
Source Host           : localhost:3306
Source Database       : translation

Target Server Type    : MYSQL
Target Server Version : 80013
File Encoding         : 65001

Date: 2019-06-05 22:20:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for api
-- ----------------------------
DROP TABLE IF EXISTS `api`;
CREATE TABLE `api` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apiname` varchar(255) DEFAULT NULL,
  `param1` varchar(255) DEFAULT NULL,
  `param2` varchar(255) DEFAULT NULL,
  `param3` varchar(255) DEFAULT NULL,
  `describe_` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `tag1` varchar(255) DEFAULT NULL,
  `tag2` varchar(255) DEFAULT NULL,
  `tag3` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of api
-- ----------------------------
INSERT INTO `api` VALUES ('2', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('3', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口水的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('4', '这是什么', '不知道1', '不知道2', '不知道3', '流口水的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('5', '这是什么', '不知道1', '不知道2', '不知道3', '让流口水的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('6', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('7', '这是什么', '不知道1', '不知道2', '不知道3', '让人流的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('8', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口水的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('9', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('10', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('11', '这是什么', '不知道1', '不知道2', '不知道3', '让人流的白斩鸡', '人', '白', '鸡', '口水鸡');
INSERT INTO `api` VALUES ('12', '这是什么', '不知道1', '不知道2', '不知道3', '让人流口的白斩鸡', '人', '白', '鸡', '口水鸡');

-- ----------------------------
-- Table structure for serverdescribe
-- ----------------------------
DROP TABLE IF EXISTS `serverdescribe`;
CREATE TABLE `serverdescribe` (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `api` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `parm` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `aname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `describes` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of serverdescribe
-- ----------------------------
INSERT INTO `serverdescribe` VALUES ('1558713528', 'http://apis.juhe.cn/mobile/get', '转入账户#转出账户#金额', '转账', '在系统内通过不同方式进行转账 ', '支付宝转账#微信转账#红包转账');
INSERT INTO `serverdescribe` VALUES ('1558761013', 'http://apis.juhe.cn/mobile/get', '名字#时间#操作人', '账户操作', '对帐户进行操作 ', '注销#锁定#删除');
INSERT INTO `serverdescribe` VALUES ('1559267239', '', '##', '', ' ', '##');

-- ----------------------------
-- Table structure for shuyu
-- ----------------------------
DROP TABLE IF EXISTS `shuyu`;
CREATE TABLE `shuyu` (
  `id` int(255) NOT NULL,
  `shuname` varchar(255) DEFAULT NULL,
  `shutype` varchar(255) DEFAULT NULL,
  `hangye` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shuyu
-- ----------------------------

-- ----------------------------
-- Table structure for xml
-- ----------------------------
DROP TABLE IF EXISTS `xml`;
CREATE TABLE `xml` (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `xml` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `hangye` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of xml
-- ----------------------------
INSERT INTO `xml` VALUES ('1558773649', '1558773649', '金融');
INSERT INTO `xml` VALUES ('1559266966', '1559266966', '金融');
