import logging
import os

import qrcode

from vo import ResultEntity
from vo.QrExport import QrExportReq, QrExportRes
from vo.ResultEntity import ResultEntityMethod

logger = logging.getLogger()
def qrExport(request: QrExportReq) -> ResultEntity:
    try:

        # 带自定义选项但无文本的二维码生成
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=request.size,
                border=request.border,
            )
            data = request.to_qr_data()  # 返回过滤后的字典
            qr.add_data(data)
            qr.make(fit=True)

            # 创建 export 目录（如果不存在）
            export_dir = "export"
            if not os.path.exists(export_dir):
                os.makedirs(export_dir)
                logger.info(f"[qr 导出] - 创建目录: {export_dir}")

            # 设置文件路径到 export 目录
            filename = request.filename
            filepath = os.path.join(export_dir, filename)

            # img可导出返回
            img = qr.make_image(fill_color=request.fill_color, back_color=request.back_color)
            img.save(filepath)
            logger.info(f"[qr 导出] - 二维码已成功生成并保存为: {filepath}")
            logger.info(f"[qr 导出] - 编码的数据: {data}")
            qrExportRes = QrExportRes(
                exportSuccess=True
            )
            return ResultEntityMethod.buildSuccessResult(data=qrExportRes)
        except Exception as e:
            logger.error("[qr 导出] - 生成二维码时出错:", e)
            ResultEntityMethod.buildFailedResult(message="opc qr导出生成二维码出错")
    except Exception as e:
        logger.error("[qr 导出] - opc qr导出未知失败", e)
        return ResultEntityMethod.buildFailedResult(message="opc qr导出未知失败")
if __name__ == "__main__":
    request = QrExportReq(
        filename='example.jpg',
        size=4,
        border=4,
        fill_color="black",
        back_color="white",
        # 样品编号
        sample_number="2132168",
        # 样品状态
        sample_status="A",
        # 样品是否符合规格
        sample_in_spec="T",
        # 取样日期
        sampled_date="2025/10/29 0:00:00",
        # 产品
        product="YPA2烟气",
        # 取样点
        sampling_point="A2烟气",
        # 样品类型
        sample_type="常规样品",
        # 产品类型
        prod_type="中控",
        # 产品名称
        product_name="烟气",
        # 工艺单元
        process_unit="二套ARGG",
        # 车间工段
        workshop_section="炼油生产二部催化作业区",
        # 最终等级
        final_grade="合格",
        # 主组
        main_group="质量检验中心",
        # 测试编号
        test_number="5007045",
        # 分析项目
        analysis="YP3焦炉煤气",
        # 测试订单号
        test_order_number="1",
        # 是否发布
        released="T",
        # 结果编号
        result_number="49568029",
        # 名称
        name="氧气",
        # 结果顺序号
        result_order_number="3",
        # 单位显示
        units_display=" %(体积分数)",
        # 格式化输入
        formatted_entry="4.82",
        # 结果类型
        result_type="K",
        # 结果标准
        result_standard="≤7（过程监控）",
        # 结果是否符合规格
        result_in_spec="T",
        # 是否可报告
        reportable="T",
        # 报告名称
        reported_name="氧气",
        # 父样品
        parent_aliquot='0',
        # 报告名称
        sp_reportName="余锅入口水封罐",
        # 工厂
        plant="炼油二部",
        # 站点
        site="大庆炼化分公司",
        # 分析标准
        analysis_standard="GB/T 28901-2012",
        # 修改人
        changed_by="马国军",
        # 修改时间
        changed_on="2025/10/29 10:47:05",
        # 发布人
        released_by="马国军",
        # 发布时间
        released_on="2025/10/29 10:47:00",
        # 是否移除
        remove="F",
        # COA签发人
        coa_by=None,
        # 测试类型
        test_type="油品站色谱综合岗",
        # 取样时间
        drawtime="08:00:00",
        # 录入人
        entred_by="张海峰",
        # 测试审核人
        test_reviewer="尹丽萍",
        # 样品审核人
        sample_reviewer="马国军",
        # 搜索时间
        searchTime="2025/10/29 8:00:00"
    )
    qrExport(request)