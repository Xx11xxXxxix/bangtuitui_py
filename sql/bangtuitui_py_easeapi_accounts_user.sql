/*
 Navicat Premium Data Transfer

 Source Server         : wenjiee
 Source Server Type    : MySQL
 Source Server Version : 90001 (9.0.1)
 Source Host           : localhost:3306
 Source Schema         : bangtuitui_py

 Target Server Type    : MySQL
 Target Server Version : 90001 (9.0.1)
 File Encoding         : 65001

 Date: 01/12/2024 15:52:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bangtuitui_py_easeapi_accounts_user
-- ----------------------------
DROP TABLE IF EXISTS `bangtuitui_py_easeapi_accounts_user`;
CREATE TABLE `bangtuitui_py_easeapi_accounts_user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of bangtuitui_py_easeapi_accounts_user
-- ----------------------------
BEGIN;
INSERT INTO `bangtuitui_py_easeapi_accounts_user` (`uid`, `username`, `phone_number`, `password`) VALUES (1, 'wenjie', '18825263749', 'pbkdf2_sha256$870000$MTEZKY1H35Dd5UDtxGs1Mw$XPCCbtFGvV9uR+wZLUtt7G9kk/PaYRcu/2cSJEB+5ag=');
INSERT INTO `bangtuitui_py_easeapi_accounts_user` (`uid`, `username`, `phone_number`, `password`) VALUES (4, 'wenjie2', '18825263748', 'pbkdf2_sha256$870000$gvpc9H3PqTnvqQJDP3Qiyd$l3K5AIoXYS2catOjvQGEcb/fTyyDbZXClVrJoUuwTgI=');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
