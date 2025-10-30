from typing import Optional

from pydantic import BaseModel

class QrExportRes(BaseModel):
    exportSuccess: bool = False

class QrExportReq(BaseModel):

    def to_qr_data(self):
        # 排除特定字段后返回字典
        exclude_fields = {'filename', 'size', 'border', 'fill_color', 'back_color'}
        data_dict = self.dict(exclude=exclude_fields)
        return data_dict

    filename: Optional[str] = None
    size: Optional[int] = None
    border: Optional[int] = None
    fill_color: Optional[str] = None
    back_color: Optional[str] = None
    # 样品编号
    sample_number: Optional[str] = None
    # 产品批次
    product_batch: Optional[str] = None
    # 样品状态
    sample_status: Optional[str] = None
    # 样品是否符合规格
    sample_in_spec: Optional[str] = None
    # 取样日期
    sampled_date: Optional[str] = None
    # 产品
    product: Optional[str] = None
    # 取样点
    sampling_point: Optional[str] = None
    # 样品类型
    sample_type: Optional[str] = None
    # 产品类型
    prod_type: Optional[str] = None
    # 产品名称
    product_name: Optional[str] = None
    # 工艺单元
    process_unit: Optional[str] = None
    # 车间工段
    workshop_section: Optional[str] = None
    # 最终等级
    final_grade: Optional[str] = None
    # 主组
    main_group: Optional[str] = None
    # 测试编号
    test_number: Optional[str] = None
    # 分析项目
    analysis: Optional[str] = None
    # 测试订单号
    test_order_number: Optional[str] = None
    # 是否发布
    released: Optional[str] = None
    # 结果编号
    result_number: Optional[str] = None
    # 名称
    name: Optional[str] = None
    # 结果顺序号
    result_order_number: Optional[str] = None
    # 单位显示
    units_display: Optional[str] = None
    # 格式化输入
    formatted_entry: Optional[str] = None
    # 结果类型
    result_type: Optional[str] = None
    # 结果标准
    result_standard: Optional[str] = None
    # 结果是否符合规格
    result_in_spec: Optional[str] = None
    # 是否可报告
    reportable: Optional[str] = None
    # 报告名称
    reported_name: Optional[str] = None
    # 样品顺序
    samp_order: Optional[str] = None
    # 父样品
    parent_aliquot: Optional[str] = None
    # 报告名称
    sp_reportName: Optional[str] = None
    # 工厂
    plant: Optional[str] = None
    # 站点
    site: Optional[str] = None
    # 产品标准
    prod_standard: Optional[str] = None
    # QA代码
    qa_code: Optional[str] = None
    # 报告代码
    report_code: Optional[str] = None
    # 品牌
    c_brand: Optional[str] = None
    # QA备注
    qa_remark: Optional[str] = None
    # 分析标准
    analysis_standard: Optional[str] = None
    # 修改人
    changed_by: Optional[str] = None
    # 修改时间
    changed_on: Optional[str] = None
    # 发布人
    released_by: Optional[str] = None
    # 发布时间
    released_on: Optional[str] = None
    # 是否移除
    remove: Optional[str] = None
    # COA签发人
    coa_by: Optional[str] = None
    # 测试类型
    test_type: Optional[str] = None
    # 产率
    yield_: Optional[str] = None
    # 其他
    others: Optional[str] = None
    # 生产信息
    manufacture: Optional[str] = None
    # 包装信息
    baoZhuang: Optional[str] = None
    # 样品批次
    samp_batch: Optional[str] = None
    # 自定义属性1
    c_attribute_1: Optional[str] = None
    # 自定义属性2
    c_attribute_2: Optional[str] = None
    # 自定义属性3
    c_attribute_3: Optional[str] = None
    # 自定义属性4
    c_attribute_4: Optional[str] = None
    # 自定义属性5
    c_attribute_5: Optional[str] = None
    # 取样时间
    drawtime: Optional[str] = None
    # 录入人
    entred_by: Optional[str] = None
    # 测试审核人
    test_reviewer: Optional[str] = None
    # 样品审核人
    sample_reviewer: Optional[str] = None
    # COA文件
    coa_file: Optional[str] = None
    # 搜索时间
    searchTime: Optional[str] = None