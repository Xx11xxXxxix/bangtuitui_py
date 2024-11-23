/*
 Navicat Premium Dump SQL

 Source Server         : bendibangtuitui
 Source Server Type    : MySQL
 Source Server Version : 80012 (8.0.12)
 Source Host           : localhost:3306
 Source Schema         : bangtuitui_py

 Target Server Type    : MySQL
 Target Server Version : 80012 (8.0.12)
 File Encoding         : 65001

 Date: 23/11/2024 17:52:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bangtuitui_py_shop_access
-- ----------------------------
DROP TABLE IF EXISTS `bangtuitui_py_shop_access`;
CREATE TABLE `bangtuitui_py_shop_access`  (
  `access_id` int(10) UNSIGNED NOT NULL COMMENT '主键id',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '权限名称',
  `path` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '路由地址',
  `parent_id` int(10) UNSIGNED NOT NULL DEFAULT 0 COMMENT '父级id',
  `sort` tinyint(3) UNSIGNED NOT NULL DEFAULT 100 COMMENT '排序(数字越小越靠前)',
  `icon` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '菜单图标',
  `redirect_name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '重定向名称',
  `is_route` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否是路由 0=不是1=是',
  `is_menu` tinyint(3) UNSIGNED NOT NULL DEFAULT 0 COMMENT '是否是菜单 0不是 1是',
  `alias` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '别名(废弃)',
  `is_show` tinyint(3) UNSIGNED NOT NULL DEFAULT 1 COMMENT '是否显示1=显示0=不显示',
  `plus_category_id` int(11) NULL DEFAULT 0 COMMENT '插件分类id',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '描述',
  `app_id` int(10) UNSIGNED NULL DEFAULT 10001 COMMENT 'app_id',
  `create_time` int(10) UNSIGNED NOT NULL DEFAULT 0 COMMENT '创建时间',
  `update_time` int(10) UNSIGNED NOT NULL DEFAULT 0 COMMENT '更新时间',
  PRIMARY KEY (`access_id`) USING BTREE,
  UNIQUE INDEX `idx_path`(`path` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '商家用户权限表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of bangtuitui_py_shop_access
-- ----------------------------
INSERT INTO `bangtuitui_py_shop_access` VALUES (14, '商品', '/product', 0, 1, 'icon-shangping', '/product/product/index', 1, 1, 'product', 1, 0, '', 10001, 1574333176, 1721875455);
INSERT INTO `bangtuitui_py_shop_access` VALUES (15, '商品管理', '/product/product/index', 14, 0, '', '', 1, 1, 'product_index', 1, 0, '', 10001, 1574333221, 1592203199);
INSERT INTO `bangtuitui_py_shop_access` VALUES (16, '添加商品', '/product/product/add', 15, 0, '', '', 1, 0, 'product_add', 1, 0, '', 10001, 1574333303, 1591164900);
INSERT INTO `bangtuitui_py_shop_access` VALUES (39, '订单', '/order', 0, 1, 'icon-16', '/order/order/index', 1, 1, 'order', 0, 0, '', 10001, 1574931867, 1720947860);
INSERT INTO `bangtuitui_py_shop_access` VALUES (40, '订单管理', '/order/order/index', 39, 0, '', '', 1, 1, 'order_index', 1, 0, '', 10001, 1574932080, 1576288013);
INSERT INTO `bangtuitui_py_shop_access` VALUES (41, '编辑商品', '/product/product/edit', 15, 1, '', '', 1, 0, 'product_edit', 1, 0, '', 10001, 1574938802, 1576220678);
INSERT INTO `bangtuitui_py_shop_access` VALUES (42, '商品分类', '/product/category/index', 14, 1, '', '', 1, 1, 'category_index', 1, 0, '', 10001, 1574939256, 1575364640);
INSERT INTO `bangtuitui_py_shop_access` VALUES (45, '售后管理', '/order/refund/index', 39, 1, '', '', 1, 1, 'refund_refund', 1, 0, '', 10001, 1575342052, 1591955681);
INSERT INTO `bangtuitui_py_shop_access` VALUES (47, '售后详情', '/order/refund/detail', 45, 2, '', '', 1, 0, 'refund_detail', 1, 0, '', 10001, 1575352981, 1576221706);
INSERT INTO `bangtuitui_py_shop_access` VALUES (49, '订单详情', '/order/order/detail', 40, 1, '', '', 1, 0, 'order_detail', 1, 0, '', 10001, 1575353695, 1576221490);
INSERT INTO `bangtuitui_py_shop_access` VALUES (52, '设置', '/setting', 0, 10, 'icon-shezhi', '/setting/store/index', 1, 1, 'setting', 0, 0, '', 10001, 1575359731, 1721120874);
INSERT INTO `bangtuitui_py_shop_access` VALUES (53, '商城设置', '/setting/store/index', 52, 1, '', '', 1, 1, 'setting_store', 0, 0, '', 10001, 1575359827, 1720948270);
INSERT INTO `bangtuitui_py_shop_access` VALUES (54, '会员', '/user', 0, 3, 'icon-huiyuan', '/user/user/index', 1, 1, 'member', 1, 0, '', 10001, 1575424557, 1721875554);
INSERT INTO `bangtuitui_py_shop_access` VALUES (55, '会员管理', '/user/user/index', 54, 1, '', '', 1, 1, 'menber_index', 1, 0, '', 10001, 1575425107, 1592019070);
INSERT INTO `bangtuitui_py_shop_access` VALUES (56, '等级管理', '/user/grade/index', 54, 2, '', '', 1, 1, 'member_grade', 1, 0, '', 10001, 1575425249, 1592019516);
INSERT INTO `bangtuitui_py_shop_access` VALUES (58, '财务概况', '/finance/financeSituation', 57, 1, '', '', 1, 0, 'finance_financesituation', 1, 0, '', 10001, 1575425405, 1577087762);
INSERT INTO `bangtuitui_py_shop_access` VALUES (61, '统计', '/statistics', 0, 4, 'icon-tongji', '/statistics/user/index', 1, 1, 'statistics', 1, 0, '', 10001, 1575425980, 1721791862);
INSERT INTO `bangtuitui_py_shop_access` VALUES (62, '销售统计', '/statistics/sales/index', 61, 1, '', '', 1, 1, 'statistics_Data', 0, 0, '', 10001, 1575426033, 1721791847);
INSERT INTO `bangtuitui_py_shop_access` VALUES (63, '门店', '/store', 0, 5, 'icon-mendian', '/store/store/index', 1, 1, 'store', 0, 0, '', 10001, 1575426188, 1721120676);
INSERT INTO `bangtuitui_py_shop_access` VALUES (64, '门店列表', '/store/store/index', 63, 1, '', '', 1, 1, 'store_index', 1, 0, '', 10001, 1575426245, 1576226029);
INSERT INTO `bangtuitui_py_shop_access` VALUES (65, '店员列表', '/store/clerk/index', 63, 3, '', '', 1, 1, 'store_clerk_index', 1, 0, '', 10001, 1575426295, 1576288613);
INSERT INTO `bangtuitui_py_shop_access` VALUES (66, '订单核销记录', '/store/order/index', 63, 2, '', '', 1, 1, 'store_order_index', 0, 0, '', 10001, 1575426484, 1721098259);
INSERT INTO `bangtuitui_py_shop_access` VALUES (67, '编辑门店', '/store/store/edit', 64, 2, '', '', 1, 0, 'store_edit', 1, 0, '', 10001, 1575426657, 1576222576);
INSERT INTO `bangtuitui_py_shop_access` VALUES (68, '添加门店', '/store/store/add', 64, 1, '', '', 1, 0, 'store_add', 1, 0, '', 10001, 1575426746, 1576222543);
INSERT INTO `bangtuitui_py_shop_access` VALUES (69, '添加店员', '/store/clerk/add', 65, 1, '', '', 1, 0, 'clerk_add', 1, 0, '', 10001, 1575426942, 1576222719);
INSERT INTO `bangtuitui_py_shop_access` VALUES (70, '编辑店员', '/store/clerk/edit', 65, 2, '', '', 1, 0, 'clerk_edit', 1, 0, '', 10001, 1575427016, 1576222751);
INSERT INTO `bangtuitui_py_shop_access` VALUES (71, '页面', '/page', 0, 7, 'icon-iconset0335', '/page/page/list', 1, 1, 'page', 0, 0, '', 10001, 1575427143, 1720948095);
INSERT INTO `bangtuitui_py_shop_access` VALUES (73, '插件', '/plus', 0, 8, 'icon-chajian1', '/plus/plus/index', 1, 1, 'plus', 0, 0, '', 10001, 1575427389, 1720947913);
INSERT INTO `bangtuitui_py_shop_access` VALUES (74, '插件中心', '/plus/plus/index', 73, 1, '', '', 1, 1, 'plus_index', 1, 0, '', 10001, 1575427446, 1592031902);
INSERT INTO `bangtuitui_py_shop_access` VALUES (75, '交易设置', '/setting/trade/index', 52, 2, '', '', 1, 1, 'setting_trade', 0, 0, '', 10001, 1575427639, 1720948271);
INSERT INTO `bangtuitui_py_shop_access` VALUES (76, '运费模板', '/setting/delivery/index', 52, 3, '', '', 1, 1, 'setting_delivery_index', 0, 0, '', 10001, 1575427739, 1720948273);
INSERT INTO `bangtuitui_py_shop_access` VALUES (77, '物流公司', '/setting/express/index', 52, 4, '', '', 1, 1, 'setting_express_index', 0, 0, '', 10001, 1575427795, 1720948275);
INSERT INTO `bangtuitui_py_shop_access` VALUES (78, '消息设置', '/setting/message/index', 52, 5, '', '', 1, 1, 'setting_message', 1, 0, '', 10001, 1575427840, 1721120822);
INSERT INTO `bangtuitui_py_shop_access` VALUES (80, '退货地址', '/setting/address/index', 52, 6, '', '', 1, 1, 'setting_address_Index', 0, 0, '', 10001, 1575427894, 1720948285);
INSERT INTO `bangtuitui_py_shop_access` VALUES (81, '上传设置', '/setting/storage/index', 52, 8, '', '', 1, 1, 'setting_storage', 1, 0, '', 10001, 1575427949, 1591956959);
INSERT INTO `bangtuitui_py_shop_access` VALUES (82, '打印机管理', '/setting/printer/index', 52, 9, '', '', 1, 1, 'setting_printer_index', 0, 0, '', 10001, 1575427995, 1720948288);
INSERT INTO `bangtuitui_py_shop_access` VALUES (83, '打印设置', '/setting/printing/index', 52, 10, '', '', 1, 1, 'setting_printing', 0, 0, '', 10001, 1575428041, 1720948292);
INSERT INTO `bangtuitui_py_shop_access` VALUES (84, '清理缓存', '/setting/clear/index', 52, 11, '', '', 1, 1, 'setting_clear', 1, 0, '', 10001, 1575428087, 1591957018);
INSERT INTO `bangtuitui_py_shop_access` VALUES (85, '应用', '/appsetting', 0, 9, 'icon-application', '', 1, 1, 'appsettings', 1, 0, '', 10001, 1575428240, 1721636905);
INSERT INTO `bangtuitui_py_shop_access` VALUES (86, '基础设置', '/appsetting/app/index', 85, 1, '', '', 1, 1, 'appsettings_appbase', 0, 0, '', 10001, 1575428301, 1721637065);
INSERT INTO `bangtuitui_py_shop_access` VALUES (87, '小程序', '/appsetting/appwx/index', 85, 2, '', '', 1, 1, 'appsettings_appwx', 0, 0, '', 10001, 1575428355, 1721120705);
INSERT INTO `bangtuitui_py_shop_access` VALUES (89, '权限', '/auth', 0, 11, 'icon-authority', '/auth/user/index', 1, 1, 'auth', 1, 0, '', 10001, 1575428502, 1576288793);
INSERT INTO `bangtuitui_py_shop_access` VALUES (90, '管理员列表', '/auth/user/index', 89, 1, '', '', 1, 1, 'auth_user_index', 1, 0, '', 10001, 1575428548, 1576288472);
INSERT INTO `bangtuitui_py_shop_access` VALUES (91, '角色管理', '/auth/role/index', 89, 2, '', '', 1, 1, 'auth_role_index', 1, 0, '', 10001, 1575428592, 1576288479);
INSERT INTO `bangtuitui_py_shop_access` VALUES (92, '添加管理员', '/auth/user/add', 90, 1, '', '', 1, 0, 'user_add', 1, 0, '', 10001, 1575428670, 1576223932);
INSERT INTO `bangtuitui_py_shop_access` VALUES (93, '编辑管理员', '/auth/user/edit', 90, 2, '', '', 1, 0, 'user_edit', 1, 0, '', 10001, 1575428718, 1576223949);
INSERT INTO `bangtuitui_py_shop_access` VALUES (94, '添加角色', '/auth/role/add', 91, 1, '', '', 1, 0, 'role_add', 1, 0, '', 10001, 1575428782, 1576224031);
INSERT INTO `bangtuitui_py_shop_access` VALUES (95, '编辑角色', '/auth/role/edit', 91, 2, '', '', 1, 0, 'role_edit', 1, 0, '', 10001, 1575428833, 1576224010);
INSERT INTO `bangtuitui_py_shop_access` VALUES (96, '积分管理', '/user/points/index', 54, 4, '', '', 1, 1, 'member_points_index', 0, 0, '', 10001, 1575429689, 1721098242);
INSERT INTO `bangtuitui_py_shop_access` VALUES (97, '优惠券', '/plus/coupon/index', 74, 2, 'icon-weibiaoti2fuzhi02', '', 1, 1, 'plus_coupon_index', 1, 2, '将优惠进行到底', 10001, 1575429858, 1607565001);
INSERT INTO `bangtuitui_py_shop_access` VALUES (98, '添加优惠券', '/plus/coupon/coupon/add', 241, 1, '', '', 1, 0, 'plus_coupon_list_add', 1, 0, '', 10001, 1575429999, 1592277945);
INSERT INTO `bangtuitui_py_shop_access` VALUES (100, '文章', '/plus/article', 74, 4, 'icon-16', '/plus/article/index', 1, 1, 'plus_article_Index', 1, 1, '动心的文案促销的利器', 10001, 1575430639, 1607563505);
INSERT INTO `bangtuitui_py_shop_access` VALUES (101, '引导收藏', '/plus/collection/index', 74, 5, 'icon-collection', '', 1, 1, 'plus_collection_index', 1, 1, '', 10001, 1575430698, 1607563674);
INSERT INTO `bangtuitui_py_shop_access` VALUES (112, '编辑优惠券', '/plus/coupon/coupon/edit', 241, 2, '', '', 1, 0, 'plus_coupon_list_edit', 1, 0, '', 10001, 1575454566, 1594979744);
INSERT INTO `bangtuitui_py_shop_access` VALUES (113, '添加文章', '/plus/article/article/add', 224, 2, '', '', 1, 1, 'plus_article_Add', 1, 0, '', 10001, 1575454725, 1592214338);
INSERT INTO `bangtuitui_py_shop_access` VALUES (114, '编辑文章', '/plus/article/article/edit', 224, 3, '', '', 1, 1, 'plus_article_Edit', 1, 0, '', 10001, 1575454781, 1592214348);
INSERT INTO `bangtuitui_py_shop_access` VALUES (118, '页面列表', '/page/page/index', 71, 2, '', '', 1, 1, 'page_lists', 1, 0, '', 10001, 1575697716, 1592029804);
INSERT INTO `bangtuitui_py_shop_access` VALUES (122, '商品评价', '/product/comment/index', 14, 3, '', '', 1, 1, 'product_comment_evaluation', 0, 0, '', 10001, 1575852391, 1720947832);
INSERT INTO `bangtuitui_py_shop_access` VALUES (123, '评价详情', '/product/comment/detail', 122, 1, '', '', 1, 0, 'comment_detail', 1, 0, '', 10001, 1575852589, 1576221135);
INSERT INTO `bangtuitui_py_shop_access` VALUES (124, '添加运费', '/setting/delivery/add', 76, 1, '', '', 1, 0, 'delivery_add', 0, 0, '', 10001, 1575941834, 1720949239);
INSERT INTO `bangtuitui_py_shop_access` VALUES (125, '编辑运费', '/setting/delivery/edit', 76, 2, '', '', 1, 0, 'delivery_edit', 0, 0, '', 10001, 1575941891, 1720949240);
INSERT INTO `bangtuitui_py_shop_access` VALUES (126, '添加物流', '/setting/express/add', 77, 1, '', '', 1, 0, 'express_add', 0, 0, '', 10001, 1575941958, 1720949242);
INSERT INTO `bangtuitui_py_shop_access` VALUES (127, '编辑物流', '/setting/express/edit', 77, 2, '', '', 1, 0, 'express_edit', 0, 0, '', 10001, 1575941997, 1720949242);
INSERT INTO `bangtuitui_py_shop_access` VALUES (128, '添加地址', '/setting/address/add', 80, 1, '', '', 1, 0, 'address_add', 0, 0, '', 10001, 1575942071, 1720949256);
INSERT INTO `bangtuitui_py_shop_access` VALUES (129, '编辑地址', '/setting/address/edit', 80, 2, '', '', 1, 0, 'address_edit', 0, 0, '', 10001, 1575942113, 1720949256);
INSERT INTO `bangtuitui_py_shop_access` VALUES (130, '添加打印机', '/setting/printer/add', 82, 1, '', '', 1, 0, 'printer_add', 0, 0, '', 10001, 1575942184, 1720949263);
INSERT INTO `bangtuitui_py_shop_access` VALUES (131, '编辑打印机', '/setting/printer/edit', 82, 2, '', '', 1, 0, 'printer_edit', 0, 0, '', 10001, 1575942238, 1720949263);
INSERT INTO `bangtuitui_py_shop_access` VALUES (133, '删除评价', '/product/comment/delete', 122, 2, '', '', 1, 0, 'comment|_delete', 1, 0, '', 10001, 1575943511, 1576221202);
INSERT INTO `bangtuitui_py_shop_access` VALUES (143, '删除商品', '/product/product/delete', 15, 3, '', '', 1, 0, 'product_delete', 1, 0, '', NULL, 1576220720, 1576220720);
INSERT INTO `bangtuitui_py_shop_access` VALUES (144, '一键复制', '/product/product/copy', 15, 4, '', '', 1, 0, 'product_copy', 0, 0, '', NULL, 1576220763, 1720947823);
INSERT INTO `bangtuitui_py_shop_access` VALUES (145, '添加分类', '/product/category/add', 42, 1, '', '', 1, 0, 'category_add', 1, 0, '', NULL, 1576220915, 1576220915);
INSERT INTO `bangtuitui_py_shop_access` VALUES (146, '编辑分类', '/product/category/edit', 42, 2, '', '', 1, 0, 'category_edit', 1, 0, '', NULL, 1576220968, 1576220968);
INSERT INTO `bangtuitui_py_shop_access` VALUES (147, '删除分类', '/product/category/delete', 42, 3, '', '', 1, 0, 'category_delete', 1, 0, '', NULL, 1576221000, 1576221000);
INSERT INTO `bangtuitui_py_shop_access` VALUES (148, '会员充值', '/user/user/recharge', 55, 1, '', '', 1, 0, '/member/member/recharge', 0, 0, '', NULL, 1576222057, 1720947875);
INSERT INTO `bangtuitui_py_shop_access` VALUES (149, '会员编辑', '/user/user/edit', 55, 2, '', '', 1, 0, '/member/member/grade', 1, 0, '', NULL, 1576222118, 1592020342);
INSERT INTO `bangtuitui_py_shop_access` VALUES (150, '删除会员', '/user/user/delete', 55, 3, '', '', 1, 0, '/member/member/delete', 1, 0, '', NULL, 1576222165, 1592020351);
INSERT INTO `bangtuitui_py_shop_access` VALUES (151, '添加等级', '/user/grade/add', 56, 1, '', '', 1, 0, '/member/grade/add', 1, 0, '', NULL, 1576222269, 1592019499);
INSERT INTO `bangtuitui_py_shop_access` VALUES (152, '编辑等级', '/user/grade/edit', 56, 2, '', '', 1, 0, '/member/grade/edit', 1, 0, '', NULL, 1576222339, 1592019523);
INSERT INTO `bangtuitui_py_shop_access` VALUES (153, '删除等级', '/user/grade/delete', 56, 3, '', '', 1, 0, '/member/grade/delete', 1, 0, '', NULL, 1576222364, 1592019530);
INSERT INTO `bangtuitui_py_shop_access` VALUES (154, '删除门店', '/store/store/delete', 64, 3, '', '', 1, 0, 'store_delete', 1, 0, '', NULL, 1576222609, 1576222609);
INSERT INTO `bangtuitui_py_shop_access` VALUES (155, '删除店员', '/store/clerk/delete', 65, 3, '', '', 1, 0, 'clerk_delete', 1, 0, '', NULL, 1576222789, 1576222789);
INSERT INTO `bangtuitui_py_shop_access` VALUES (156, '编辑页面', '/page/page/edit', 118, 2, '', '', 1, 0, 'page_edit', 1, 0, '', NULL, 1576222920, 1592030602);
INSERT INTO `bangtuitui_py_shop_access` VALUES (157, '添加页面', '/page/page/add', 118, 1, '', '', 1, 0, 'page_add', 1, 0, '', NULL, 1576222978, 1592030579);
INSERT INTO `bangtuitui_py_shop_access` VALUES (158, '删除页面', '/page/page/delete', 118, 3, '', '', 0, 0, 'page_delete', 1, 0, '', NULL, 1576223041, 1592030615);
INSERT INTO `bangtuitui_py_shop_access` VALUES (159, '设为首页', '/page/page/set', 118, 4, '', '', 0, 0, 'page_set', 1, 0, '', NULL, 1576223087, 1592030627);
INSERT INTO `bangtuitui_py_shop_access` VALUES (160, '删除运费', '/setting/delivery/delete', 76, 3, '', '', 1, 0, 'delivery_delete', 0, 0, '', NULL, 1576223228, 1720949241);
INSERT INTO `bangtuitui_py_shop_access` VALUES (161, '删除物流', '/setting/express/delete', 77, 3, '', '', 1, 0, 'express_delete', 0, 0, '', NULL, 1576223379, 1720949243);
INSERT INTO `bangtuitui_py_shop_access` VALUES (162, '删除地址', '/setting/address/delete', 80, 3, '', '', 1, 0, 'address_delete', 0, 0, '', NULL, 1576223509, 1720949257);
INSERT INTO `bangtuitui_py_shop_access` VALUES (163, '删除打印机', '/setting/printer/delete', 82, 3, '', '', 1, 0, 'printer_delete', 0, 0, '', NULL, 1576223776, 1720949264);
INSERT INTO `bangtuitui_py_shop_access` VALUES (164, '删除管理员', '/auth/user/delete', 90, 3, '', '', 1, 0, 'user_delete', 1, 0, '', NULL, 1576223898, 1576223898);
INSERT INTO `bangtuitui_py_shop_access` VALUES (165, '删除角色', '/auth/role/delete', 91, 3, '', '', 1, 0, 'role_delete', 1, 0, '', NULL, 1576223985, 1576223985);
INSERT INTO `bangtuitui_py_shop_access` VALUES (169, '物流编码', '/setting/express/company', 77, 4, '', '', 1, 0, 'setting_express_company', 0, 0, '', NULL, 1577268734, 1720949244);
INSERT INTO `bangtuitui_py_shop_access` VALUES (170, '公众号关注', '/plus/officia/index', 74, 8, 'icon-gongzhonghaoguanli', '', 1, 1, 'plus_officia_index', 1, 1, '公众号聚粉', 0, 1577696979, 1607565142);
INSERT INTO `bangtuitui_py_shop_access` VALUES (175, '商品推荐', '/plus/recommend/index', 74, 9, 'icon-tuijian1', '', 1, 1, 'plus_recommend_index', 1, 1, '推荐指定商品给用户', 0, 1578275635, 1607565532);
INSERT INTO `bangtuitui_py_shop_access` VALUES (176, '签到有礼', '/plus/sign', 74, 1, 'icon-qiandao', '/plus/sign/index', 1, 1, 'plus_sign_index', 1, 3, '签到享好礼，提升客户粘性', 0, 1578371850, 1607563629);
INSERT INTO `bangtuitui_py_shop_access` VALUES (185, '首页推送', '/plus/homepush/index', 74, 1, 'icon-tuisong', '', 1, 1, 'plus_homepush_Index', 1, 1, '推送最新消息给用户', 0, 1578479354, 1607563655);
INSERT INTO `bangtuitui_py_shop_access` VALUES (211, '短信设置', '/setting/sms/index', 52, 5, '', '', 1, 1, '', 1, 0, '', NULL, 1592016295, 1592018633);
INSERT INTO `bangtuitui_py_shop_access` VALUES (213, '签到记录', '/plus/sign/lists', 176, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592209550, 1592209550);
INSERT INTO `bangtuitui_py_shop_access` VALUES (214, '签到设置', '/plus/sign/index', 176, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592209645, 1592209645);
INSERT INTO `bangtuitui_py_shop_access` VALUES (224, '文章管理', '/plus/article/index', 100, 1, '', '', 1, 0, '', 1, 0, '', 0, 1592214175, 1592215442);
INSERT INTO `bangtuitui_py_shop_access` VALUES (225, '文章列表', '/plus/article/article/index', 224, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592214317, 1592214317);
INSERT INTO `bangtuitui_py_shop_access` VALUES (227, '删除文章', '/plus/article/article/delete', 224, 3, '', '', 0, 1, 'plus_article_Edit', 1, 0, '', NULL, 1592217117, 1592217117);
INSERT INTO `bangtuitui_py_shop_access` VALUES (230, '分类管理', '/plus/article/category', 100, 1, '', '/plus/article/category/index', 1, 0, '', 1, 0, '', NULL, 1592217566, 1592217566);
INSERT INTO `bangtuitui_py_shop_access` VALUES (231, '分类列表', '/plus/article/category/index', 230, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592217637, 1592217637);
INSERT INTO `bangtuitui_py_shop_access` VALUES (232, '添加分类', '/plus/article/category/add', 230, 2, '', '', 1, 0, '', 1, 0, '', 0, 1592217658, 1592217682);
INSERT INTO `bangtuitui_py_shop_access` VALUES (233, '编辑分类', '/plus/article/category/edit', 230, 3, '', '', 1, 0, '', 1, 0, '', NULL, 1592217675, 1592217675);
INSERT INTO `bangtuitui_py_shop_access` VALUES (234, '删除分类', '/plus/article/category/delete', 230, 4, '', '', 0, 0, '', 1, 0, '', 0, 1592217696, 1592217701);
INSERT INTO `bangtuitui_py_shop_access` VALUES (241, '优惠券列表', '/plus/coupon/coupon/index', 97, 1, '', '', 1, 0, '', 1, 0, '', 0, 1592275863, 1592277368);
INSERT INTO `bangtuitui_py_shop_access` VALUES (242, '领取记录', '/plus/coupon/coupon/receive', 97, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592275974, 1592275974);
INSERT INTO `bangtuitui_py_shop_access` VALUES (243, '发送优惠券', '/plus/coupon/coupon/SendCoupon', 97, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1592276320, 1592276320);
INSERT INTO `bangtuitui_py_shop_access` VALUES (246, '分类模板', '/page/page/category', 71, 3, '', '', 1, 1, '', 1, 0, '', 0, 1593399888, 1593400404);
INSERT INTO `bangtuitui_py_shop_access` VALUES (247, '客服设置', '/setting/mpservice/index', 52, 8, '', '', 1, 1, '', 1, 0, '', NULL, 1594344417, 1594344417);
INSERT INTO `bangtuitui_py_shop_access` VALUES (251, '会员统计', '/statistics/user/index', 61, 1, '', '', 1, 1, '', 1, 0, '', 0, 1595313049, 1721098248);
INSERT INTO `bangtuitui_py_shop_access` VALUES (252, '登录日志', '/auth/loginlog/index', 89, 10, '', '', 1, 1, '', 1, 0, '', 0, 0, 0);
INSERT INTO `bangtuitui_py_shop_access` VALUES (253, '操作日志', '/auth/optlog/index', 89, 10, '', '', 1, 1, '', 1, 0, '', 0, 0, 0);
INSERT INTO `bangtuitui_py_shop_access` VALUES (254, '获取手机号', '/setting/message/getphone', 52, 5, '', '', 1, 0, '', 1, 0, '', 0, 1597537789, 1721120817);
INSERT INTO `bangtuitui_py_shop_access` VALUES (255, '订单发货', '/order/order/delivery', 40, 1, '', '', 0, 0, '', 0, 0, '', 0, 1598685493, 1720947839);
INSERT INTO `bangtuitui_py_shop_access` VALUES (256, '订单改价', '/order/order/updatePrice', 40, 1, '', '', 0, 0, '', 0, 0, '', NULL, 1598753520, 1720947841);
INSERT INTO `bangtuitui_py_shop_access` VALUES (257, '取消审核', '/order/operate/confirmCancel', 40, 1, '', '', 0, 0, '', 1, 0, '', NULL, 1598753587, 1598753587);
INSERT INTO `bangtuitui_py_shop_access` VALUES (258, '订单核销', '/order/operate/extract', 40, 1, '', '', 0, 0, '', 1, 0, '', NULL, 1598753609, 1598753609);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1611737214, '支付设置', '/appsetting/apph5/pay', 1611737154, 3, '', '', 1, 1, 'appsettings_appmp', 1, 0, '', 0, 1611737214, 1611737797);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1616228260, '批量发货', '/order/operate/batchDelivery', 40, 10, '', '', 0, 0, '', 0, 0, '', NULL, 1616228260, 1720947848);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1616228316, '订单导出', '/order/operate/export', 40, 9, '', '', 0, 0, '', 0, 0, '', NULL, 1616228316, 1720947846);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626400548, '底部导航', '/page/tabbar/index', 71, 4, '', '', 1, 1, '', 1, 0, '', 0, 1626400548, 1626405360);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626400583, '个人中心', '/page/center/index', 71, 5, '', '', 1, 1, '', 1, 0, '', 0, 1626400583, 1721098276);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626402611, '编辑导航', '/page/tabbar/edit', 1626400548, 1, '', '', 1, 1, '', 1, 0, '', 0, 1626402611, 1626405364);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626421350, '添加菜单', '/page/center/add', 1626400583, 5, '', '', 1, 0, '', 1, 0, '', NULL, 1626421350, 1626421350);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626421363, '编辑菜单', '/page/center/edit', 1626400583, 5, '', '', 1, 0, '', 1, 0, '', NULL, 1626421363, 1626421363);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1626421378, '删除菜单', '/page/center/delete', 1626400583, 5, '', '', 1, 0, '', 1, 0, '', NULL, 1626421378, 1626421378);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1627553916, '标签管理', '/user/tag/index', 54, 2, '', '', 1, 1, '', 1, 0, '', 0, 1627553916, 1627554389);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1627553945, '添加标签', '/user/tag/add', 1627553916, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1627553945, 1627553945);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1627553967, '修改标签', '/user/tag/edit', 1627553916, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1627553967, 1627553967);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1627553983, '删除标签', '/user/tag/delete', 1627553916, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1627553983, 1627553983);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646105229, '首页装修', '/page/page/list', 71, 1, '', '', 1, 1, 'page_home', 1, 0, '', 0, 1646105229, 1646120158);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646120244, '添加', '/page/page/addPage', 1646105229, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1646120244, 1646120244);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646120257, '编辑', '/page/page/editPage', 1646105229, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1646120257, 1646120257);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646120284, '删除', '/page/page/deletePage', 1646105229, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1646120284, 1646120284);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646120351, '设为首页', '/page/page/setPage', 1646105229, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1646120351, 1646120351);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1646292411, '主题设置', '/page/theme/index', 71, 3, '', '', 1, 1, '', 1, 0, '', NULL, 1646292411, 1646292411);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1650781218, '支付设置', '/appsetting/app/pay', 85, 3, '', '', 1, 1, 'appsettings_appmp', 0, 0, '', NULL, 1650781218, 1721120706);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656061695, '取消订单', '/order/order/orderCancel', 40, 10, '', '', 0, 0, '', 1, 0, '', NULL, 1656061695, 1656061695);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656062908, '售后审核', '/order/refund/audit', 45, 2, '', '', 1, 0, 'refund_detail', 1, 0, '', NULL, 1656062908, 1656062908);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656063093, '售后确认', '/order/refund/receipt', 45, 2, '', '', 1, 0, 'refund_detail', 1, 0, '', NULL, 1656063093, 1656063093);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656063620, '会员标签', '/user/user/tag', 55, 3, '', '', 1, 0, '/member/member/delete', 1, 0, '', NULL, 1656063620, 1656063620);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656064981, '升级日志', '/user/grade/log', 56, 3, '', '', 1, 0, '/member/grade/delete', 1, 0, '', NULL, 1656064981, 1656064981);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656065454, '积分设置', '/user/points/setting', 96, 1, '', '', 1, 0, '', 0, 0, '', NULL, 1656065454, 1721098242);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656065481, '积分明细', '/user/points/log', 96, 1, '', '', 1, 0, '', 0, 0, '', NULL, 1656065481, 1721098243);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656311685, '获取消息设置', '/setting/message/field', 78, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1656311685, 1721120823);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656311724, '编辑消息设置', '/setting/message/saveSettings', 78, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1656311724, 1721120825);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656311758, '消息设置状态', '/setting/message/updateSettingsStatus', 78, 1, '', '', 1, 0, '', 1, 0, '', NULL, 1656311758, 1721120824);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656385988, '审核评价', '/product/comment/edit', 122, 2, '', '', 1, 0, 'comment|_delete', 1, 0, '', NULL, 1656385988, 1656385988);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1656386098, '商品上下架', '/product/product/state', 15, 4, '', '', 1, 0, 'product_copy', 1, 0, '', NULL, 1656386098, 1656386098);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1660787976, '修改地址', '/order/order/updateAddress', 40, 10, '', '', 0, 0, '', 1, 0, '', NULL, 1660787976, 1660787976);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1666406677, '会员等级', '/user/user/grade', 55, 3, '', '', 1, 0, '/member/member/delete', 1, 0, '', NULL, 1666406677, 1721098232);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1692345073, '微信小程序发货', '/order/order/wxDelivery', 40, 10, '', '', 0, 0, '', 1, 0, '', NULL, 1692345073, 1692345073);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721091710, '商品标签', '/product/tags', 14, 1, '', '/product/tags/index', 1, 1, 'category_index', 1, 0, '', 0, 1721091710, 1721875511);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721091742, '添加标签', '/product/tags/add', 1721091710, 1, '', '', 1, 0, 'category_add', 1, 0, '', NULL, 1721091742, 1721091742);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721091765, '编辑标签', '/product/tags/edit', 1721091710, 2, '', '', 1, 0, 'category_edit', 1, 0, '', NULL, 1721091765, 1721091765);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721091785, '删除标签', '/product/tags/delete', 1721091710, 3, '', '', 1, 0, 'category_delete', 1, 0, '', NULL, 1721091785, 1721091785);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438000, '渠道', '/platform', 0, 2, 'icon-stores', '/platform/platform/index', 1, 1, 'product', 1, 0, '', 0, 1721438000, 1721875477);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438037, '渠道管理', '/platform/platform/index', 1721438000, 0, '', '', 1, 1, 'product_index', 1, 0, '', NULL, 1721438037, 1721438037);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438071, '添加渠道', '/platform/platform/add', 1721438037, 0, '', '', 1, 0, 'product_add', 1, 0, '', NULL, 1721438071, 1721438071);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438090, '编辑渠道', '/platform/platform/edit', 1721438037, 1, '', '', 1, 0, 'product_edit', 1, 0, '', 0, 1721438090, 1721438102);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438126, '删除渠道', '/platform/platform/delete', 1721438037, 3, '', '', 1, 0, 'product_delete', 1, 0, '', NULL, 1721438126, 1721438126);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438174, '渠道分类', '/platform/category/index', 1721438000, 1, '', '', 1, 1, 'category_index', 1, 0, '', NULL, 1721438174, 1721438174);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438194, '添加分类', '/platform/category/add', 1721438174, 1, '', '', 1, 0, 'category_add', 1, 0, '', NULL, 1721438194, 1721438194);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438220, '编辑分类', '/platform/category/edit', 1721438174, 2, '', '', 1, 0, 'category_edit', 1, 0, '', NULL, 1721438220, 1721438220);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721438240, '删除分类', '/platform/category/delete', 1721438174, 3, '', '', 1, 0, 'category_delete', 1, 0, '', NULL, 1721438240, 1721438240);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721636656, '用户协议', '/appsetting/app/doc', 85, 1, '', '', 1, 1, '', 1, 0, '', 0, 1721636656, 1721637045);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721636706, '隐私协议', '/appsetting/app/private', 85, 2, '', '', 1, 1, '', 1, 0, '', 0, 1721636706, 1721637053);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721800506, '渠道统计', '/statistics/platform/index', 61, 1, '', '', 1, 1, '', 1, 0, '', NULL, 1721800506, 1721800506);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721808135, '数据统计', '/statistics_other', 0, 4, 'icon-tongji', '/statistics_other/platform/index', 1, 1, 'statistics', 1, 0, '', 0, 1721808135, 1721809025);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721808177, '渠道数据统计', '/statistics_other/platform/index', 1721808135, 1, '', '', 1, 1, '', 1, 0, '', NULL, 1721808177, 1721808177);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721810889, '查询', '/statistics_other/platform/getList', 1721808177, 1, '', '', 1, 0, '', 1, 0, '', 0, 1721810889, 1721811020);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721812456, '浏览记录', '/statistics/history/index', 61, 1, '', '', 1, 1, '', 1, 0, '', 0, 1721812456, 1731739828);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721812499, '查看', '/product/product/query', 15, 4, '', '', 1, 0, 'product_copy', 1, 0, '', NULL, 1721812499, 1721812499);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721812697, '首页', '/home', 0, 0, 'icon-home', '/home', 1, 1, '', 1, 0, '', 0, 1721812697, 1721814871);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721875532, '标签数据', '/product/tags/index', 1721091710, 1, '', '', 1, 0, 'category_add', 1, 0, '', NULL, 1721875532, 1721875532);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976490, '轮播图', '/slide', 0, 0, 'icon-tupian111', '/slide/index', 1, 1, '', 1, 0, '', 0, 1721976490, 1721976658);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976762, '轮播图管理', '/slide/index', 1721976490, 0, '', '', 1, 1, 'product_add', 1, 0, '', NULL, 1721976762, 1721976762);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976795, '添加轮播图', '/slide/add', 1721976762, 0, '', '', 1, 0, 'product_add', 1, 0, '', NULL, 1721976795, 1721976795);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976816, '编辑轮播图', '/slide/edit', 1721976762, 0, '', '', 1, 0, 'product_add', 1, 0, '', NULL, 1721976816, 1721976816);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976831, '删除轮播图', '/slide/delete', 1721976762, 0, '', '', 1, 0, 'product_add', 1, 0, '', NULL, 1721976831, 1721976831);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1721976832, '渠道详情', '/platform/platform/detail', 1721438037, 1, '', '', 1, 0, 'product_edit', 1, 0, '', 0, 1721438090, 1721438102);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1731726795, '留言管理', '/user/msg/index', 54, 1, '', '', 1, 1, 'menber_index', 1, 0, '', NULL, 1731726795, 1731726795);
INSERT INTO `bangtuitui_py_shop_access` VALUES (1731726796, '往南登录', '/netease', 0, 1, '', '', 1, 1, '', 1, 0, '', 0, 1731726795, 1731726795);

SET FOREIGN_KEY_CHECKS = 1;
