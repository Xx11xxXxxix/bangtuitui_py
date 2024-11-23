/*
 Navicat Premium Dump SQL

 Source Server         : 1
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : localhost:3306
 Source Schema         : bangtuitui_py

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 22/11/2024 22:07:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bangtuitui_py_easeapi_user
-- ----------------------------
DROP TABLE IF EXISTS `bangtuitui_py_easeapi_user`;
CREATE TABLE `bangtuitui_py_easeapi_user`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `music_u` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatar_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `background_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `signature` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `birthday` bigint NULL DEFAULT NULL,
  `gender` tinyint NULL DEFAULT NULL,
  `province` int NULL DEFAULT NULL,
  `city` int NULL DEFAULT NULL,
  `vip_type` tinyint NULL DEFAULT NULL,
  `account_type` tinyint NULL DEFAULT NULL,
  `authority` int NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `detail_description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `auth_status` tinyint NULL DEFAULT NULL,
  `last_login_time` bigint NULL DEFAULT NULL,
  `last_login_ip` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of bangtuitui_py_easeapi_user
-- ----------------------------
INSERT INTO `bangtuitui_py_easeapi_user` VALUES (3, 1406801710, '網上临狙', '<WSGIRequest: GET \'/netease/get_user_info/\'>', 'http://p2.music.126.net/_hjfMsNcV06yfyZmhysDiA==/109951166370891427.jpg', 'http://p1.music.126.net/_f8R60U9mZ42sSNvdPn2sQ==/109951162868126486.jpg', '', 631190823221, 1, 110000, 110101, 0, 1, 0, NULL, NULL, 0, 1732030926437, '183.197.178.100', '2024-11-19 23:54:21', '2024-11-19 23:54:21');

SET FOREIGN_KEY_CHECKS = 1;
